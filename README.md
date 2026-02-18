⚖️ Legal Compliance RAG Assistant

An AI-powered Legal & Compliance Question-Answering System built using LangChain, Groq (LLaMA 3.1), ChromaDB, HuggingFace Embeddings, and Streamlit.

Upload legal/compliance PDF documents and ask contextual questions using a Retrieval-Augmented Generation (RAG) pipeline.

🚀 Live Capabilities

📄 Upload multiple legal PDF documents

🧠 Automatic compliance-document validation

✂️ Intelligent document chunking

🔎 Semantic search using vector embeddings

🤖 LLaMA 3.1 (8B) powered responses via Groq

🛡 Strict domain-restricted answering (legal/compliance only)

🎯 Context-based answers (No hallucination beyond documents)

🌐 Clean Streamlit web interface

🧠 Architecture Overview
1️⃣ Document Processing Pipeline

Upload PDFs

Extract text using PyPDFLoader

Validate document relevance (keyword-based compliance detection)

Split text into chunks using RecursiveCharacterTextSplitter

Generate embeddings using:

Alibaba-NLP/gte-base-en-v1.5


Store vectors in ChromaDB (persistent storage)

2️⃣ RAG Question Answering Flow

User asks a question

Retrieve top 5 relevant chunks from vector store

Inject into structured legal-compliance prompt

Query LLaMA 3.1 via Groq API

Return professional, analytical response

🏗 Project Structure
Legal-Compliance-RAG-Assistant/
│
├── main.py                 # Streamlit frontend
├── project1.py             # Core RAG + processing logic
├── vectorstore/            # Chroma persistent storage
├── .env                    # Environment variables (not committed)
├── pyproject.toml          # Dependency definitions
├── uv.lock                 # Locked dependency versions
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/abhijithj12/Legal-Compliance-RAG-Assistant.git
cd Legal-Compliance-RAG-Assistant

2️⃣ Install Dependencies (Using uv)

This project uses uv for dependency management.

uv sync


No requirements.txt is required.

3️⃣ Setup Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here


Get your API key from:
https://console.groq.com/

4️⃣ Run the Application
streamlit run main.py


App will open at:

http://localhost:8501

🛡 Compliance Validation Logic

Before storing documents, the system checks for at least 3 legal/compliance-related keywords, such as:

policy

compliance

regulation

clause

audit

liability

governance

data protection

breach

If the document is not classified as a compliance document, it is rejected.

💬 Question Answering Rules

The system:

✅ Answers only if related to:

Policies

Regulations

Legal clauses

Compliance requirements

Risk management

Governance

❌ If unrelated:

"This system only answers legal and compliance related questions."

❓ If answer not found in context:

"I don't know."

🧩 Tech Stack

LLM: Groq (LLaMA 3.1-8B-Instant)

Embeddings: HuggingFace gte-base-en-v1.5

Vector Database: ChromaDB

Framework: LangChain

Frontend: Streamlit

PDF Parsing: PyPDFLoader

Environment Management: uv

📌 Example Use Cases

Corporate compliance auditing

Regulatory document review

Policy interpretation

Legal clause explanation

Risk & governance analysis

Data protection compliance review

⚠️ Limitations

English documents only

Requires compliance-related PDFs

Answers strictly from uploaded documents

No internet access or external knowledge

🔮 Future Improvements

ML-based document classification

Multi-language support

Authentication & user sessions

Cloud deployment (AWS / GCP / Azure)

Conversation memory

Admin dashboard

🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

📜 License

This project is licensed under the MIT License.

👤 Author

Abhijith J
AI / GenAI Enthusiast
GitHub: https://github.com/abhijithj12