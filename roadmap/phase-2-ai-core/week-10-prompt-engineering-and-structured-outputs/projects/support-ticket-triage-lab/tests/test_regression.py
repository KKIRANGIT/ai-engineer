import unittest

from src.regression import run_mock_regression


class RegressionTests(unittest.TestCase):
    def test_mock_regression_passes_all_seed_cases(self) -> None:
        outcomes = run_mock_regression()
        self.assertTrue(all(outcome.passed for outcome in outcomes))


if __name__ == "__main__":
    unittest.main()
