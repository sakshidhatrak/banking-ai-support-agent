import os


MEMORY_FILE = "memory/conversation_history.json"


def reset_memory():

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w") as file:

            file.write("[]")

    print("Memory reset successfully.")