from src.rag_pipeline import GroundedPolicyAssistant
from src.store import load_evaluation_questions


def run_evaluation() -> list[dict]:
    assistant = GroundedPolicyAssistant()
    outcomes = []

    for item in load_evaluation_questions():
        answer = assistant.answer(item["question"])
        top_document_id = answer.citations[0]["document_id"] if answer.citations else None
        outcomes.append(
            {
                "question": item["question"],
                "expected_document_id": item["expected_document_id"],
                "retrieved_document_id": top_document_id,
                "passed": top_document_id == item["expected_document_id"],
            }
        )

    return outcomes
