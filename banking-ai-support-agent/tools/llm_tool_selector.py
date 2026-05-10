_from llm.openai_client import get_llm_response


def select_tool(user_query):

    prompt = f"""
    You are a banking tool routing assistant.

    Available tools:
    - emi_calculator
    - branch_locator
    - faq_tool

    Return ONLY the tool name.

    User Query:
    {user_query}
    """

    response = get_llm_response(prompt)

    return response.strip().lower()