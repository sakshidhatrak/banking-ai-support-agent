import os
import logging

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader
)

# =========================================
# ABSOLUTE PATH FIX
# =========================================

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

KNOWLEDGE_BASE_PATH = os.path.join(
    CURRENT_DIR,
    "knowledge_base"
)

# =========================================
# LOAD DOCUMENTS
# =========================================

def load_documents():

    documents = []

    logging.warning(
        f"Knowledge Base Path: "
        f"{KNOWLEDGE_BASE_PATH}"
    )

    if not os.path.exists(
        KNOWLEDGE_BASE_PATH
    ):

        logging.warning(
            "Knowledge base folder missing."
        )

        return []

    for file_name in os.listdir(
        KNOWLEDGE_BASE_PATH
    ):

        file_path = os.path.join(
            KNOWLEDGE_BASE_PATH,
            file_name
        )

        try:

            # TXT FILES
            if file_name.endswith(".txt"):

                loader = TextLoader(
                    file_path,
                    encoding="utf-8"
                )

                docs = loader.load()

                documents.extend(docs)

            # PDF FILES
            elif file_name.endswith(".pdf"):

                loader = PyPDFLoader(
                    file_path
                )

                docs = loader.load()

                documents.extend(docs)

        except Exception as error:

            logging.warning(
                f"Failed loading "
                f"{file_name}: {error}"
            )

    logging.warning(
        f"Documents Loaded: "
        f"{len(documents)}"
    )

    return documents
