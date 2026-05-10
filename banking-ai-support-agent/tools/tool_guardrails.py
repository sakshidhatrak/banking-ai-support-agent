UNSAFE_TOOL_KEYWORDS = [
    "transfer money",
    "approve loan",
    "reset password",
    "change mobile number"
]


def is_unsafe_tool_request(query):

    query = query.lower()

    return any(
        keyword in query
        for keyword in UNSAFE_TOOL_KEYWORDS
    )