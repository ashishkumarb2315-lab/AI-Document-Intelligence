@"
import chromadb
import time

print("A: Import complete", flush=True)

client = chromadb.Client()
print("B: Client created", flush=True)

collection = client.get_or_create_collection("debug_test")
print("C: Collection created", flush=True)

print("D: About to add", flush=True)

collection.add(
    ids=["test1"],
    documents=["hello"]
)

print("E: Add completed", flush=True)

print("Count:", collection.count(), flush=True)
"@ | Set-Content .\chroma_debug.py
