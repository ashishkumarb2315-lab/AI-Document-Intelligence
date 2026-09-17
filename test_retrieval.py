from src.embeddings import generate_embeddings
from src.vector_store import search_chunks

question = "What are the types of machine learning?"

embedding = generate_embeddings([question])

results = search_chunks(
    embedding,
    top_k=15
)

print("\n--- RETRIEVED RESULTS ---\n")

for result in results:
    print("Page:", result["page"])
    print(result["text"])
    print("\n" + "-" * 60)