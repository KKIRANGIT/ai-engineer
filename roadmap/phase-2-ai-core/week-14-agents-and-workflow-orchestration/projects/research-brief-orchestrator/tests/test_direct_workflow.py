from __future__ import annotations

import unittest

from src.data_access import DocumentStore
from src.direct_workflow import run_direct_workflow


class DirectWorkflowTests(unittest.TestCase):
    def test_direct_workflow_retrieves_refund_docs(self) -> None:
        state = run_direct_workflow(
            "Prepare a brief about refund policy for enterprise customers.",
            DocumentStore(),
        )
        self.assertIn("refund", state.topics)
        self.assertGreaterEqual(len(state.retrieved_docs), 1)
        self.assertIn("Research brief for", state.brief)


if __name__ == "__main__":
    unittest.main()
