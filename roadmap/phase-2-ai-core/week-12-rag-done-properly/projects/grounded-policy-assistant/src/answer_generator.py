from src.models import GroundedAnswer, RetrievedChunk


def generate_grounded_answer(question: str, rewritten_query: str, retrieved_chunks: list[RetrievedChunk]) -> GroundedAnswer:
    if not retrieved_chunks:
        return GroundedAnswer(
            answer_text="I could not find supporting policy evidence for this question.",
            citations=[],
            rewritten_query=rewritten_query,
            retrieved_chunks=[],
        )

    top_chunk = retrieved_chunks[0].chunk
    answer_text = (
        f"Based on {top_chunk.title}, {top_chunk.text} "
        "This answer is grounded in the retrieved policy material shown below."
    )

    citations = [
        {
            "chunk_id": item.chunk.chunk_id,
            "document_id": item.chunk.document_id,
            "title": item.chunk.title,
            "text": item.chunk.text,
        }
        for item in retrieved_chunks
    ]

    return GroundedAnswer(
        answer_text=answer_text,
        citations=citations,
        rewritten_query=rewritten_query,
        retrieved_chunks=[
            {
                "chunk_id": item.chunk.chunk_id,
                "document_id": item.chunk.document_id,
                "title": item.chunk.title,
                "score": item.score,
            }
            for item in retrieved_chunks
        ],
    )
