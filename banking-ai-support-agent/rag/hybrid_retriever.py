from rag.retriever import retrieve_context


def keyword_search(query):

    if "GST" in query:
        return "GST registration required"

    return ""


def hybrid_search(query):

    semantic_result = retrieve_context(query)

    keyword_result = keyword_search(query)

    return f"""
    Semantic Result:
    {semantic_result}

    Keyword Result:
    {keyword_result}
    """