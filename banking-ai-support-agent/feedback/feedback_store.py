import json
import os


FEEDBACK_FILE = "feedback/feedback_data.json"


def save_feedback(user_query, response, feedback):

    data = []

    if os.path.exists(FEEDBACK_FILE):

        with open(FEEDBACK_FILE, "r") as file:

            try:
                data = json.load(file)
            except:
                data = []

    data.append({
        "query": user_query,
        "response": response,
        "feedback": feedback
    })

    with open(FEEDBACK_FILE, "w") as file:

        json.dump(data, file, indent=4)


def load_feedback():

    if not os.path.exists(FEEDBACK_FILE):
        return []

    with open(FEEDBACK_FILE, "r") as file:

        try:
            return json.load(file)
        except:
            return []