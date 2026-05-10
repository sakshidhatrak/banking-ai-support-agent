import json
import os

# =========================================
# ABSOLUTE FEEDBACK FILE PATH
# =========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

FEEDBACK_FILE = os.path.join(
    BASE_DIR,
    "feedback_data.json"
)

# =========================================
# SAVE FEEDBACK
# =========================================

def save_feedback(
    user_query,
    response,
    feedback
):

    data = []

    # =====================================
    # LOAD EXISTING FEEDBACK
    # =====================================

    if os.path.exists(FEEDBACK_FILE):

        try:

            with open(
                FEEDBACK_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

        except Exception:

            data = []

    # =====================================
    # APPEND NEW FEEDBACK
    # =====================================

    data.append({
        "query": user_query,
        "response": response,
        "feedback": feedback
    })

    # =====================================
    # SAVE UPDATED FEEDBACK
    # =====================================

    with open(
        FEEDBACK_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

# =========================================
# LOAD FEEDBACK
# =========================================

def load_feedback():

    if not os.path.exists(
        FEEDBACK_FILE
    ):

        return []

    try:

        with open(
            FEEDBACK_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return []