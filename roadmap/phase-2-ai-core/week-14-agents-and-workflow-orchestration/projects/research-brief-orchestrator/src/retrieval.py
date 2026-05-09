"""Deterministic local retrieval for the Week 14 lab."""

from __future__ import annotations

from .data_access import DocumentStore


def _normalize(text: str) -> str:
    return " ".join(text.lower().split())


def search_documents(store: DocumentStore, query: str, topics: list[str], limit: int = 3) -> list[dict[str, object]]:
    query_terms = set(_normalize(query).split())
    ranked: list[tuple[int, dict[str, object]]] = []

    for document in store.all_documents():
        doc_topic = str(document["topic"])
        if topics and "general" not in topics and doc_topic not in topics:
            continue

        haystack = _normalize(
            f"{document['title']} {document['topic']} {document['summary']} {document['details']}"
        )
        score = sum(1 for term in query_terms if term in haystack)
        if score > 0:
            ranked.append((score, document))

    ranked.sort(key=lambda item: item[0], reverse=True)
    return [document for _, document in ranked[:limit]]
