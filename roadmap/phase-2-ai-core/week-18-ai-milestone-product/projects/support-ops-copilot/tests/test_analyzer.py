from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src import analyzer as analyzer_module


class AnalyzerTests(unittest.TestCase):
    def test_security_ticket_escalates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            original = analyzer_module.TRACE_PATH
            analyzer_module.TRACE_PATH = Path(temp_dir) / "trace.json"
            try:
                output = analyzer_module.analyze_ticket("T-1003")
                self.assertEqual(output.category, "security")
                self.assertTrue(output.escalation_needed)
            finally:
                analyzer_module.TRACE_PATH = original

    def test_suspicious_ticket_goes_to_manual_review(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            original = analyzer_module.TRACE_PATH
            analyzer_module.TRACE_PATH = Path(temp_dir) / "trace.json"
            try:
                output = analyzer_module.analyze_ticket("T-1004")
                self.assertEqual(output.category, "manual_review")
                self.assertTrue(output.escalation_needed)
            finally:
                analyzer_module.TRACE_PATH = original


if __name__ == "__main__":
    unittest.main()
