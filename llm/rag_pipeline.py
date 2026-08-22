from retrieval.search import search_chunks
from llm.gemini_client import generate_response
from llm.memory import get_history, add_message

def ask_rag(query: str):

    # 1. Save user message
    add_message("user", query)

    # 2. Retrieve chunks
    chunks = search_chunks(query)

    # 3. Get chat history
    history = get_history()

    # 4. Build conversation context
    conversation = ""

    for msg in history:
        conversation += f"{msg['role']}: {msg['content']}\n"

    # 5. Generate answer with memory
    answer = generate_response(query, chunks, conversation)

    # 6. Save assistant response
    add_message("assistant", answer)

    return answer, chunks

