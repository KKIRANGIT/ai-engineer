import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9_]+", text.lower())


def keyword_score(query: str, text: str) -> float:
    query_terms = tokenize(query)
    text_terms = set(tokenize(text))
    if not query_terms:
        return 0.0

    matches = sum(1 for term in query_terms if term in text_terms)
    return matches / len(query_terms)
