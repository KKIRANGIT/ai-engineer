from src.retrieval import SemanticSearchPlayground
from src.store import load_evaluation_queries


def evaluate_mode(mode: str) -> list[dict]:
    playground = SemanticSearchPlayground()
    outcomes = []

    for case in load_evaluation_queries():
        results = playground.search(case["query"], mode=mode, top_k=1)
        top_document_id = results[0].chunk.document_id if results else None
        outcomes.append(
            {
                "query": case["query"],
                "expected_document_id": case["expected_document_id"],
                "retrieved_document_id": top_document_id,
                "passed": top_document_id == case["expected_document_id"],
            }
        )

    return outcomes
