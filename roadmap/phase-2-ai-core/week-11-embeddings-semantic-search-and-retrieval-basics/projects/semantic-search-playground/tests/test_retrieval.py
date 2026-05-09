import unittest

from src.retrieval import SemanticSearchPlayground


class RetrievalTests(unittest.TestCase):
    def test_semantic_search_returns_billing_doc_for_refund_query(self) -> None:
        playground = SemanticSearchPlayground()
        results = playground.search("How do I get a refund for a duplicate charge?", mode="semantic", top_k=1)

        self.assertEqual(results[0].chunk.document_id, "doc_001")

    def test_filtering_excludes_wrong_audience(self) -> None:
        playground = SemanticSearchPlayground()
        results = playground.search(
            "How should staff escalate a large refund case?",
            mode="hybrid",
            audience="customers",
            top_k=3,
        )

        self.assertTrue(all(result.chunk.audience == "customers" for result in results))


if __name__ == "__main__":
    unittest.main()
