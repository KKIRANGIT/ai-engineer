from src.embeddings import cosine_similarity
from src.keyword_search import keyword_score
from src.models import SearchResult


def semantic_score(query_vector: list[float], chunk_vector: list[float]) -> float:
    return cosine_similarity(query_vector, chunk_vector)


def hybrid_score(keyword_value: float, semantic_value: float, keyword_weight: float = 0.4) -> float:
    semantic_weight = 1.0 - keyword_weight
    return (keyword_value * keyword_weight) + (semantic_value * semantic_weight)


def sort_results(results: list[SearchResult]) -> list[SearchResult]:
    return sorted(results, key=lambda item: item.score, reverse=True)
