from langchain_community.document_loaders import TextLoader


def load_documents():

    files = [
        "rag/knowledge_base/loan_policy.txt",
        "rag/knowledge_base/credit_card_rules.txt",
        "rag/knowledge_base/banking_faqs.txt",
        "rag/knowledge_base/escalation_guidelines.txt"
    ]

    documents = []

    for file in files:

        loader = TextLoader(file)

        documents.extend(loader.load())

    return documents