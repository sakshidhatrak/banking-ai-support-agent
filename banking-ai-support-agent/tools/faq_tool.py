FAQS = {
    "kyc": "KYC requires identity proof and address proof.",
    "blocked card": "Blocked cards should be reported immediately.",
    "credit card": "Credit cards require income verification."
}


def search_faq(query):

    query = query.lower()

    for key, value in FAQS.items():

        if key in query:
            return value

    return "No FAQ information found."