from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DocumentQA:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.vector_store = None

    def load_document(self, file_path):
        """Load and process a PDF document."""
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        texts = self.text_splitter.split_documents(documents)
        
        # Create vector store
        self.vector_store = FAISS.from_documents(
            documents=texts,
            embedding=self.embeddings
        )
        return len(texts)

    def get_answer(self, question):
        """Get answer for a question using the loaded documents."""
        if not self.vector_store:
            return "Please load a document first."

        llm = OpenAI(temperature=0)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(),
            return_source_documents=True
        )

        response = qa_chain({"query": question})
        
        # Format the response with source information
        answer = response['result']
        sources = [f"Document: {doc.metadata.get('source', 'Unknown')}, Page: {doc.metadata.get('page', 'Unknown')}"
                  for doc in response['source_documents']]
        
        return {
            'answer': answer,
            'sources': sources
        }
