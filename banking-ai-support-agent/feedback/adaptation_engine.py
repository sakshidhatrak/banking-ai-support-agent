from feedback.feedback_store import load_feedback


def get_adaptation_rules():

    feedback_data = load_feedback()

    rules = {
        "prefer_short_answers": False,
        "prefer_detailed_answers": False
    }

    short_count = 0
    detailed_count = 0

    for item in feedback_data:

        feedback = item["feedback"].lower()

        if "too long" in feedback:

            short_count += 1

        if "more detail" in feedback:

            detailed_count += 1

    if short_count > detailed_count:

        rules["prefer_short_answers"] = True

    elif detailed_count > short_count:

        rules["prefer_detailed_answers"] = True

    return rules