# 📄 AI Document Intelligence

An AI-powered document question-answering application that allows users to upload PDF documents and ask questions using natural language.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from documents and generate answers using a local Large Language Model.

## 🚀 Features

* 📄 Upload PDF documents
* ✂️ Split documents into smaller chunks
* 🧠 Generate semantic embeddings using Sentence Transformers
* 🔎 Perform similarity search using FAISS
* 🤖 Generate answers using Ollama and Llama 3.2
* 💬 Interactive Streamlit web interface
* 📚 Support for multiple documents
* 📌 Display source document and page number
* 🧪 Unit tests for core components
* 🔒 Runs locally without requiring an external LLM API

## 🏗️ Architecture

```text
PDF Documents
      ↓
Document Loader
      ↓
Text Chunking
      ↓
Sentence Transformer Embeddings
      ↓
FAISS Vector Store
      ↓
Similarity Search
      ↓
Relevant Document Context
      ↓
Ollama / Llama 3.2
      ↓
Generated Answer
      ↓
Streamlit UI
```

## 🛠️ Technologies Used

* Python
* Streamlit
* FAISS
* Sentence Transformers
* PyMuPDF
* LangChain Text Splitters
* Ollama
* Llama 3.2
* NumPy
* PyTorch

## 📁 Project Structure

```text
AI-Document-Intelligence/
│
├── data/
│   └── documents/
│
├── src/
│   ├── chunker.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── llm.py
│   └── vector_store.py
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
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashishkumarb2315-lab/AI-Document-Intelligence.git
```

### 2. Open the project folder

```bash
cd AI-Document-Intelligence
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Python dependencies

```powershell
pip install -r requirements.txt
```

## 🤖 Install Ollama

Install Ollama on your computer.

Then download the Llama 3.2 model:

```powershell
ollama pull llama3.2:3b
```

Make sure Ollama is running before starting the application.

## 📄 Add Documents

Place your PDF files inside:

```text
data/documents/
```

The application will read the PDF files, extract their text, split the text into chunks, and prepare them for semantic search.

## 🧠 Build the FAISS Index

Run:

```powershell
python build_index.py
```

This will:

1. Find the PDF documents.
2. Extract text from the PDFs.
3. Split the text into chunks.
4. Generate embeddings.
5. Store the embeddings in FAISS.

## ▶️ Run the Streamlit Application

Run:

```powershell
streamlit run streamlit_app.py
```

Then open the URL displayed in the terminal, usually:

```text
http://localhost:8501
```

The application will open in your web browser.

## 💬 Example Questions

You can ask questions such as:

```text
What is supervised learning?
```

```text
What are the types of machine learning?
```

```text
What is a database management system?
```

The application retrieves relevant document content and uses that context to generate the answer.

## 🔍 How RAG Works in This Project

The application follows a Retrieval-Augmented Generation workflow.

### 1. Document Loading

PDF documents are loaded using PyMuPDF.

### 2. Chunking

Large document text is divided into smaller chunks using a recursive text splitter.

### 3. Embedding Generation

Each chunk is converted into a numerical vector using:

```text
all-MiniLM-L6-v2
```

### 4. Vector Storage

The embeddings are stored in a FAISS vector index.

### 5. Retrieval

When the user asks a question, the question is converted into an embedding and compared with the stored document vectors.

### 6. Context Generation

The most relevant document chunks are retrieved.

### 7. Answer Generation

The retrieved context is provided to the local Llama 3.2 model through Ollama.

### 8. User Interface

The final answer is displayed through Streamlit along with the relevant document sources.

## 🧪 Testing

The project includes tests for:

* Document loading
* Text chunking
* Embedding generation
* Vector store functionality

Run the tests using:

```powershell
pytest
```

## 🔐 Privacy

The application is designed to run locally.

Documents are processed on the local machine and the LLM is accessed through Ollama.

PDF documents and generated vector databases are excluded from the Git repository using `.gitignore`.

## 📌 Future Improvements

* Better document metadata filtering
* Conversation memory
* Improved retrieval and reranking
* Support for additional document formats
* Authentication and user management
* Cloud deployment
* Advanced document citation
* Hybrid keyword and semantic search

## 👩‍💻 Author

**Ashish Kumar**

GitHub:
https://github.com/ashishkumarb2315-lab
