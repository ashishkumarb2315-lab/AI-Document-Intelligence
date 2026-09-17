import os
import pymupdf

from src.chunker import split_documents
from src.embeddings import generate_embeddings
from src.vector_store import store_chunks


DOCUMENTS_PATH = "data/documents"


print("STEP 1: Finding PDF documents")

pdf_files = []

for filename in os.listdir(DOCUMENTS_PATH):

    if filename.lower().endswith(".pdf"):

        pdf_files.append(
            os.path.join(
                DOCUMENTS_PATH,
                filename
            )
        )


print("PDF files found:", len(pdf_files))

for pdf in pdf_files:
    print("-", pdf)


print("\nSTEP 2: Loading documents")

pages = []

for pdf_path in pdf_files:

    print("\nOpening:", pdf_path)

    document = pymupdf.open(pdf_path)

    print("Pages:", len(document))

    for page_number, page in enumerate(document):

        pages.append({
            "text": page.get_text(),
            "page": page_number + 1,
            "source": pdf_path
        })


print("\nTotal pages loaded:", len(pages))


print("\nSTEP 3: Creating chunks")

chunks = split_documents(pages)

print("Chunks created:", len(chunks))


print("\nSTEP 4: Generating embeddings")

texts = [chunk["text"] for chunk in chunks]

embeddings = generate_embeddings(texts)

print("Embeddings shape:", embeddings.shape)


print("\nSTEP 5: Storing in FAISS")

store_chunks(
    chunks,
    embeddings
)


print("\n===== INDEX BUILD COMPLETE =====")

print("Total PDF files:", len(pdf_files))
print("Total pages:", len(pages))
print("Total chunks:", len(chunks))
print("Total vectors:", len(embeddings))