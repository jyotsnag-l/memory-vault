from retriever import retrieve


results = retrieve(
    "What database does Atlas use?"
)


for i, document in enumerate(results["documents"][0]):
    print(f"\nResult {i + 1}")
    print(document)