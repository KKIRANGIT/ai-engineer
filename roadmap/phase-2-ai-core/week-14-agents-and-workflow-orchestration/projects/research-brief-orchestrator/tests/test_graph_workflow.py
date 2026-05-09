from __future__ import annotations

import unittest

from src.data_access import DocumentStore
from src.graph_workflow import run_graph_workflow


class GraphWorkflowTests(unittest.TestCase):
    def test_graph_workflow_can_retry_before_drafting(self) -> None:
        state = run_graph_workflow(
            "Summarize travel reimbursement and security requirements.",
            DocumentStore(),
        )
        self.assertIn("travel", state.topics)
        self.assertIn("security", state.topics)
        self.assertGreaterEqual(len(state.step_history), 4)
        self.assertTrue(state.brief)


if __name__ == "__main__":
    unittest.main()
