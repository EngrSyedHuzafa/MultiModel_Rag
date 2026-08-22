from fastapi import APIRouter
from llm.rag_pipeline import ask_rag

router = APIRouter()

@router.get("/chat")
def chat(query: str):

    answer, chunks = ask_rag(query)

    return {
        "query": query,
        "answer": answer,
        "sources": chunks
    }