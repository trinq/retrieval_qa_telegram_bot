import os
import re
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load documents from the specified directory and split them into chunks
doc_directory = "/path/to/documents"
chunk_size = 1000
documents = load_documents(doc_directory, chunk_size)
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=20)
split_docs = text_splitter.split_documents(documents)

# Initialize the OpenAI embeddings and FAISS vector store
api_key = "INSERT_YOUR_OPENAI_API_KEY_HERE"
embeddings = OpenAIEmbeddings(api_key=api_key)
vector_store = FAISS()

# Add each chunk of text to a Document object and add it to the vector store
for doc in split_docs:
    doc.add_embeddings(embeddings)
    vector_store.add_document(doc)

# Train the FAISS index
vector_store.train_index()

# Verify the content of the vector store with a sample query
query = "How do I create a virtual environment in Python?"
query_doc = Document(page_content=query)
query_doc.add_embeddings(embeddings)
results = vector_store.query(query_doc, k=5)
for result in results:
    print(result.metadata["source"])
