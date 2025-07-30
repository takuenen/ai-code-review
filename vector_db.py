from langchain.vectorstores import Chroma
from langchain.embeddings import AzureOpenAIEmbeddings
import os

def get_vectorstore(persist_directory="chroma_db"):
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_EMBEDDING"),
        chunk_size=1000
    )
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return vectordb

def add_code_to_vectorstore(vectordb, code_snippet, metadata=None):
    vectordb.add_texts([code_snippet], metadatas=[metadata or {}])

def query_similar_code(vectordb, query, top_k=5):
    return vectordb.similarity_search(query, k=top_k)
