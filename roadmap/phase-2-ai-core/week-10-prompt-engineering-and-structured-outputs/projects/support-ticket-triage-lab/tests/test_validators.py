import unittest

from src.validators import ValidationError, validate_structured_output


class ValidatorTests(unittest.TestCase):
    def test_validate_structured_output_accepts_valid_payload(self) -> None:
        payload = {
            "category": "billing",
            "priority": "medium",
            "summary": "Duplicate subscription charge reported.",
            "needs_human_follow_up": True,
            "confidence_note": "High confidence because the issue is explicit.",
        }

        validate_structured_output(payload)

    def test_validate_structured_output_rejects_invalid_enum_and_extra_field(self) -> None:
        payload = {
            "category": "other",
            "priority": "urgent",
            "summary": "Unknown issue.",
            "needs_human_follow_up": True,
            "confidence_note": "Low confidence.",
            "extra_field": "not allowed",
        }

        with self.assertRaises(ValidationError):
            validate_structured_output(payload)


if __name__ == "__main__":
    unittest.main()
