import unittest

from src.evaluation import run_evaluation
from src.rag_pipeline import GroundedPolicyAssistant


class RAGPipelineTests(unittest.TestCase):
    def test_pipeline_returns_citations_for_policy_question(self) -> None:
        assistant = GroundedPolicyAssistant()
        answer = assistant.answer("What should support do when a customer is charged twice?")

        self.assertTrue(answer.citations)
        self.assertEqual(answer.citations[0]["document_id"], "policy_001")

    def test_evaluation_passes_seed_questions(self) -> None:
        outcomes = run_evaluation()
        self.assertTrue(all(item["passed"] for item in outcomes))


if __name__ == "__main__":
    unittest.main()
