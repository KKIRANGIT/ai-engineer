from __future__ import annotations

import unittest

from src.data_access import WorkspaceDataStore
from src.tools import calculate_refund, lookup_ticket, search_policy_docs


class ToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = WorkspaceDataStore()

    def test_lookup_ticket_returns_ticket(self) -> None:
        result = lookup_ticket(self.store, {"ticket_id": "T-1001"})
        self.assertTrue(result["found"])
        self.assertEqual(result["ticket"]["owner"], "Asha")

    def test_search_policy_docs_returns_matches(self) -> None:
        result = search_policy_docs(self.store, {"query": "refund policy", "topic": "refund"})
        self.assertTrue(result["found"])
        self.assertGreaterEqual(len(result["matches"]), 1)

    def test_calculate_refund_returns_expected_value(self) -> None:
        result = calculate_refund(self.store, {"amount": 1200, "percent": 50})
        self.assertEqual(result["refund_value"], 600.0)


if __name__ == "__main__":
    unittest.main()
