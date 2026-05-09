import unittest

from src.answer_generator import generate_grounded_answer
from src.models import PolicyChunk, RetrievedChunk


class AnswerGeneratorTests(unittest.TestCase):
    def test_generate_grounded_answer_returns_citations(self) -> None:
        retrieved_chunks = [
            RetrievedChunk(
                chunk=PolicyChunk(
                    chunk_id="policy_001_chunk_1",
                    document_id="policy_001",
                    title="Billing Resolution Policy",
                    section="refunds",
                    text="Support should open a refund review case.",
                ),
                score=0.9,
            )
        ]

        answer = generate_grounded_answer(
            "What should support do when a customer is charged twice?",
            "duplicate charge refund billing dispute",
            retrieved_chunks,
        )

        self.assertTrue(answer.citations)
        self.assertEqual(answer.citations[0]["document_id"], "policy_001")


if __name__ == "__main__":
    unittest.main()
