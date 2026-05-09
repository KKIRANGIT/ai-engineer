import argparse
from pprint import pprint

from src.clients import ProviderConfigurationError, run_request
from src.config import get_log_path
from src.cost_utils import estimate_cost
from src.logger import append_trace
from src.models import LLMRequest
from src.prompts import DEFAULT_INSTRUCTIONS, build_default_prompt
from src.sample_data import build_mock_response


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 09 LLM API Playground")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ask_parser = subparsers.add_parser("ask", help="Run one provider request.")
    ask_parser.add_argument("--provider", choices=["mock", "openai", "anthropic"], required=True)
    ask_parser.add_argument("--model", default="mock-model-v1")
    ask_parser.add_argument("--prompt", required=True)
    ask_parser.add_argument("--instructions", default=DEFAULT_INSTRUCTIONS)
    ask_parser.add_argument("--max-output-tokens", type=int, default=400)

    compare_parser = subparsers.add_parser("compare", help="Run mock comparison for OpenAI and Anthropic shapes.")
    compare_parser.add_argument("--prompt", required=True)
    compare_parser.add_argument("--instructions", default=DEFAULT_INSTRUCTIONS)

    return parser


def print_response(response):
    pprint(
        {
            "provider": response.provider,
            "model": response.model,
            "raw_id": response.raw_id,
            "stop_reason": response.stop_reason,
            "latency_seconds": response.latency_seconds,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.total_tokens,
            },
            "estimated_cost_usd": estimate_cost(response.provider, response.usage),
            "text": response.text,
        }
    )


def run_single_request(arguments) -> None:
    llm_request = LLMRequest(
        provider=arguments.provider,
        model=arguments.model,
        prompt=build_default_prompt(arguments.prompt),
        instructions=arguments.instructions,
        max_output_tokens=arguments.max_output_tokens,
    )

    response = run_request(llm_request)
    append_trace(get_log_path(), llm_request, response)
    print_response(response)


def run_comparison(arguments) -> None:
    for provider_name, model_name in [
        ("openai", "gpt-5-mock-shape"),
        ("anthropic", "claude-sonnet-4-mock-shape"),
    ]:
        llm_request = LLMRequest(
            provider=provider_name,
            model=model_name,
            prompt=build_default_prompt(arguments.prompt),
            instructions=arguments.instructions,
        )
        response = build_mock_response(provider_name, model_name, llm_request.prompt)
        append_trace(get_log_path(), llm_request, response)
        print("\n--- comparison result ---")
        print_response(response)


def main() -> None:
    parser = build_argument_parser()
    arguments = parser.parse_args()

    try:
        if arguments.command == "ask":
            run_single_request(arguments)
        elif arguments.command == "compare":
            run_comparison(arguments)
    except ProviderConfigurationError as error:
        print(f"Configuration error: {error}")
    except Exception as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()
