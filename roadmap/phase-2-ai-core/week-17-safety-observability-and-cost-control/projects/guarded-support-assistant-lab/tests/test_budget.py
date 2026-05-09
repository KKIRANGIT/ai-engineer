from __future__ import annotations

import unittest

from src.budget import estimate_request_cost


class BudgetTests(unittest.TestCase):
    def test_cost_estimate_is_positive(self) -> None:
        cost = estimate_request_cost("hello world", "note", "response")
        self.assertGreater(cost, 0)


if __name__ == "__main__":
    unittest.main()
