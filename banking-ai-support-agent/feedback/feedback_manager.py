from feedback.feedback_store import save_feedback
from feedback.adaptation_engine import get_adaptation_rules


def process_feedback(user_query, response, feedback):

    save_feedback(
        user_query,
        response,
        feedback
    )

    updated_rules = get_adaptation_rules()

    return updated_rules