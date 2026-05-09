from src.models import RetrievedChunk
from src.query_rewriter import rewrite_query
from src.store import load_policy_documents
from src.chunking import chunk_documents


def tokenize(text: str) -> list[str]:
    return [token for token in text.lower().replace(",", " ").replace(".", " ").split() if token]


class RetrievalBackend:
    def __init__(self) -> None:
        self.documents = load_policy_documents()
        self.chunks = chunk_documents(self.documents)

    def retrieve(self, question: str, top_k: int) -> tuple[str, list[RetrievedChunk]]:
        rewritten_query = rewrite_query(question)
        query_terms = set(tokenize(rewritten_query))

        scored_chunks = []
        for chunk in self.chunks:
            chunk_terms = set(tokenize(chunk.text + " " + chunk.title + " " + chunk.section))
            overlap = len(query_terms.intersection(chunk_terms))
            score = overlap / max(1, len(query_terms))
            scored_chunks.append(RetrievedChunk(chunk=chunk, score=score))

        scored_chunks.sort(key=lambda item: item.score, reverse=True)
        return rewritten_query, scored_chunks[:top_k]
