import os
import logging

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader
)

# =========================================
# KNOWLEDGE BASE PATH
# =========================================

KNOWLEDGE_BASE_PATH = "rag/knowledge_base"

# =========================================
# LOAD DOCUMENTS
# =========================================

def load_documents():

    documents = []

    # CREATE FOLDER IF MISSING
    os.makedirs(
        KNOWLEDGE_BASE_PATH,
        exist_ok=True
    )

    for file_name in os.listdir(
        KNOWLEDGE_BASE_PATH
    ):

        file_path = os.path.join(
            KNOWLEDGE_BASE_PATH,
            file_name
        )

        try:

            # =====================================
            # TXT FILES
            # =====================================

            if file_name.endswith(".txt"):

                loader = TextLoader(
                    file_path,
                    encoding="utf-8"
                )

                documents.extend(
                    loader.load()
                )

            # =====================================
            # PDF FILES
            # =====================================

            elif file_name.endswith(".pdf"):

                loader = PyPDFLoader(
                    file_path
                )

                documents.extend(
                    loader.load()
                )

        except Exception as error:

            logging.warning(
                f"Failed to load "
                f"{file_name}: {error}"
            )

            # SKIP BAD FILES
            continue

    return documents