from src.models import GroundedAnswer


def build_debug_view(answer: GroundedAnswer) -> dict:
    return {
        "rewritten_query": answer.rewritten_query,
        "retrieved_chunks": answer.retrieved_chunks,
        "citations": answer.citations,
    }
