import unittest

from src.query_rewriter import rewrite_query


class QueryRewriterTests(unittest.TestCase):
    def test_rewrite_query_expands_duplicate_charge_case(self) -> None:
        rewritten = rewrite_query("What should support do when a customer is charged twice?")
        self.assertIn("duplicate charge", rewritten)


if __name__ == "__main__":
    unittest.main()
