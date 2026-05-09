from __future__ import annotations

import unittest

from src.case_loader import get_case
from src.guardrails import assess_risk, should_block


class GuardrailTests(unittest.TestCase):
    def test_high_risk_case_is_blocked(self) -> None:
        case = get_case("CASE-02")
        risk_level, _ = assess_risk(case)
        self.assertEqual(risk_level, "high")
        self.assertTrue(should_block(risk_level))


if __name__ == "__main__":
    unittest.main()
