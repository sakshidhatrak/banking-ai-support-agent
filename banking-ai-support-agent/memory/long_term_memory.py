import json
import os


MEMORY_FILE = "memory/conversation_history.json"


def save_long_term_memory(role, message):

    memory = []

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as file:

            try:
                memory = json.load(file)
            except:
                memory = []

    memory.append({
        "role": role,
        "message": message
    })

    with open(MEMORY_FILE, "w") as file:

        json.dump(memory, file, indent=4)


def load_long_term_memory(limit=10):

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:

        try:
            memory = json.load(file)
        except:
            return []

    return memory[-limit:]