from src.document_loader import load_pdf


pdf_path = "data/documents/AI and Machine Learning.pdf"

pages = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Total pages:", len(pages))

print("\nFirst page:")
print(pages[0]["text"][:1000])

print("\nSource:")
print(pages[0]["source"])

print("\nPage number:")
print(pages[0]["page"])