from llm.openai_client import get_llm_response
from agent.safety_guardrails import is_unsafe_query


def load_prompt(prompt_file):
    with open(prompt_file, "r") as file:
        return file.read()


def generate_response(user_input):
    if is_unsafe_query(user_input):
        return (
            "I cannot assist with transactional, legal, "
            "or unsafe banking requests."
        )

    system_prompt = load_prompt(
        "llm/prompt_versions/v2_safe_rag.txt"
    )

    final_prompt = f"""
    {system_prompt}

    Customer Question:
    {user_input}
    """

    response = get_llm_response(final_prompt)

    return response