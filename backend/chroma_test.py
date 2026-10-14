import chromadb
from sentence_transformers import SentenceTransformer # type: ignore


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="memory_vault"
)


question = "What database does Atlas use?"


question_embedding = model.encode(
    question
).tolist()


results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)


print("\nQuestion:")
print(question)

print("\nTop 3 retrieved chunks:")

for i in range(3):

    print("\n" + "=" * 60)

    print("Result:", i + 1)

    print("Document:", results["ids"][0][i])

    print("Distance:", results["distances"][0][i])

    print("Content:")
    print(results["documents"][0][i])