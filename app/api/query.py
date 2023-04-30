from fastapi import APIRouter, HTTPException
from app.utils.vector_store import query_vector_store

router = APIRouter()

@api_router.get("/query_vector_store")
async def query_vector_store(store_id: str, question: str, k: int = 5):
    """
    Query the vector store with the specified question and return the top results.

    :param store_id: The ID of the vector store to query.
    :param question: The question to query the vector store with.
    :param k: The number of top results to return.
    :return: A list of (score, filename) tuples representing the top results.
    """
    if not vector_store.exists(store_id):
        raise HTTPException(status_code=400, detail="Invalid vector store ID.")
    vector_store = vector_store.get(store_id)
    results = query_vector_store(vector_store, question, k=k)
    return results
