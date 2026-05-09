"""A lightweight ReAct-style loop for the Week 14 project."""

from __future__ import annotations

from .data_access import DocumentStore
from .models import WorkflowState
from .quality import draft_brief, should_request_review
from .retrieval import search_documents
from .topic_router import classify_topics


def run_agent_loop(query: str, store: DocumentStore) -> WorkflowState:
    state = WorkflowState(query=query)
    state.topics = classify_topics(query)
    state.add_step("classify_topics", {"topics": state.topics})

    remaining_topics = [topic for topic in state.topics if topic != "general"]
    searched_topics: set[str] = set()

    if not remaining_topics:
        remaining_topics = ["general"]

    while remaining_topics and len(searched_topics) < 4:
        next_topic = remaining_topics.pop(0)
        if next_topic in searched_topics:
            continue

        searched_topics.add(next_topic)
        search_query = f"{query} {next_topic}"
        state.add_step("plan_next_action", {"chosen_topic": next_topic, "search_query": search_query})

        docs = search_documents(store, search_query, [next_topic] if next_topic != "general" else ["general"])
        state.add_step("search_topic", {"topic": next_topic, "doc_ids": [doc["doc_id"] for doc in docs]})

        for doc in docs:
            if doc not in state.retrieved_docs:
                state.retrieved_docs.append(doc)

    state.brief = draft_brief(query, state.topics, state.retrieved_docs)
    state.needs_human_review = should_request_review(state.topics, state.retrieved_docs)
    state.add_step("synthesize_brief", {"needs_human_review": state.needs_human_review})
    return state
