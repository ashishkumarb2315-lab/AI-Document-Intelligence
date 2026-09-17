
import chromadb

print("1. Starting", flush=True)

client = chromadb.PersistentClient(
    path="data/chroma_test"
)

print("2. Client created", flush=True)

collection = client.get_or_create_collection(
    name="test_collection",
    embedding_function=None
)

print("3. Collection created", flush=True)

collection.upsert(
    ids=["test1"],
    documents=["hello"],
    embeddings=[[0.1] * 384],
    metadatas=[{"source": "test", "page": 1}]
)

print("4. Upsert successful", flush=True)

print("5. Count:", collection.count(), flush=True)