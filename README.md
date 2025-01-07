# Document Q&A System using LangChain

This project is a Document Question-Answering system built using LangChain. It allows users to upload documents and ask questions about their content.

## Features
- Upload PDF documents
- Process and analyze document content
- Ask questions about the documents
- Get answers with source citations

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

## Project Structure
- `app.py`: Main Streamlit application
- `document_qa.py`: Core Q&A functionality
- `requirements.txt`: Project dependencies

## Learning Resources
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [Streamlit Documentation](https://docs.streamlit.io)
