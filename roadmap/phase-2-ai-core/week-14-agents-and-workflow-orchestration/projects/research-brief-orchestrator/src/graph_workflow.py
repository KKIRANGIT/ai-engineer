"""Graph-style orchestration for the Week 14 project."""

from __future__ import annotations

from .data_access import DocumentStore
from .graph_runtime import StateGraph
from .models import WorkflowState
from .quality import draft_brief, should_request_review
from .retrieval import search_documents
from .topic_router import build_retrieval_query, classify_topics


def build_graph(store: DocumentStore) -> StateGraph:
    graph = StateGraph()

    def classify(state: WorkflowState) -> WorkflowState:
        state.topics = classify_topics(state.query)
        state.add_step("classify_topics", {"topics": state.topics})
        return state

    def retrieve(state: WorkflowState) -> WorkflowState:
        state.retrieval_query = build_retrieval_query(state.query, state.topics, state.retry_count)
        state.retrieved_docs = search_documents(store, state.retrieval_query, state.topics)
        state.add_step(
            "retrieve_docs",
            {
                "retry_count": state.retry_count,
                "retrieval_query": state.retrieval_query,
                "doc_ids": [doc["doc_id"] for doc in state.retrieved_docs],
            },
        )
        return state

    def assess(state: WorkflowState) -> WorkflowState:
        state.needs_human_review = should_request_review(state.topics, state.retrieved_docs)
        state.add_step("assess_evidence", {"needs_human_review": state.needs_human_review})
        return state

    def refine_query(state: WorkflowState) -> WorkflowState:
        state.retry_count += 1
        state.add_step("refine_query", {"retry_count": state.retry_count})
        return state

    def draft(state: WorkflowState) -> WorkflowState:
        state.brief = draft_brief(state.query, state.topics, state.retrieved_docs)
        state.add_step("draft_brief", {"brief_preview": state.brief.splitlines()[:4]})
        return state

    def review(state: WorkflowState) -> WorkflowState:
        state.add_step("review_gate", {"needs_human_review": state.needs_human_review})
        return state

    def finalize(state: WorkflowState) -> WorkflowState:
        state.add_step("finalize", {"status": "completed"})
        return state

    graph.add_node("classify", classify)
    graph.add_node("retrieve", retrieve)
    graph.add_node("assess", assess)
    graph.add_node("refine_query", refine_query)
    graph.add_node("draft", draft)
    graph.add_node("review", review)
    graph.add_node("finalize", finalize)

    graph.add_router("classify", lambda state: "retrieve")
    graph.add_router("retrieve", lambda state: "assess")
    graph.add_router(
        "assess",
        lambda state: "refine_query" if state.needs_human_review and state.retry_count < 1 else "draft",
    )
    graph.add_router("refine_query", lambda state: "retrieve")
    graph.add_router("draft", lambda state: "review")
    graph.add_router("review", lambda state: "finalize")
    graph.add_router("finalize", lambda state: "END")
    graph.set_start("classify")

    return graph


def run_graph_workflow(query: str, store: DocumentStore) -> WorkflowState:
    state = WorkflowState(query=query)
    graph = build_graph(store)
    return graph.run(state)
