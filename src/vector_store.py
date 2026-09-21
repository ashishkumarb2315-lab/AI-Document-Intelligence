import os
import json
import faiss
import numpy as np


DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "faiss_db"
)

INDEX_FILE = os.path.join(
    DB_PATH,
    "documents.index"
)

METADATA_FILE = os.path.join(
    DB_PATH,
    "metadata.json"
)


def get_index(dimension=384):

    os.makedirs(DB_PATH, exist_ok=True)

    if os.path.exists(INDEX_FILE):
        return faiss.read_index(INDEX_FILE)

    return faiss.IndexFlatL2(dimension)


def store_chunks(chunks, embeddings):

    embeddings = np.asarray(
        embeddings,
        dtype="float32"
    )

    os.makedirs(DB_PATH, exist_ok=True)

    index = get_index(
        embeddings.shape[1]
    )

    index.add(embeddings)

    metadata = []

    for chunk in chunks:

        metadata.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "page": chunk["page"]
        })

    faiss.write_index(
        index,
        INDEX_FILE
    )

    with open(
        METADATA_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            ensure_ascii=False,
            indent=2
        )

    return index


def search_chunks(
    query_embedding,
    top_k=15,
    max_distance=1.2
):

    if not os.path.exists(INDEX_FILE):

        raise FileNotFoundError(
            "FAISS index not found. Please run build_index.py first."
        )

    if not os.path.exists(METADATA_FILE):

        raise FileNotFoundError(
            "Metadata file not found. Please run build_index.py first."
        )

    index = get_index()

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    with open(
        METADATA_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        metadata = json.load(f)

    results = []

    added_ids = set()

    for distance, index_id in zip(
        distances[0],
        indices[0]
    ):

        if index_id == -1:
            continue

        if distance > max_distance:
            continue

        if index_id in added_ids:
            continue

        results.append({
            "text": metadata[index_id]["text"],
            "source": metadata[index_id]["source"],
            "page": metadata[index_id]["page"],
            "distance": float(distance)
        })

        added_ids.add(index_id)

    return results