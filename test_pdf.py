import fitz

pdf_path = "data/documents/AI and Machine Learning.pdf"

document = fitz.open(pdf_path)

print("PDF opened successfully!")
print("Number of pages:", len(document))

for page_number, page in enumerate(document):
    text = page.get_text()

    print("\n" + "=" * 60)
    print("PAGE:", page_number + 1)
    print("=" * 60)

    print(text[:1000])
import fitz

print("PyMuPDF is working!")