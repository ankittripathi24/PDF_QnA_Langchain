import streamlit as st
from document_qa import DocumentQA
import tempfile
import os

st.set_page_config(page_title="Document Q&A", page_icon="📚")

# Initialize DocumentQA
@st.cache_resource
def get_qa_system():
    return DocumentQA()

qa_system = get_qa_system()

st.title("📚 Document Q&A System")
st.write("Upload a PDF document and ask questions about its content!")

# File upload
uploaded_file = st.file_uploader("Upload a PDF document", type=['pdf'])

if uploaded_file:
    # Create a temporary file to store the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    # Process the document
    with st.spinner("Processing document..."):
        num_chunks = qa_system.load_document(tmp_file_path)
        st.success(f"Document processed! Split into {num_chunks} chunks.")
    
    # Remove temporary file
    os.unlink(tmp_file_path)

    # Question input
    question = st.text_input("Ask a question about the document:")
    
    if question:
        with st.spinner("Thinking..."):
            response = qa_system.get_answer(question)
            
            st.write("### Answer:")
            st.write(response['answer'])
            
            st.write("### Sources:")
            for source in response['sources']:
                st.write(f"- {source}")

else:
    st.info("Please upload a PDF document to get started!")
