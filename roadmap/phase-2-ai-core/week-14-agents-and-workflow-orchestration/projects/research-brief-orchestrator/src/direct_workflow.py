"""Deterministic workflow implementation for the Week 14 project."""

from __future__ import annotations

from .data_access import DocumentStore
from .models import WorkflowState
from .quality import draft_brief, should_request_review
from .retrieval import search_documents
from .topic_router import build_retrieval_query, classify_topics


def run_direct_workflow(query: str, store: DocumentStore) -> WorkflowState:
    state = WorkflowState(query=query)

    state.topics = classify_topics(query)
    state.add_step("classify_topics", {"topics": state.topics})

    state.retrieval_query = build_retrieval_query(query, state.topics)
    state.retrieved_docs = search_documents(store, state.retrieval_query, state.topics)
    state.add_step(
        "retrieve_docs",
        {
            "retrieval_query": state.retrieval_query,
            "doc_ids": [doc["doc_id"] for doc in state.retrieved_docs],
        },
    )

    state.brief = draft_brief(query, state.topics, state.retrieved_docs)
    state.add_step("draft_brief", {"brief_preview": state.brief.splitlines()[:4]})

    state.needs_human_review = should_request_review(state.topics, state.retrieved_docs)
    state.add_step("quality_gate", {"needs_human_review": state.needs_human_review})

    return state
