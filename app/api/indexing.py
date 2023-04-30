import os
import re
from app.utils.document import Document
from app.utils.document_loading import load_documents
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def load_and_index_documents(doc_directory, chunk_size, api_key):
    # Load documents from the specified directory and split them into chunks
    documents = load_documents(doc_directory, chunk_size)
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=20)
    split_docs = text_splitter.split_documents(documents)

    # Initialize the OpenAI embeddings and FAISS vector store
    embeddings = OpenAIEmbeddings(api_key=api_key)
    vector_store = FAISS()

    # Add each chunk of text to a Document object and add it to the vector store
    for doc in split_docs:
        doc.add_embeddings(embeddings)
        vector_store.add_document(doc)

    # Train the FAISS index
    vector_store.train_index()

    return vector_store
