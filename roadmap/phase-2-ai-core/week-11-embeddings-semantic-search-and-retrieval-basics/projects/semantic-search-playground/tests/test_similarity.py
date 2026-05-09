import unittest

from src.embeddings import MockEmbeddingClient, cosine_similarity


class SimilarityTests(unittest.TestCase):
    def test_cosine_similarity_is_higher_for_related_text(self) -> None:
        client = MockEmbeddingClient()
        query = client.embed_text("refund charged twice")
        related = client.embed_text("billing refund issue")
        unrelated = client.embed_text("dark mode request")

        self.assertGreater(cosine_similarity(query, related), cosine_similarity(query, unrelated))


if __name__ == "__main__":
    unittest.main()
