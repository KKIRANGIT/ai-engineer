from __future__ import annotations

import unittest

from src.decision_memo import generate_decision_memo


class DecisionMemoTests(unittest.TestCase):
    def test_memo_mentions_fine_tuning(self) -> None:
        memo = generate_decision_memo()
        self.assertIn("Fine-tuning", memo)


if __name__ == "__main__":
    unittest.main()
