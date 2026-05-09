"""Simple routing helpers for turning a query into one or more topics."""

from __future__ import annotations


TOPIC_KEYWORDS = {
    "refund": ["refund", "billing", "chargeback", "exception"],
    "travel": ["travel", "reimbursement", "receipt", "lodging"],
    "security": ["security", "password", "mfa", "incident"],
    "equipment": ["equipment", "laptop", "device", "replacement"],
}


def classify_topics(query: str) -> list[str]:
    query_lower = query.lower()
    topics: list[str] = []

    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword in query_lower for keyword in keywords):
            topics.append(topic)

    if not topics:
        topics.append("general")

    return topics


def build_retrieval_query(query: str, topics: list[str], retry_count: int = 0) -> str:
    if retry_count == 0:
        return query

    if topics and topics[0] != "general":
        return f"{query} {' '.join(topics)} policy summary"

    return f"{query} internal policy summary"
