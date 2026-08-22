chat_history = []

def add_message(role, content):
    chat_history.append({
        "role": role,
        "content": content
    })

def get_history(limit=6):
    return chat_history[-limit:]