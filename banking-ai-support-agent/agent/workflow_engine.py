from tools.emi_calculator import calculate_emi
from tools.branch_locator import locate_branch


def execute_workflow(query):

    responses = []

    if "emi" in query.lower():

        emi = calculate_emi(500000, 8.5, 5)

        responses.append(f"Estimated EMI: ₹{emi}")

    if "branch" in query.lower():

        branch = locate_branch("mumbai")

        responses.append(branch)

    return "\n".join(responses)