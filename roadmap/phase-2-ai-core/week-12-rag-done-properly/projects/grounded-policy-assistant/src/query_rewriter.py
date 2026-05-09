def rewrite_query(question: str) -> str:
    normalized = question.lower()

    replacements = {
        "charged twice": "duplicate charge refund billing dispute",
        "login failures": "login failure password reset account locked sign in",
        "feature request timelines": "feature request delivery date product feedback policy",
        "keeps crashing": "repeated crash workflow incident escalation logs reproduction steps",
    }

    for source_text, replacement in replacements.items():
        if source_text in normalized:
            return replacement

    return normalized.strip()
