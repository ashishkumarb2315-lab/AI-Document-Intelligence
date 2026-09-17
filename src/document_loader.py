import pymupdf
from pathlib import Path


def load_pdf(file_path):

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document):

        text = page.get_text()

        pages.append({
            "text": text,
            "page": page_number + 1,
            "source": Path(file_path).name
        })

    document.close()

    return pages