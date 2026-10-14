import chromadb
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Connect to our existing ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Get our existing collection
collection = client.get_collection(
    name="memory_vault"
)


def retrieve(query, top_k=3):

    # Convert the user's question into a vector
    query_embedding = model.encode(query).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results