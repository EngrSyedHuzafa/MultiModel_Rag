from embeddings.embedder import get_embedding
from retrieval.pinecone_client import index

def search_chunks(query: str, top_k: int = 5):

    # 1. Convert query → vector
    query_vector = get_embedding(query)

    # 2. Search Pinecone
    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    # 3. Extract text chunks
    chunks = []

    for match in results["matches"]:
        chunks.append(match["metadata"]["text"])

    return chunks