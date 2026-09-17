import os
import pymupdf
import streamlit as st

from src.chunker import split_documents
from src.embeddings import generate_embeddings
from src.vector_store import search_chunks, store_chunks
from src.llm import generate_answer


st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Document Intelligence")
st.write("Ask questions about your uploaded documents.")


if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


st.subheader("Upload a PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button("Process PDF"):

        with st.spinner("Processing PDF..."):

            os.makedirs(
                "data/documents",
                exist_ok=True
            )

            pdf_path = os.path.join(
                "data/documents",
                uploaded_file.name
            )

            with open(
                pdf_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )


            document = pymupdf.open(
                pdf_path
            )

            pages = []

            for page_number, page in enumerate(
                document
            ):

                pages.append({
                    "text": page.get_text(),
                    "page": page_number + 1,
                    "source": pdf_path
                })


            chunks = split_documents(
                pages
            )

            texts = [
                chunk["text"]
                for chunk in chunks
            ]

            embeddings = generate_embeddings(
                texts
            )

            store_chunks(
                chunks,
                embeddings
            )


        st.success(
            f"PDF processed successfully! "
            f"{len(pages)} pages and "
            f"{len(chunks)} chunks created."
        )


st.subheader("Ask a Question")

question = st.text_input(
    "Enter your question:"
)


if st.button("Ask"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching documents..."
        ):

            query_embedding = generate_embeddings(
                [question]
            )

            try:

                results = search_chunks(
                    query_embedding,
                    top_k=15
                )

            except FileNotFoundError as e:

                st.error(str(e))
                st.stop()


        context = ""

        for result in results:

            context += (
                f"Page {result['page']}:\n"
                f"{result['text']}\n\n"
            )


        with st.spinner(
            "Generating answer..."
        ):

            answer = generate_answer(
                question=question,
                context=context
            )


        st.session_state.chat_history.append({
            "question": question,
            "answer": answer
        })


        st.subheader("Answer")

        st.write(answer)


        if results:

            st.subheader("Sources")

            seen_sources = set()

            for result in results:

                source_key = (
                    result["source"],
                    result["page"]
                )

                if source_key not in seen_sources:

                    document_name = os.path.basename(
                        result["source"]
                    )

                    st.write(
                        f"📄 {document_name} — "
                        f"Page {result['page']}"
                    )

                    seen_sources.add(
                        source_key
                    )


if st.button("🧹 Clear Chat"):

    st.session_state.chat_history = []

    st.rerun()


if st.session_state.chat_history:

    st.subheader("💬 Chat History")

    for chat in reversed(
        st.session_state.chat_history
    ):

        st.markdown(
            f"**You:** {chat['question']}"
        )

        st.markdown(
            f"**AI:** {chat['answer']}"
        )

        st.divider()




