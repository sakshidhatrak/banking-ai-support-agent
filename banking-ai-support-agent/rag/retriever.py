from rag.document_loader import load_documents
from rag.chunking import split_documents
from rag.vector_store import create_vector_store


documents = load_documents()

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)


def retrieve_context(query):

    results = vector_store.similarity_search(
        query,
        k=2
    )

    context = "\n".join(
        [doc.page_content for doc in results]
    )

    return context