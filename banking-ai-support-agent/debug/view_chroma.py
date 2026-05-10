from dotenv import load_dotenv

load_dotenv()

from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings


embeddings = get_embeddings()

vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

collection = vector_store.get()

print("\n===== STORED CHROMA DOCUMENTS =====\n")

for i, document in enumerate(collection["documents"]):

    print(f"\nDocument {i+1}")
    print("-" * 60)
    print(document)

print("\n===== METADATA =====\n")

for metadata in collection["metadatas"]:

    print(metadata)