# 📄 AI Document Intelligence

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about their content.

The application extracts text from PDFs, splits the content into chunks, generates embeddings, stores them in a FAISS vector database, retrieves relevant information, and uses a local LLM through Ollama to generate answers.

---

## 🚀 Features

* 📄 Upload PDF documents
* 📚 Support multiple PDF documents
* 🔍 Extract text from PDF files
* ✂️ Split documents into smaller chunks
* 🧠 Generate text embeddings using Sentence Transformers
* ⚡ Store and search embeddings using FAISS
* 🤖 Generate answers using a local LLM with Ollama
* 💬 Interactive Streamlit interface
* 📝 Chat history
* 🧹 Clear Chat functionality
* 📑 Display source document and page numbers
* 🛡️ Answer only using information available in the documents
* ❌ Return a fallback message when information is not available

---

## 🏗️ Architecture

```text
PDF Documents
      │
      ▼
PDF Text Extraction
      │
      ▼
Document Chunking
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
User Question
      │
      ▼
Question Embedding
      │
      ▼
Similarity Search
      │
      ▼
Relevant Document Chunks
      │
      ▼
Ollama LLM
      │
      ▼
Generated Answer
      │
      ▼
Streamlit UI
```

---

## 🛠️ Technologies

* Python 3.11
* Streamlit
* PyMuPDF
* LangChain Text Splitters
* Sentence Transformers
* FAISS
* NumPy
* PyTorch
* Ollama
* Llama 3.2 3B

---

## 📁 Project Structure

```text
AI-Document-Intelligence/
│
├── data/
│   ├── documents/
│   └── faiss_db/
│
├── src/
│   ├── chunker.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── llm.py
│   └── __init__.py
│
├── tests/
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_loader.py
│   └── test_vector_store.py
│
├── app.py
├── build_index.py
├── streamlit_app.py
├── test_pdf.py
├── test_retrieval.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ashishkumarb2315-lab/AI-Document-Intelligence.git
```

```bash
cd AI-Document-Intelligence
```

---

## 2. Python Version

This project requires **Python 3.11.x**.

Python 3.11 is recommended because the project uses **PyTorch 2.5.1**, which is compatible with this Python version.

Python 3.14 is not supported by the current dependency configuration.

---

## 3. Create a Virtual Environment

### Windows

```powershell
py -3.11 -m venv venv
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3.11 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 🤖 Ollama Setup

This project uses Ollama to run the local LLM.

Install Ollama on your system and make sure it is running.

Then download the required model:

```bash
ollama pull llama3.2:3b
```

Verify that the model is available:

```bash
ollama list
```

You should see:

```text
llama3.2:3b
```

---

# 📚 Add Documents

Create the following folder if it does not already exist:

```text
data/documents/
```

Place your PDF files inside this folder.

Example:

```text
data/
└── documents/
    ├── document1.pdf
    ├── document2.pdf
    └── document3.pdf
```

The PDF documents are intentionally excluded from GitHub because users can provide their own documents.

---

# 🧠 Build the FAISS Index

After adding your PDF files, run:

```bash
python build_index.py
```

This process will:

1. Find PDF documents
2. Extract PDF text
3. Split the text into chunks
4. Generate embeddings
5. Store the embeddings in FAISS
6. Store document metadata

The generated FAISS files are stored locally in:

```text
data/faiss_db/
```

---

# ▶️ Run the Streamlit Application

Start the application with:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

You can then:

1. Upload a PDF
2. Process the PDF
3. Ask questions
4. View the generated answer
5. View source documents and page numbers
6. Continue the conversation using chat history

---

# 💡 Example Questions

For a machine learning document:

```text
What are the types of machine learning?
```

```text
What is supervised learning?
```

```text
What is the difference between supervised and unsupervised learning?
```

For a database document:

```text
What is a database management system?
```

```text
What are the advantages of DBMS?
```

The system answers questions using information retrieved from the uploaded documents.

---

# 🔎 How RAG Works

This project follows a Retrieval-Augmented Generation workflow.

### Step 1 — Document Loading

PDF documents are read using PyMuPDF.

### Step 2 — Chunking

Large documents are divided into smaller text chunks using the LangChain text splitter.

### Step 3 — Embeddings

Each chunk is converted into a numerical vector using:

```text
all-MiniLM-L6-v2
```

### Step 4 — Vector Storage

The embeddings are stored in a FAISS vector database.

### Step 5 — Question Embedding

When the user asks a question, the question is converted into an embedding.

### Step 6 — Similarity Search

FAISS searches for the most relevant document chunks.

### Step 7 — Answer Generation

The retrieved context is provided to the local:

```text
llama3.2:3b
```

model through Ollama.

### Step 8 — Response

The generated answer is displayed in the Streamlit application together with source document and page information.

---

# 🧪 Testing

The project includes tests for:

* Document loading
* Document chunking
* Embedding generation
* Vector store functionality
* Retrieval

Run the tests with:

```bash
pytest
```

---

# 🔐 Privacy

The project is designed to use a **local LLM through Ollama**.

Documents and FAISS indexes are stored locally and are not included in the GitHub repository.

PDF files placed in:

```text
data/documents/
```

are excluded from Git tracking.

---

# 📌 Current Project Capabilities

The application currently supports:

* Multiple PDF documents
* PDF text extraction
* Document chunking
* Semantic embeddings
* FAISS similarity search
* Local LLM generation
* Source document identification
* Page-level source information
* Streamlit UI
* Chat history
* Clear Chat
* Out-of-document fallback responses

For example, when information cannot be found in the documents, the system responds:

```text
I could not find enough information in the document.
```

---

# 🔮 Future Improvements

Possible future improvements include:

* Better document filtering
* Improved retrieval ranking
* Metadata filtering
* Hybrid search
* Conversation-aware retrieval
* Document deletion
* Document management UI
* Authentication
* Cloud deployment
* Azure integration
* Advanced RAG techniques
* Improved evaluation and monitoring

---

# 👨‍💻 Author

**Ashish Kumar**

GitHub:

https://github.com/ashishkumarb2315-lab
