# 📄 AI Document Intelligence

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about their content.

The application extracts text from PDFs, splits the content into chunks, generates embeddings, stores them in a FAISS vector database, retrieves relevant information, and uses an LLM to generate document-grounded answers.

The application supports **Gemini Cloud LLM for deployment** and **Ollama for local LLM usage**.

## 🚀 Live Demo

👉 [Open AI Document Intelligence](https://ai-document-intelligence-mnspnejdsvthhuxnzfwcjm.streamlit.app/)

---

## 🚀 Features

* 📄 Upload PDF documents
* 📚 Support multiple PDF documents
* 🔍 Extract text from PDF files
* ✂️ Split documents into smaller chunks
* 🧠 Generate text embeddings using Sentence Transformers
* ⚡ Store and search embeddings using FAISS
* 🤖 Generate answers using Gemini Cloud LLM
* 🖥️ Use Ollama for local LLM generation
* 💬 Interactive Streamlit interface
* 📝 Chat history
* 🧹 Clear Chat functionality
* 📑 Display source document and page numbers
* 🛡️ Answer only using information available in the documents
* ❌ Return a fallback message when information is not available
* ☁️ Deployable on Streamlit Community Cloud

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
LLM
 ┌────┴─────┐
 │          │
 ▼          ▼
Ollama    Gemini
Local     Cloud
 │          │
 └────┬─────┘
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
* Google Gemini API
* Google GenAI SDK

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

Python 3.11 is recommended because the project uses PyTorch 2.5.1 and the current dependency configuration is tested with Python 3.11.

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

# 🤖 Local Ollama Setup

For local development, the application can use Ollama with the Llama 3.2 3B model.

Install Ollama and make sure it is running.

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

# 🔐 Gemini Cloud Setup

For Streamlit Cloud deployment, the application uses the Google Gemini API.

Create a Gemini API key and configure it as a Streamlit secret.

Use the following secret name:

```text
GEMINI_API_KEY
```

Do not commit the API key to GitHub.

The application checks for `GEMINI_API_KEY` and uses Gemini when the key is available.

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

# ☁️ Streamlit Cloud Deployment

The application can be deployed using Streamlit Community Cloud.

### Deployment steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new application.
4. Select the GitHub repository.
5. Select the `main` branch.
6. Set the main file to:

```text
streamlit_app.py
```

7. Configure the application secret:

```toml
GEMINI_API_KEY = "your-api-key"
```

8. Deploy the application.

The deployed application uses Gemini for cloud-based answer generation.

### Live Application

👉 [Open AI Document Intelligence](https://ai-document-intelligence-mnspnejdsvthhuxnzfwcjm.streamlit.app/)

---

# 💡 Example Questions

### Machine Learning

```text
What are the types of machine learning?
```

```text
What is supervised learning?
```

```text
What is the difference between supervised and unsupervised learning?
```

### Database

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

The retrieved document context is provided to the configured LLM.

For local execution, the application can use:

```text
llama3.2:3b
```

through Ollama.

For cloud deployment, the application uses:

```text
Gemini
```

through the Google GenAI SDK.

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

The application has also been tested with:

* In-document questions
* Out-of-document questions
* Multiple PDF documents
* Source document identification
* Page-level source information

When information cannot be found in the documents, the system responds:

```text
I could not find enough information in the document.
```

---

# 🔐 Privacy

The project supports local document processing and local LLM usage through Ollama.

For cloud deployment, Gemini is used for answer generation.

Documents and FAISS indexes are not included in the GitHub repository.

PDF files placed in:

```text
data/documents/
```

are excluded from Git tracking.

API keys should never be committed to the repository.

---

# 📌 Current Project Capabilities

The application currently supports:

* Multiple PDF documents
* PDF text extraction
* Document chunking
* Semantic embeddings
* FAISS similarity search
* Local LLM generation through Ollama
* Cloud LLM generation through Gemini
* Source document identification
* Page-level source information
* Streamlit UI
* Chat history
* Clear Chat
* Out-of-document fallback responses
* Streamlit Cloud deployment

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
* Azure integration
* Advanced RAG techniques
* Improved evaluation and monitoring

---

# 👨‍💻 Author

**Ashish Kumar**

GitHub:

https://github.com/ashishkumarb2315-lab

