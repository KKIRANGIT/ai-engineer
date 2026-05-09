from __future__ import annotations

import unittest

from src.case_loader import get_ticket
from src.retrieval import infer_category, retrieve_policy_notes


class RetrievalTests(unittest.TestCase):
    def test_refund_ticket_retrieves_refund_policy(self) -> None:
        ticket = get_ticket("T-1001")
        notes = retrieve_policy_notes(ticket)
        self.assertEqual(infer_category(ticket), "refund")
        self.assertGreaterEqual(len(notes), 1)


if __name__ == "__main__":
    unittest.main()
