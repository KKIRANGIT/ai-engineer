from src.models import RetrievedChunk


def build_context(retrieved_chunks: list[RetrievedChunk]) -> str:
    sections = []
    for item in retrieved_chunks:
        sections.append(
            f"[{item.chunk.chunk_id}] {item.chunk.title} ({item.chunk.section})\n{item.chunk.text}"
        )
    return "\n\n".join(sections)
