# 🧠 Memory Vault

> A lightweight full-stack RAG application for asking questions from a custom knowledge base.

---

## 🔗 What is it?

**Memory Vault** is a Retrieval-Augmented Generation (RAG) application that combines semantic search with an LLM to generate answers from a custom knowledge base.

The basic flow is:

**📄 Documents → ✂️ Chunks → 🔢 Embeddings → 🗄️ ChromaDB → 🔍 Retrieval → 🤖 LLM → 💬 Answer**

Instead of directly asking the LLM, Memory Vault first retrieves relevant information from the knowledge base and then uses that context to generate the answer.

---

## 🛠️ Tech Stack

<p>
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logoColor=white"/>
</p>

### AI / RAG

- Sentence Transformers
- `all-MiniLM-L6-v2`
- ChromaDB
- Groq API
- `openai/gpt-oss-120b`

---

## 🧠 What I Learnt

- How RAG works internally
- Document chunking
- Text embeddings and vectors
- Semantic similarity search
- Cosine similarity
- Top-K retrieval
- Vector database concepts
- Context construction for LLMs
- Building REST APIs with FastAPI
- Connecting React with a Python backend
- Handling CORS between frontend and backend

---

## ⚙️ How to Run

### Backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install fastapi uvicorn chromadb sentence-transformers groq python-dotenv
```

Create a `.env` file inside `backend/`:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the backend:

```bash
python -m uvicorn main:app --reload
```

### Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL provided by Vite.

---

## 👩🏻‍💻 Built By

**Jyotsna G**

Computer Science (Data Science)
