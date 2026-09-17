from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=50
    )

    chunks = []

    for page in pages:

        text_chunks = splitter.split_text(page["text"])

        for chunk in text_chunks:

            chunks.append({
                "text": chunk,
                "page": page["page"],
                "source": page["source"]
            })

    return chunks