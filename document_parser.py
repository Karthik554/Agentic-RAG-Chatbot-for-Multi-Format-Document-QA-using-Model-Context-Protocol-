from langchain_community.document_loaders import (
    PyPDFLoader, TextLoader, Docx2txtLoader, CSVLoader, UnstructuredFileLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
from typing import List

def load_and_split_documents(file_paths: List[str]):
    documents = []
    for path in file_paths:
        ext = Path(path).suffix.lower()
        if ext == ".pdf":
            loader = PyPDFLoader(path)
        elif ext == ".txt":
            loader = TextLoader(path)
        elif ext == ".csv":
            loader = CSVLoader(path)
        elif ext == ".docx":
            loader = Docx2txtLoader(path)
        else:
            loader = UnstructuredFileLoader(path)
        docs = loader.load()
        documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    return splitter.split_documents(documents)
