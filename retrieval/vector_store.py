# from embeddings.embedder import get_embedding
# from retrieval.pinecone_client import index
# import uuid

# def store_chunks(chunks, filename, page_number, document_id: str):

#     vectors = []

#     for i, chunk in enumerate(chunks):

#         vector = get_embedding(chunk)
#         print(f"Vector length: {len(vector)}")
#         vectors.append({
#             "id": str(uuid.uuid4()),
#             "values": vector,
#             "metadata": {
#                 "text": chunk,
#                 "doc_id": document_id,
#                 "chunk_id": i,
#                 "source": filename,
#                 "page": page_number
#             }
#         })

#     print("Uploading vectors to Pinecone...")
#     index.upsert(vectors=vectors)
#     print("Upload complete")
#     return len(vectors)\

"""
Stores embedded chunks into Pinecone.
"""

import uuid
from embeddings.embedder import get_embedding
from retrieval.pinecone_client import index
from app.logger import get_logger

logger = get_logger(__name__)


def store_chunks(chunks: list[str], filename: str, page_number: int, document_id: str) -> int:
    if not chunks:
        logger.warning(f"store_chunks called with no chunks (doc={document_id}, page={page_number})")
        return 0

    vectors = []
    for i, chunk in enumerate(chunks):
        try:
            vector = get_embedding(chunk)
        except Exception as e:
            logger.warning(f"Skipping chunk {i} on page {page_number} of {filename} — embedding failed: {e}")
            continue

        vectors.append({
            "id": str(uuid.uuid4()),
            "values": vector,
            "metadata": {
                "text": chunk,
                "doc_id": document_id,
                "chunk_id": i,
                "source": filename,
                "page": page_number
            }
        })

    if not vectors:
        logger.error(f"No chunks could be embedded for {filename} page {page_number}")
        return 0

    try:
        index.upsert(vectors=vectors)
    except Exception as e:
        logger.error(f"Pinecone upsert failed for {filename} page {page_number}: {e}")
        raise

    logger.info(f"Stored {len(vectors)} chunks from {filename} (page {page_number}, doc_id={document_id})")
    return len(vectors)