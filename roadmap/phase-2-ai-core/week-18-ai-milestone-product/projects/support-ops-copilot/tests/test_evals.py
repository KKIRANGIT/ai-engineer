from __future__ import annotations

import unittest

from src.evals import run_eval


class EvalTests(unittest.TestCase):
    def test_eval_suite_runs(self) -> None:
        result = run_eval()
        self.assertEqual(result["case_count"], 4)
        self.assertGreaterEqual(result["average_score"], 0.75)


if __name__ == "__main__":
    unittest.main()
