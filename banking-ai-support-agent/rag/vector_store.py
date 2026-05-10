from langchain_community.vectorstores import (
    Chroma
)

from rag.embeddings import get_embeddings


def create_vector_store(chunks):

    # =====================================
    # SAFETY CHECK
    # =====================================

    if not chunks:

        raise ValueError(
            "No valid document chunks found "
            "for vector database creation."
        )

    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vector_store