import unittest

from src.openai_structured_client import build_openai_structured_payload
from src.validators import load_schema


class OpenAIStructuredClientTests(unittest.TestCase):
    def test_build_openai_structured_payload_uses_json_schema_format(self) -> None:
        payload = build_openai_structured_payload(
            model="gpt-4.1",
            prompt_text="Classify this support ticket.",
            schema=load_schema(),
        )

        self.assertEqual(payload["model"], "gpt-4.1")
        self.assertEqual(payload["text"]["format"]["type"], "json_schema")
        self.assertTrue(payload["text"]["format"]["strict"])
        self.assertEqual(payload["text"]["format"]["name"], "ticket_triage")


if __name__ == "__main__":
    unittest.main()
