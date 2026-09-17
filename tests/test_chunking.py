from src.document_loader import load_pdf
from src.chunker import create_chunks


pdf_path = "data/documents/AI and Machine Learning.pdf"

pages = load_pdf(pdf_path)

chunks = create_chunks(pages)

print("Total pages:", len(pages))
print("Total chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0]["text"])

print("\nSource:", chunks[0]["source"])
print("Page:", chunks[0]["page"])