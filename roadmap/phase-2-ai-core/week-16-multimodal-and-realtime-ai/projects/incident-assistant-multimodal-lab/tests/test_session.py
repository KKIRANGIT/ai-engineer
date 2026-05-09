from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.session import run_case


class SessionTests(unittest.TestCase):
    def test_multimodal_mode_contains_image_observations(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            from src import session as session_module

            original = session_module.TRACE_PATH
            session_module.TRACE_PATH = Path(temp_dir) / "trace.json"
            try:
                result = run_case("CASE-01", "multimodal")
                self.assertIn("Image observations", result.summary)
                self.assertTrue(Path(result.trace_path).exists())
            finally:
                session_module.TRACE_PATH = original

    def test_text_mode_omits_image_section(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            from src import session as session_module

            original = session_module.TRACE_PATH
            session_module.TRACE_PATH = Path(temp_dir) / "trace.json"
            try:
                result = run_case("CASE-01", "text")
                self.assertNotIn("Image observations", result.summary)
            finally:
                session_module.TRACE_PATH = original


if __name__ == "__main__":
    unittest.main()
