print("STEP 1: Starting RAG test")

from src.embeddings import generate_embeddings
from src.vector_store import search_chunks
from src.llm import generate_answer

print("STEP 2: Imports successful")


query = input("Enter your question: ")
print("STEP 3: User question:")
print(query)


print("STEP 4: Generating question embedding")

query_embedding = generate_embeddings([query])

print("STEP 5: Question embedding generated")


print("STEP 6: Searching FAISS")

try:

    results = search_chunks(
        query_embedding,
        top_k=5
    )

except FileNotFoundError as e:

    print("\nERROR:")
    print(e)

    exit()

print("STEP 7: Relevant chunks retrieved")


print("\n===== CONTEXT FOR LLM =====\n")

context = ""

for i, result in enumerate(results, start=1):

    print(f"--- Chunk {i} | Page {result['page']} ---")
    print(result["text"])
    print()

    context += (
        f"Page {result['page']}:\n"
        f"{result['text']}\n\n"
    )


print("===== FINAL CONTEXT =====")
print(context)
print("\n===== ASKING LLAMA =====\n")

answer = generate_answer(
    question=query,
    context=context
)

print("===== FINAL ANSWER =====")
print(answer)

print("\n===== SOURCES =====")

seen_sources = set()

for result in results:

    source_key = (
        result["source"],
        result["page"]
    )

    if source_key not in seen_sources:

        print(f"\n--- Page {result['page']} ---")
        print(result["text"])

        seen_sources.add(source_key)