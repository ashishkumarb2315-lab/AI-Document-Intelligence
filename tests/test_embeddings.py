from src.document_loader import load_pdf
from src.chunker import split_documents
from src.embeddings import generate_embeddings


pdf_path = "data/documents/AI and Machine Learning.pdf"


pages = load_pdf(pdf_path)

chunks = split_documents(pages)

texts = [chunk["text"] for chunk in chunks]

embeddings = generate_embeddings(texts)


print("PDF loaded successfully!")
print("Total pages:", len(pages))

print("Total chunks:", len(chunks))

print("Embeddings generated successfully!")

print("Embedding shape:", embeddings.shape)

print("\nFirst embedding:")
print(embeddings[0])

