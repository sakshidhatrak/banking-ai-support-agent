def create_plan(query):

    query = query.lower()

    steps = []

    if "loan" in query:
        steps.append("Retrieve loan policies")

    if "emi" in query:
        steps.append("Calculate EMI")

    if "branch" in query:
        steps.append("Locate nearest branch")

    if not steps:
        steps.append("General banking response")

    return steps