"""Estimate request cost from rough token counts."""

from __future__ import annotations


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def main() -> None:
    prompt = "Customer asked for refund guidance."
    output = "Support response."
    input_tokens = estimate_tokens(prompt)
    output_tokens = estimate_tokens(output)
    print(f"input_tokens={input_tokens}")
    print(f"output_tokens={output_tokens}")


if __name__ == "__main__":
    main()
