import unittest

from src.context_builder import build_context
from src.models import PolicyChunk, RetrievedChunk


class ContextBuilderTests(unittest.TestCase):
    def test_build_context_includes_chunk_ids_and_titles(self) -> None:
        retrieved_chunks = [
            RetrievedChunk(
                chunk=PolicyChunk(
                    chunk_id="policy_001_chunk_1",
                    document_id="policy_001",
                    title="Billing Resolution Policy",
                    section="refunds",
                    text="Duplicate charges should trigger refund review.",
                ),
                score=1.0,
            )
        ]

        context = build_context(retrieved_chunks)
        self.assertIn("policy_001_chunk_1", context)
        self.assertIn("Billing Resolution Policy", context)


if __name__ == "__main__":
    unittest.main()
