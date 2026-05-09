"""
This exercise shows how prompt size and output size influence rough token
economics and why even "good" answers have operational tradeoffs.
"""


def estimate_request_cost(input_tokens: int, output_tokens: int, input_rate: float, output_rate: float) -> float:
    input_cost = (input_tokens / 1_000_000) * input_rate
    output_cost = (output_tokens / 1_000_000) * output_rate
    return input_cost + output_cost


def main():
    scenarios = [
        {"name": "Short helper answer", "input_tokens": 900, "output_tokens": 250},
        {"name": "Long report summary", "input_tokens": 18_000, "output_tokens": 1_200},
    ]

    input_rate = 0.50
    output_rate = 1.50

    for scenario in scenarios:
        estimated_cost = estimate_request_cost(
            scenario["input_tokens"],
            scenario["output_tokens"],
            input_rate,
            output_rate,
        )
        print(
            f"{scenario['name']}: "
            f"input={scenario['input_tokens']} tokens, "
            f"output={scenario['output_tokens']} tokens, "
            f"estimated cost=${estimated_cost:.6f}"
        )


if __name__ == "__main__":
    main()
