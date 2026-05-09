from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src import processor as processor_module


class ProcessorTests(unittest.TestCase):
    def test_low_risk_case_returns_response(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            original = processor_module.TRACE_PATH
            processor_module.TRACE_PATH = Path(temp_dir) / "trace.json"
            try:
                result = processor_module.run_case("CASE-01")
                self.assertFalse(result.blocked)
                self.assertTrue(Path(result.trace_path).exists())
            finally:
                processor_module.TRACE_PATH = original

    def test_high_risk_case_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            original = processor_module.TRACE_PATH
            processor_module.TRACE_PATH = Path(temp_dir) / "trace.json"
            try:
                result = processor_module.run_case("CASE-02")
                self.assertTrue(result.blocked)
            finally:
                processor_module.TRACE_PATH = original


if __name__ == "__main__":
    unittest.main()
