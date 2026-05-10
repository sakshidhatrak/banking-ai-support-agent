conversation_memory = []


def save_short_term_memory(role, message):

    conversation_memory.append({
        "role": role,
        "message": message
    })


def get_recent_memory(limit=5):

    return conversation_memory[-limit:]