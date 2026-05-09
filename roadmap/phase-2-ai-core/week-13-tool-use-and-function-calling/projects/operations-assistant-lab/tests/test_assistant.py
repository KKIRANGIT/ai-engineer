from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.assistant import OperationsAssistant
from src.data_access import WorkspaceDataStore


class AssistantTests(unittest.TestCase):
    def test_multi_tool_query_runs_and_writes_trace(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            trace_path = Path(temp_dir) / "trace.json"
            assistant = OperationsAssistant(store=WorkspaceDataStore(), trace_path=trace_path)

            result = assistant.run(
                "Look up ticket T-1002, search the refund policy, and calculate 50 percent of 1200."
            )

            self.assertEqual(len(result.planned_calls), 3)
            self.assertIn("lookup_ticket", result.final_answer)
            self.assertIn("search_policy_docs", result.final_answer)
            self.assertIn("calculate_refund", result.final_answer)
            self.assertTrue(trace_path.exists())

    def test_query_without_tool_pattern_returns_guidance(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            assistant = OperationsAssistant(trace_path=Path(temp_dir) / "trace.json")
            result = assistant.run("Hello there")
            self.assertIn("No tool call was planned", result.final_answer)


if __name__ == "__main__":
    unittest.main()
