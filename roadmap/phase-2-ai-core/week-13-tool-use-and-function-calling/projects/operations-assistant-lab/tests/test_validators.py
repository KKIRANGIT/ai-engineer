from __future__ import annotations

import unittest

from src.validators import ValidationError, validate_tool_arguments


class ValidatorTests(unittest.TestCase):
    def test_lookup_ticket_validation_accepts_expected_format(self) -> None:
        validated = validate_tool_arguments("lookup_ticket", {"ticket_id": "t-1002"})
        self.assertEqual(validated["ticket_id"], "T-1002")

    def test_lookup_ticket_validation_rejects_bad_format(self) -> None:
        with self.assertRaises(ValidationError):
            validate_tool_arguments("lookup_ticket", {"ticket_id": "1002"})

    def test_calculate_refund_validation_rejects_large_percent(self) -> None:
        with self.assertRaises(ValidationError):
            validate_tool_arguments("calculate_refund", {"amount": 1000, "percent": 150})


if __name__ == "__main__":
    unittest.main()
