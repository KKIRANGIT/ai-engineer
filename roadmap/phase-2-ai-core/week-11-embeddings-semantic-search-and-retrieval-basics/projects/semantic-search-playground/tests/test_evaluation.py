import unittest

from src.evaluation import evaluate_mode


class EvaluationTests(unittest.TestCase):
    def test_hybrid_evaluation_passes_core_seed_queries(self) -> None:
        outcomes = evaluate_mode("hybrid")
        self.assertTrue(all(item["passed"] for item in outcomes))


if __name__ == "__main__":
    unittest.main()
