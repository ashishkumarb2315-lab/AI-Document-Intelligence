from src.embeddings import generate_embeddings
from src.vector_store import search_chunks
from src.llm import generate_answer


print("=" * 60)
print("        AI DOCUMENT INTELLIGENCE")
print("=" * 60)

print("\nAsk questions about your document.")
print("Type 'exit' to close the application.\n")


while True:

    query = input("Enter your question: ")

    if query.lower() == "exit":
        print("\nApplication closed.")
        break

    if not query.strip():
        print("Please enter a question.\n")
        continue

    print("\nSearching the document...")

    query_embedding = generate_embeddings([query])

    try:

        results = search_chunks(
            query_embedding,
            top_k=10
        )

    except FileNotFoundError as e:

        print("\nERROR:")
        print(e)
        break

    context = ""

    for result in results:

        context += (
            f"Page {result['page']}:\n"
            f"{result['text']}\n\n"
        )

    print("\nGenerating answer...")

    answer = generate_answer(
        question=query,
        context=context
    )

    print("\n===== ANSWER =====")
    print(answer)

    print("\n===== SOURCES =====")

    seen_sources = set()

    for result in results:

        source_key = (
            result["source"],
            result["page"]
        )

        if source_key not in seen_sources:

            print(
                f"- Page {result['page']}"
            )

            seen_sources.add(source_key)

    print("\n" + "=" * 60 + "\n")