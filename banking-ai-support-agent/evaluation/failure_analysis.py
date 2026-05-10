failure_analysis = [

    {
        "issue":
        "Some responses are too short.",

        "root_cause":
        "Prompt instructions encourage concise responses.",

        "solution":
        "Improve prompt engineering for detailed explanations."
    },

    {
        "issue":
        "Limited financial domain knowledge.",

        "root_cause":
        "Small RAG knowledge base.",

        "solution":
        "Add more banking PDFs and policy documents."
    },

    {
        "issue":
        "No numerical EMI calculator.",

        "root_cause":
        "No financial calculator tool integrated.",

        "solution":
        "Add EMI calculator tool."
    },

    {
        "issue":
        "Weak multi-turn contextual memory.",

        "root_cause":
        "Simple conversation history mechanism.",

        "solution":
        "Use vector memory retrieval."
    }
]

for item in failure_analysis:

    print("\n==========================")
    print("ISSUE:", item["issue"])
    print("ROOT CAUSE:", item["root_cause"])
    print("SOLUTION:", item["solution"])