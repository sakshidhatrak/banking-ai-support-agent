from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def split_documents(documents):

    # =====================================
    # REMOVE EMPTY DOCUMENTS
    # =====================================

    valid_documents = []

    for document in documents:

        if (
            document.page_content
            and document.page_content.strip()
        ):

            valid_documents.append(
                document
            )

    # =====================================
    # TEXT SPLITTER
    # =====================================

    text_splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )
    )

    chunks = text_splitter.split_documents(
        valid_documents
    )

    # =====================================
    # REMOVE EMPTY CHUNKS
    # =====================================

    valid_chunks = []

    for chunk in chunks:

        if (
            chunk.page_content
            and chunk.page_content.strip()
        ):

            valid_chunks.append(chunk)

    return valid_chunks