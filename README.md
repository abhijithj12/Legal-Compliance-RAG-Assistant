⚖️ Legal Compliance RAG Assistant
<p align="center"> <b>Domain-Restricted Legal & Compliance Question-Answering System</b><br> Built with LangChain · Groq (LLaMA 3.1) · ChromaDB · HuggingFace · Streamlit </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" /> <img src="https://img.shields.io/badge/LangChain-RAG-green" /> <img src="https://img.shields.io/badge/VectorDB-ChromaDB-orange" /> <img src="https://img.shields.io/badge/LLM-LLaMA--3.1--8B-purple" /> <img src="https://img.shields.io/badge/License-MIT-lightgrey" /> </p>
📖 Overview

The Legal Compliance RAG Assistant is a Retrieval-Augmented Generation (RAG) system that allows users to upload legal/compliance PDF documents and ask contextual questions grounded strictly in the uploaded content.

The system enforces domain restriction, preventing answers outside legal and compliance topics and minimizing hallucinations by relying only on retrieved document context.

🚀 Features

📄 Upload multiple legal/compliance PDF documents

🧠 Automatic compliance-document validation

✂️ Intelligent document chunking

🔎 Semantic search using vector embeddings

🤖 LLaMA 3.1 (8B) responses via Groq API

🛡 Strict legal-domain enforcement

🎯 Context-based answers (no external knowledge)

🌐 Interactive Streamlit interface

🧠 System Architecture
1️⃣ Document Processing Pipeline

Upload PDF files

Extract text using PyPDFLoader

Validate document relevance (keyword-based compliance detection)

Split documents using RecursiveCharacterTextSplitter

Generate embeddings with:

Alibaba-NLP/gte-base-en-v1.5


Store vectors in ChromaDB (persistent storage)

2️⃣ RAG Question Answering Flow

User submits a query

Retrieve top 5 relevant document chunks

Inject retrieved context into structured legal prompt

Query LLaMA 3.1 (8B) via Groq

Return professional, analytical response

If:

❌ Question is unrelated →
"This system only answers legal and compliance related questions."

❓ Answer not in context →
"I don't know."

🏗 Project Structure

Legal-Compliance-RAG-Assistant/
│
├── main.py # Streamlit frontend
├── project1.py # Core RAG logic
├── vectorstore/ # Persistent Chroma storage
├── .env # Environment variables (not committed)
├── pyproject.toml # Dependencies
├── uv.lock # Locked dependency versions
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository

git clone https://github.com/abhijithj12/Legal-Compliance-RAG-Assistant.git

cd Legal-Compliance-RAG-Assistant

2️⃣ Install Dependencies (Using uv)

This project uses uv for dependency management.

uv sync

No requirements.txt is required.

3️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

Get your key from:
https://console.groq.com/

4️⃣ Run the Application

streamlit run main.py

App will launch at:

http://localhost:8501

🛡 Compliance Validation Logic

Before indexing, the system ensures the document contains at least three legal/compliance-related keywords, such as:

policy

compliance

regulation

clause

audit

liability

governance

data protection

breach

Non-compliant documents are rejected.

🧩 Tech Stack
Layer	Technology
LLM	Groq (LLaMA 3.1-8B-Instant)
Embeddings	HuggingFace gte-base-en-v1.5
Vector Database	ChromaDB
Framework	LangChain
Frontend	Streamlit
PDF Parsing	PyPDFLoader
Dependency Management	uv
📌 Use Cases

Corporate compliance auditing

Regulatory document review

Policy interpretation

Legal clause analysis

Risk & governance assessment

Data protection compliance review

⚠️ Limitations

English documents only

Requires compliance-related PDFs

No external knowledge access

No conversation memory (single-turn queries)

🔮 Future Improvements

ML-based document classification

Citation highlighting in answers

Multi-language support

Authentication & role-based access

Cloud deployment (AWS / GCP / Azure)

Conversational memory

Docker containerization

🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss improvements.

📜 License

This project is licensed under the MIT License.

👤 Author

Abhijith J
AI / Generative AI Enthusiast
GitHub: https://github.com/abhijithj12
