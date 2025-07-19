from langchain.vectorstores import Chroma
from utils.embedding_handler import get_google_embeddings

def create_vectorstore(documents):
    embedding = get_google_embeddings()
    return Chroma.from_documents(documents, embedding=embedding, persist_directory="chroma_store")

def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
