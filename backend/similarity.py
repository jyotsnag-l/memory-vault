from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer # type: ignore


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


KNOWLEDGE_DIR = Path("../knowledge")


def load_documents():
    documents = []

    for file_path in KNOWLEDGE_DIR.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        chunks = text.split("\n\n")

        for chunk in chunks:
            chunk = chunk.strip()

            if chunk:
                documents.append({
                    "filename": file_path.name,
                    "content": f"Atlas Project - {file_path.stem}:\n{chunk}"
                })

    return documents


def cosine_similarity(vector_a, vector_b):
    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )


documents = load_documents()

question = input("Ask a question: ")

question_embedding = model.encode(question)


results = []

for document in documents:

    document_embedding = model.encode(document["content"])

    similarity = cosine_similarity(
        question_embedding,
        document_embedding
    )

    results.append({
        "filename": document["filename"],
        "content": document["content"],
        "similarity": similarity
    })


results.sort(
    key=lambda x: x["similarity"],
    reverse=True
)


print("\nTop results:\n")

for result in results[:3]:

    print("=" * 60)

    print("File:", result["filename"])

    print("Similarity:", result["similarity"])

    print("Content:")
    print(result["content"])