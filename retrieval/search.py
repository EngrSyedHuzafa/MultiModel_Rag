# from embeddings.embedder import get_embedding
# from retrieval.pinecone_client import index

# def search_chunks(query: str, top_k: int = 1):

#     # 1. Convert query → vector
#     query_vector = get_embedding(query)

#     # 2. Search Pinecone
#     results = index.query(
#         vector=query_vector,
#         top_k=top_k,
#         include_metadata=True
#     )

#     # 3. Extract chunks with metadata
#     chunks = []

#     for match in results["matches"]:

#         chunk_data = {
#             "text": match["metadata"]["text"],
#             "page": match["metadata"]["page"],
#             "source": match["metadata"]["source"]
#         }

#         chunks.append(chunk_data)

#     return chunks

"""
Semantic search over stored chunks.
"""

from embeddings.embedder import get_embedding
from retrieval.pinecone_client import index
from app.config import settings
from app.logger import get_logger

logger = get_logger(__name__)


def search_chunks(query: str, top_k: int = None) -> list[dict]:
    if not query or not query.strip():
        logger.warning("search_chunks called with empty query")
        return []

    top_k = top_k or settings.SEARCH_TOP_K

    try:
        query_vector = get_embedding(query)
    except Exception as e:
        logger.error(f"Failed to embed query '{query}': {e}")
        raise

    try:
        results = index.query(vector=query_vector, top_k=top_k, include_metadata=True)
    except Exception as e:
        logger.error(f"Pinecone query failed: {e}")
        raise

    chunks = []
    for match in results.get("matches", []):
        metadata = match.get("metadata", {})
        chunks.append({
            "text": metadata.get("text", ""),
            "page": metadata.get("page"),
            "source": metadata.get("source", "unknown"),
            "score": match.get("score")
        })

    logger.info(f"Query '{query}' returned {len(chunks)} chunks (top_k={top_k})")
    return chunks