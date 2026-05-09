from __future__ import annotations

import unittest

from src.agent_loop import run_agent_loop
from src.data_access import DocumentStore


class AgentLoopTests(unittest.TestCase):
    def test_agent_loop_handles_multi_topic_query(self) -> None:
        state = run_agent_loop(
            "Create a brief about laptop requests and refund exceptions.",
            DocumentStore(),
        )
        self.assertIn("equipment", state.topics)
        self.assertIn("refund", state.topics)
        self.assertGreaterEqual(len(state.retrieved_docs), 2)
        self.assertIn("Key guidance", state.brief)


if __name__ == "__main__":
    unittest.main()
