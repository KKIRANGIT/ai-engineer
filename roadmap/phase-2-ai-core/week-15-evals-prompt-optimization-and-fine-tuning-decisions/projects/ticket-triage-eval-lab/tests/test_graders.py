from __future__ import annotations

import unittest

from src.dataset import load_eval_cases
from src.graders import grade_case
from src.models import SystemOutput


class GraderTests(unittest.TestCase):
    def test_grade_case_rewards_matching_output(self) -> None:
        case = load_eval_cases()[0]
        output = SystemOutput(
            category="refund",
            priority="medium",
            next_action="Route to refund queue and manager approval path",
            customer_reply="Thanks for the details. manager approval",
        )
        score = grade_case(case, "test", output)
        self.assertGreaterEqual(score.total_score, 5)


if __name__ == "__main__":
    unittest.main()
