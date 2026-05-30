from embeddings.embedder import get_embedding
from retrieval.pinecone_client import index
import uuid

def store_chunks(chunks, document_id: str):

    vectors = []

    for i, chunk in enumerate(chunks):

        vector = get_embedding(chunk)
        print(f"Vector length: {len(vector)}")
        vectors.append({
            "id": str(uuid.uuid4()),
            "values": vector,
            "metadata": {
                "text": chunk,
                "doc_id": document_id,
                "chunk_id": i
            }
        })

    index.upsert(vectors=vectors)

    return len(vectors)