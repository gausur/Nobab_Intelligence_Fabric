import chromadb
from sentence_transformers import SentenceTransformer
from src.config import CHROMA_DIR, COLLECTION_NAME

embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection(COLLECTION_NAME)

def add_to_vectorstore(doc_id, text, metadata):
    embedding = embedder.encode([text]).tolist()[0]
    collection.upsert(
        ids=[doc_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata]
    )
    return True
