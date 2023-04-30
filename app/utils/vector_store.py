import os
import re
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(documents, api_key):
    """
    Create a vector store using OpenAI embeddings and FAISS and return it.

    :param documents: A list of Document objects to add to the vector store.
    :param api_key: Your OpenAI API key.
    :return: The created vector store.
    """
    embeddings = OpenAIEmbeddings(api_key=api_key)
    vector_store = FAISS()
    for document in documents:
        document.add_embeddings(embeddings)
        vector_store.add_document(document)
    vector_store.train_index()
    return vector_store

def query_vector_store(vector_store, question, k=5):
    """
    Query the vector store with the specified question and return the top k results.

    :param vector_store: The vector store to query.
    :param question: The question to query the vector store with.
    :param k: The number of top results to return.
    :return: A list of (score, Document) tuples representing the top results.
    """
    query_doc = Document(page_content=question)
    query_doc.add_embeddings(embeddings)
    results = vector_store.query(query_doc, k=k)
    return [(score, result.metadata["filename"]) for score, result in results]
