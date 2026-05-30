from langchain_text_splitters import RecursiveCharacterTextSplitter
# to test the text chunking functionality, we will import the store_chunks function from the vector_store module and call it within the chunk_text function. This will allow us to store the generated chunks in the vector store and verify that they are being stored correctly.
# from retrieval.vector_store import store_chunks
# we will also import the search_chunks function from the search module to test the search functionality after chunking and storing the chunks.
# from retrieval.search import search_chunks
def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)
    #count = store_chunks(chunks, document_id="doc1")
    #print("Stored chunks:", count)
    return chunks


#The vbelow code is for testing the search functionality after chunking and storing the chunks. We will use a sample query to search for relevant chunks and print the results.
# query = "what is business model?"

# results = search_chunks(query)

# for i, r in enumerate(results):
#     print(f"\nChunk {i}:\n{r}\n")