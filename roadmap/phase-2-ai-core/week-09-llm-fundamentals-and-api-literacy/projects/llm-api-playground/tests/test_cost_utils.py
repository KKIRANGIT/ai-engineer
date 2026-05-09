import unittest

from src.cost_utils import estimate_cost
from src.models import UsageMetrics


class CostUtilsTests(unittest.TestCase):
    def test_estimate_cost_returns_zero_for_mock_provider(self) -> None:
        usage = UsageMetrics(input_tokens=1000, output_tokens=500, total_tokens=1500)
        self.assertEqual(estimate_cost("mock", usage), 0.0)

    def test_estimate_cost_returns_positive_value_for_openai(self) -> None:
        usage = UsageMetrics(input_tokens=2000, output_tokens=1000, total_tokens=3000)
        self.assertGreater(estimate_cost("openai", usage), 0.0)


if __name__ == "__main__":
    unittest.main()
