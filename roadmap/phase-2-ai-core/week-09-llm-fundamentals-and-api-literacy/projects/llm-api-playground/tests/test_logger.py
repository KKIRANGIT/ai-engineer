import json
import tempfile
import unittest
from pathlib import Path

from src.logger import append_trace
from src.models import LLMRequest, NormalizedResponse, UsageMetrics


class LoggerTests(unittest.TestCase):
    def test_append_trace_writes_jsonl_line(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            log_path = Path(temp_directory) / "trace.jsonl"
            llm_request = LLMRequest(provider="mock", model="mock-model", prompt="hello")
            response = NormalizedResponse(
                provider="mock",
                model="mock-model",
                text="hello response",
                raw_id="mock-1",
                usage=UsageMetrics(input_tokens=10, output_tokens=5, total_tokens=15),
            )

            append_trace(log_path, llm_request, response)

            lines = log_path.read_text(encoding="utf-8").strip().splitlines()
            self.assertEqual(len(lines), 1)
            payload = json.loads(lines[0])
            self.assertEqual(payload["provider"], "mock")
            self.assertEqual(payload["text"], "hello response")


if __name__ == "__main__":
    unittest.main()
