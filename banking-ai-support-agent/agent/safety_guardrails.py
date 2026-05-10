BLOCKED_KEYWORDS = [
    "transfer money",
    "send money",
    "approve loan",
    "legal advice",
    "change account",
    "bypass kyc"
]


def is_unsafe_query(user_input):
    user_input = user_input.lower()

    for keyword in BLOCKED_KEYWORDS:
        if keyword in user_input:
            return True

    return False