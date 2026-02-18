import streamlit as st
from project1 import process_pdfs, question_answer

st.title("📄 Compliance Intelligence Assistant")

uploaded_files = st.sidebar.file_uploader(
    "Upload your documents",
    type=["pdf"],
    accept_multiple_files=True
)

if st.sidebar.button("Process Documents"):
    if uploaded_files:
        process_pdfs(uploaded_files)
        st.success("Documents processed successfully!")
    else:
        st.warning("Please upload at least one PDF.")

query = st.text_input("Ask a question about your documents:")

if query:
    answer = question_answer(query)
    st.write(answer)
