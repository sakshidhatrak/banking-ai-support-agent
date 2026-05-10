import os


def check_system_health():

    checks = {
        "logs_folder": os.path.exists("logs"),
        "memory_folder": os.path.exists("memory"),
        "feedback_folder": os.path.exists("feedback"),
        "chroma_db": os.path.exists("chroma_db")
    }

    return checks


if __name__ == "__main__":

    results = check_system_health()

    print("\nSystem Health Check:\n")

    for key, value in results.items():

        print(f"{key}: {value}")