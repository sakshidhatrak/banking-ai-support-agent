from llm.openai_client import get_llm_response


TEST_QUERY = "What is a home loan?"


def load_prompt(prompt_file):
    with open(prompt_file, "r") as file:
        return file.read()


prompt_files = [
    "llm/prompt_versions/v1_basic.txt",
    "llm/prompt_versions/v2_safe_rag.txt",
    "llm/prompt_versions/v3_tool_memory.txt"
]


print("\n===== Prompt Comparison Testing =====\n")

for prompt_file in prompt_files:

    system_prompt = load_prompt(prompt_file)

    final_prompt = f"""
    {system_prompt}

    Customer Question:
    {TEST_QUERY}
    """

    response = get_llm_response(final_prompt)

    print(f"\nPrompt File: {prompt_file}")
    print("-" * 60)
    print(response)
    print("-" * 60)