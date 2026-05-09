import unittest

from src.clients import (
    build_anthropic_payload,
    build_openai_payload,
    parse_anthropic_response,
    parse_openai_response,
)
from src.models import LLMRequest


class ClientPayloadTests(unittest.TestCase):
    def test_build_openai_payload_uses_responses_shape(self) -> None:
        llm_request = LLMRequest(
            provider="openai",
            model="gpt-5",
            prompt="Explain embeddings.",
            instructions="Be concise.",
            previous_response_id="resp_previous",
        )

        payload = build_openai_payload(llm_request)

        self.assertEqual(payload["model"], "gpt-5")
        self.assertEqual(payload["instructions"], "Be concise.")
        self.assertEqual(payload["input"], "Explain embeddings.")
        self.assertEqual(payload["previous_response_id"], "resp_previous")

    def test_build_anthropic_payload_uses_messages_shape(self) -> None:
        llm_request = LLMRequest(
            provider="anthropic",
            model="claude-sonnet-4-20250514",
            prompt="Explain embeddings.",
            instructions="Be concise.",
        )

        payload = build_anthropic_payload(llm_request)

        self.assertEqual(payload["system"], "Be concise.")
        self.assertEqual(payload["messages"][0]["role"], "user")
        self.assertEqual(payload["messages"][0]["content"], "Explain embeddings.")

    def test_parse_openai_response_extracts_output_text(self) -> None:
        llm_request = LLMRequest(provider="openai", model="gpt-5", prompt="hello")
        raw_response = {
            "id": "resp_1",
            "output_text": "Hello there.",
            "usage": {"input_tokens": 10, "output_tokens": 4, "total_tokens": 14},
        }

        response = parse_openai_response(raw_response, llm_request)

        self.assertEqual(response.text, "Hello there.")
        self.assertEqual(response.usage.total_tokens, 14)

    def test_parse_anthropic_response_extracts_text_blocks(self) -> None:
        llm_request = LLMRequest(provider="anthropic", model="claude-sonnet-4-20250514", prompt="hello")
        raw_response = {
            "id": "msg_1",
            "content": [{"type": "text", "text": "Hello from Claude."}],
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 12, "output_tokens": 5},
        }

        response = parse_anthropic_response(raw_response, llm_request)

        self.assertEqual(response.text, "Hello from Claude.")
        self.assertEqual(response.stop_reason, "end_turn")
        self.assertEqual(response.usage.total_tokens, 17)


if __name__ == "__main__":
    unittest.main()
