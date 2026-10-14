from pathlib import Path


KNOWLEDGE_DIR = Path("../knowledge")


def load_documents():
    documents = []

    for file_path in KNOWLEDGE_DIR.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "filename": file_path.name,
            "content": text
        })

    return documents


def chunk_document(text):
    chunks = text.split("\n\n")

    return [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]


if __name__ == "__main__":
    documents = load_documents()

    for document in documents:
        print("\n" + "=" * 50)
        print(document["filename"])
        print("=" * 50)

        chunks = chunk_document(document["content"])

        for index, chunk in enumerate(chunks):
            print(f"\n--- Chunk {index + 1} ---")
            print(chunk)