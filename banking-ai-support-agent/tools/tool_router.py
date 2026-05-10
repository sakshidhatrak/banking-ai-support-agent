import re

from tools.emi_calculator import calculate_emi
from tools.branch_locator import locate_branch
from tools.faq_tool import search_faq
from tools.tool_guardrails import is_unsafe_tool_request

from memory.conversation_memory import (
    get_history
)


def route_tool(query):

    query_lower = query.lower()

    # ==========================================
    # SAFETY CHECK
    # ==========================================

    if is_unsafe_tool_request(query):

        return (
            "unsafe",
            "Tool usage blocked due to unsafe request."
        )

    # ==========================================
    # EMI TOOL
    # ==========================================

    if "calculate emi" in query_lower:

        principal = None
        annual_rate = None
        years = None

        current_numbers = re.findall(
            r'\d+\.?\d*',
            query
        )

        # ======================================
        # EXTRACT VALUES
        # ======================================

        if len(current_numbers) >= 3:

            principal = float(
                current_numbers[0]
            )

            annual_rate = float(
                current_numbers[1]
            )

            years = int(
                float(current_numbers[2])
            )

        # ======================================
        # VALIDATE INPUTS
        # ======================================

        if (
            principal is not None
            and annual_rate is not None
            and years is not None
        ):

            try:

                emi = calculate_emi(
                    principal,
                    annual_rate,
                    years
                )

                return (
                    "emi_calculator",
                    (
                        f"For loan amount ₹{principal}, "
                        f"interest rate {annual_rate}%, "
                        f"and tenure {years} years:\n"
                        f"Estimated EMI is ₹{emi}"
                    )
                )

            except Exception as error:

                return (
                    "emi_calculator",
                    f"EMI calculation failed: {error}"
                )

        return (
            "emi_calculator",
            (
                "Please provide:\n"
                "- loan amount\n"
                "- interest rate\n"
                "- loan tenure\n\n"
                "Example:\n"
                "'Calculate EMI for 500000 "
                "at 8.5 for 5 years'"
            )
        )

    # ==========================================
    # EMI FOLLOW-UP WITH MEMORY
    # ==========================================

    elif (
        "tenure" in query_lower
        or "emi" in query_lower
    ):

        history = get_history()

        principal = None
        annual_rate = None
        years = None

        # ======================================
        # GET PREVIOUS EMI CONTEXT
        # ======================================

        for item in reversed(history):

            try:

                if isinstance(item, dict):

                    message = item.get(
                        "message",
                        ""
                    ).lower()

                    if (
                        "loan amount" in message
                        and "interest rate" in message
                    ):

                        numbers = re.findall(
                            r'\d+\.?\d*',
                            message
                        )

                        if len(numbers) >= 3:

                            principal = float(
                                numbers[0]
                            )

                            annual_rate = float(
                                numbers[1]
                            )

                            break

            except Exception:
                pass

        # ======================================
        # GET NEW TENURE
        # ======================================

        tenure_numbers = re.findall(
            r'\d+',
            query
        )

        if len(tenure_numbers) >= 1:

            years = int(
                tenure_numbers[0]
            )

        # ======================================
        # VALIDATE
        # ======================================

        if (
            principal is not None
            and annual_rate is not None
            and years is not None
        ):

            try:

                emi = calculate_emi(
                    principal,
                    annual_rate,
                    years
                )

                return (
                    "emi_calculator",
                    (
                        f"For loan amount ₹{principal}, "
                        f"interest rate {annual_rate}%, "
                        f"and tenure {years} years:\n"
                        f"Estimated EMI is ₹{emi}"
                    )
                )

            except Exception as error:

                return (
                    "emi_calculator",
                    f"EMI calculation failed: {error}"
                )

        return (
            "emi_calculator",
            (
                "No previous EMI context found.\n"
                "Please provide:\n"
                "- loan amount\n"
                "- interest rate\n"
                "- loan tenure"
            )
        )

    # ==========================================
    # BRANCH TOOL
    # ==========================================

    elif (
        "branch" in query_lower
        or "nearby branch" in query_lower
        or "nearest branch" in query_lower
    ):

        if "mumbai" in query_lower:

            city = "mumbai"

        elif "pune" in query_lower:

            city = "pune"

        elif "delhi" in query_lower:

            city = "delhi"

        else:

            city = "unknown"

        branch = locate_branch(city)

        return (
            "branch_locator",
            branch
        )

    # ==========================================
    # FAQ TOOL
    # ==========================================

    elif (
        "blocked card" in query_lower
        or "credit card" in query_lower
    ):

        faq_response = search_faq(query)

        return (
            "faq_tool",
            faq_response
        )

    # ==========================================
    # NO TOOL FOUND
    # ==========================================

    return (
        "none",
        None
    )