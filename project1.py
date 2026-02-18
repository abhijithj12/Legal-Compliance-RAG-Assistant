from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_chroma import Chroma 
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from uuid import uuid4
from langchain_core.prompts import ChatPromptTemplate
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
import tempfile

load_dotenv()

ef=HuggingFaceEmbeddings(model="Alibaba-NLP/gte-base-en-v1.5",model_kwargs={'trust_remote_code':True})

llm=None
vector_store=None

def initialization():
    global llm
    global vector_store
    if llm is None or vector_store is None:
        llm=ChatGroq(model_name="llama-3.1-8b-instant",temperature=0.4,max_tokens=800)
        vector_store=Chroma(collection_name="legal_compliance_document_store",embedding_function=ef,persist_directory=Path("vectorstore"))
    print("Initialization Completed")


def is_compliance_document(text: str) -> bool:
    keywords = [
        "policy", "compliance", "regulation", "act",
        "clause", "section", "liability", "penalty",
        "governance", "audit", "risk", "obligation",
        "confidentiality", "data protection", "breach"
    ]

    text_lower = text.lower()
    match_count = sum(1 for word in keywords if word in text_lower)

    # Require at least 3 keyword matches
    return match_count >= 3



def process_pdfs(uploaded_files):
    global vector_store

    initialization()
    
    # If vector store exists, delete old collection
    if vector_store is not None:
        vector_store.delete_collection()

    
    vector_store=Chroma(collection_name="legal_compliance_document_store",embedding_function=ef,persist_directory=Path("vectorstore"))
    
   
    all_docs = []

    for uploaded_file in uploaded_files:
        try: # Save temporarily 
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name

                loader = PyPDFLoader(tmp_path)
                data = loader.load()

                all_docs.extend(data)
        except Exception as e:
            print("Error loading PDF:", e)
    
    print("PDFs Loaded")


    combined_text = " ".join(doc.page_content for doc in all_docs)

    if not is_compliance_document(combined_text):
        raise ValueError(
            "Uploaded document is not a legal/compliance document.")
       
    
    splitter=RecursiveCharacterTextSplitter(separators=["\n\n","\n","."," "],chunk_size=1000,chunk_overlap=200)
    chunk_docs=splitter.split_documents(all_docs)
    print("Docs Created")
    
    ids=[str(uuid4()) for i in chunk_docs]
    vector_store.add_documents(chunk_docs,ids=ids)
    print("Stored in vector_store")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def rag():
    """
    Create a RAG chain for answering questions.

    """
    if not llm or not vector_store:
        raise RuntimeError("Please run initialization() first!")
    

    prompt_template = """
    You are a Legal and Compliance AI Assistant.

    You must answer ONLY if the question relates to:
        - Policies
        - Regulations
        - Legal clauses
        - Compliance requirements
        - Risk management
        - Governance

    If the question is unrelated to legal or compliance topics,
    respond strictly with:
        "This system only answers legal and compliance related questions."

    Use ONLY the provided context.
    If answer not in context, say "I don't know."
    No preamble.

    Context:{context}

    Question:{question}

    Answer in a friendly, professional, and analytical tone:
    """

    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    prompt = ChatPromptTemplate.from_template(prompt_template)
    rag_chain = (
        {
            "context": itemgetter("question") | retriever | format_docs,
            "question": itemgetter("question")
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain




def question_answer(query):
    chain=rag()
    print("Asking:",query)
    response=chain.invoke({"question":query})
    return response




