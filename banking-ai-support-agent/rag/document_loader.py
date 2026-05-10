import os

from langchain_community.document_loaders import (
    TextLoader
)

# =========================================
# KNOWLEDGE BASE PATH
# =========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

KNOWLEDGE_BASE_PATH = os.path.join(
    BASE_DIR,
    "knowledge_base"
)

# =========================================
# LOAD DOCUMENTS
# =========================================

def load_documents():

    documents = []

    for file_name in os.listdir(
        KNOWLEDGE_BASE_PATH
    ):

        if file_name.endswith(".txt"):

            file_path = os.path.join(
                KNOWLEDGE_BASE_PATH,
                file_name
            )

            loader = TextLoader(
                file_path,
                encoding="utf-8"
            )

            documents.extend(
                loader.load()
            )

    return documents