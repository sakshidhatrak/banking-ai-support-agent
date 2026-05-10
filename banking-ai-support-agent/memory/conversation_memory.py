conversation_history = []


def save_message(role, message):

    conversation_history.append({
        "role": role,
        "message": message
    })


def get_history(limit=5):

    return conversation_history[-limit:]