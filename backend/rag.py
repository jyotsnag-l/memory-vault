from retriever import retrieve
from generator import generate_answer


def ask_question(question):

    # 1. Retrieve relevant chunks
    results = retrieve(question, top_k=3)

    # 2. Extract the retrieved text
    documents = results["documents"][0]

    # 3. Combine the chunks into one context
    context = "\n\n".join(documents)

    # 4. Give question + retrieved context to the LLM
    answer = generate_answer(question, context)

    return answer