from __future__ import annotations

import unittest

from src.analysis import compare_variants, run_variant


class AnalysisTests(unittest.TestCase):
    def test_run_variant_returns_all_cases(self) -> None:
        scores = run_variant("baseline")
        self.assertEqual(len(scores), 4)

    def test_retrieval_variant_scores_at_least_as_well_as_baseline(self) -> None:
        comparison = compare_variants(["baseline", "retrieval_v1"])
        self.assertGreaterEqual(
            comparison["retrieval_v1"]["average_score"],
            comparison["baseline"]["average_score"],
        )


if __name__ == "__main__":
    unittest.main()
