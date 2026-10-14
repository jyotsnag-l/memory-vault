from sentence_transformers import SentenceTransformer # type: ignore


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


text = "Ayush is responsible for frontend development."

embedding = model.encode(text)


print("Text:")
print(text)

print("\nEmbedding:")
print(embedding)

print("\nNumber of dimensions:")
print(len(embedding)) 