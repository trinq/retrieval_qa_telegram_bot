import os
import re
import logging
from fastapi import APIRouter, HTTPException
from app.utils.document_loading import load_documents
from app.utils.vector_store import create_vector_store, query_vector_store
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

DOCUMENT_DIRECTORY = os.getenv("DOCUMENT_DIRECTORY")
API_KEY = os.getenv("OPENAI_API_KEY")

@api_router.post("/create_vector_store")
async def create_vector_store():
    """
    Create a vector store from the documents in the specified directory and return its ID.
    """
    if not os.path.isdir(DOCUMENT_DIRECTORY):
        raise HTTPException(status_code=400, detail="Directory not found.")
    documents = load_documents(DOCUMENT_DIRECTORY)
    vector_store = create_vector_store(documents, API_KEY)
    return {"id": vector_store.id}

@api_router.get("/query_vector_store")
async def query_vector_store(store_id: str, question: str):
    """
    Query the vector store with the specified question and return the top results.
    """
    vector_store = VectorStore.get(store_id)
    if not vector_store:
        raise HTTPException(status_code=400, detail="Invalid vector store ID.")
    results = query_vector_store(vector_store, question)
    return [{"score": score, "text": result.text} for score, result in results]
