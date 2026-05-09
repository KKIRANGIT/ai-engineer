from src.chunking import chunk_documents
from src.embeddings import build_embedding_client
from src.keyword_search import keyword_score
from src.models import SearchResult
from src.ranking import hybrid_score, semantic_score, sort_results
from src.store import load_documents


class SemanticSearchPlayground:
    def __init__(self) -> None:
        self.documents = load_documents()
        self.chunks = chunk_documents(self.documents)
        self.embedding_client = build_embedding_client()
        self.chunk_vectors = {
            chunk.chunk_id: self.embedding_client.embed_text(chunk.text)
            for chunk in self.chunks
        }

    def search(
        self,
        query: str,
        mode: str = "semantic",
        category: str | None = None,
        audience: str | None = None,
        top_k: int = 3,
    ) -> list[SearchResult]:
        query_vector = self.embedding_client.embed_text(query)
        results = []

        for chunk in self.chunks:
            if category and chunk.category != category:
                continue
            if audience and chunk.audience != audience:
                continue

            keyword_value = keyword_score(query, chunk.text)
            semantic_value = semantic_score(query_vector, self.chunk_vectors[chunk.chunk_id])

            if mode == "keyword":
                score = keyword_value
            elif mode == "semantic":
                score = semantic_value
            elif mode == "hybrid":
                score = hybrid_score(keyword_value, semantic_value)
            else:
                raise ValueError(f"Unsupported search mode: {mode}")

            results.append(
                SearchResult(
                    chunk=chunk,
                    score=score,
                    keyword_score=keyword_value,
                    semantic_score=semantic_value,
                )
            )

        return sort_results(results)[:top_k]
