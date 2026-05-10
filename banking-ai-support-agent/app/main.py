import logging

from llm.openai_client import get_llm_response
from agent.safety_guardrails import is_unsafe_query
from rag.retriever import retrieve_context
from tools.tool_router import route_tool

from memory.conversation_memory import (
    save_message,
    get_history
)

from feedback.adaptation_engine import (
    get_adaptation_rules
)

# =========================================
# LOGGING CONFIGURATION
# =========================================

logging.basicConfig(
    filename="logs/phase8_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================================
# LOAD PROMPT
# =========================================

def load_prompt(prompt_file):

    with open(prompt_file, "r") as file:

        return file.read()

# =========================================
# GENERATE RESPONSE
# =========================================

def generate_response(user_input):

    # =====================================
    # SAFETY CHECK
    # =====================================

    if is_unsafe_query(user_input):

        refusal_response = (
            "I cannot assist with "
            "transactional or unsafe requests."
        )

        logging.warning(
            f"UNSAFE QUERY: {user_input}"
        )

        return refusal_response

    # =====================================
    # TOOL ROUTING
    # =====================================

    tool_name, tool_response = route_tool(
        user_input
    )

    if tool_name != "none":

        logging.info(
            f"TOOL USED: {tool_name}"
        )

        logging.info(
            f"TOOL RESPONSE: {tool_response}"
        )

        save_message(
            "user",
            user_input
        )

        save_message(
            "assistant",
            tool_response
        )

        return tool_response

    # =====================================
    # LOAD SYSTEM PROMPT
    # =====================================

    system_prompt = load_prompt(
        "llm/prompt_versions/v2_safe_rag.txt"
    )

    # =====================================
    # RAG RETRIEVAL
    # =====================================

    retrieved_context = retrieve_context(
        user_input
    )

    if not retrieved_context.strip():

        retrieved_context = (
            "No relevant banking information "
            "was found."
        )

        logging.warning(
            f"NO CONTEXT FOUND: {user_input}"
        )

    # =====================================
    # MEMORY
    # =====================================

    memory = get_history()

    # =====================================
    # ADAPTIVE BEHAVIOUR
    # =====================================

    adaptation_rules = (
        get_adaptation_rules()
    )

    # =====================================
    # FINAL PROMPT
    # =====================================

    final_prompt = f"""
    {system_prompt}

    Conversation Memory:
    {memory}

    Adaptation Rules:
    {adaptation_rules}

    Retrieved Banking Context:
    {retrieved_context}

    Customer Question:
    {user_input}

    Instructions:
        - Use memory for contextual understanding.
        - Use adaptation rules to improve responses.
        - Remain strictly non-transactional.
        - Answer banking-related questions only.
        - Explain uncertainty clearly.
        - Refuse unsafe requests politely.
        - Give detailed explanations with examples when possible.
        - Explain banking concepts in simple language.
        - Use bullet points for clarity.
        - Provide educational guidance only.
    """

    # =====================================
    # LLM RESPONSE
    # =====================================

    response = get_llm_response(
        final_prompt
    )

    # =====================================
    # SAVE MEMORY
    # =====================================

    save_message(
        "user",
        user_input
    )

    save_message(
        "assistant",
        response
    )

    # =====================================
    # LOGGING
    # =====================================

    logging.info(
        f"USER: {user_input}"
    )

    logging.info(
        f"MEMORY: {memory}"
    )

    logging.info(
        f"ADAPTATION RULES: "
        f"{adaptation_rules}"
    )

    logging.info(
        f"RETRIEVED CONTEXT: "
        f"{retrieved_context}"
    )

    logging.info(
        f"BOT: {response}"
    )

    logging.info("-" * 80)

    return response

# =========================================
# CLI MAIN FUNCTION
# =========================================

def main():

    print("\n===== AI Banking Support Agent =====")

    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":

            print("\nGoodbye!")

            break

        try:

            # =================================
            # FEEDBACK SHORTCUTS
            # =================================

            if user_input.lower() in [
                "too long",
                "more detail",
                "good response"
            ]:

                print(
                    "\nFeedback received.\n"
                )

                continue

            # =================================
            # GENERATE RESPONSE
            # =================================

            response = generate_response(
                user_input
            )

            print(
                f"\nBot: {response}\n"
            )

        except Exception as error:

            logging.exception(error)

            print(
                "\nBot: Internal error occurred.\n"
            )

# =========================================
# APPLICATION ENTRY POINT
# =========================================

if __name__ == "__main__":

    main()