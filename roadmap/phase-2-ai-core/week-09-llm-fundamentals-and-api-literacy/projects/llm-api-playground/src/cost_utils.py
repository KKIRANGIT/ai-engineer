from src.models import UsageMetrics


PROVIDER_RATES = {
    "openai": {"input_per_million": 1.25, "output_per_million": 10.0},
    "anthropic": {"input_per_million": 3.0, "output_per_million": 15.0},
    "mock": {"input_per_million": 0.0, "output_per_million": 0.0},
}


def estimate_cost(provider: str, usage: UsageMetrics) -> float:
    rates = PROVIDER_RATES.get(provider, PROVIDER_RATES["mock"])
    input_cost = (usage.input_tokens / 1_000_000) * rates["input_per_million"]
    output_cost = (usage.output_tokens / 1_000_000) * rates["output_per_million"]
    return input_cost + output_cost
