import time

from src import config
from src.http_utils import post_json
from src.models import LLMRequest, NormalizedResponse, UsageMetrics
from src.sample_data import build_mock_response


class ProviderConfigurationError(Exception):
    """Raised when required configuration for a provider is missing."""


def build_openai_payload(llm_request: LLMRequest) -> dict:
    payload = {
        "model": llm_request.model,
        "instructions": llm_request.instructions,
        "input": llm_request.prompt,
        "max_output_tokens": llm_request.max_output_tokens,
    }

    if llm_request.previous_response_id:
        payload["previous_response_id"] = llm_request.previous_response_id

    return payload


def build_anthropic_payload(llm_request: LLMRequest) -> dict:
    payload = {
        "model": llm_request.model,
        "system": llm_request.instructions,
        "max_tokens": llm_request.max_output_tokens,
        "messages": [
            {
                "role": "user",
                "content": llm_request.prompt,
            }
        ],
    }
    return payload


def parse_openai_response(raw_response: dict, llm_request: LLMRequest) -> NormalizedResponse:
    usage = raw_response.get("usage", {})
    return NormalizedResponse(
        provider="openai",
        model=llm_request.model,
        text=raw_response.get("output_text", ""),
        raw_id=raw_response.get("id", ""),
        usage=UsageMetrics(
            input_tokens=usage.get("input_tokens", 0),
            output_tokens=usage.get("output_tokens", 0),
            total_tokens=usage.get("total_tokens", 0),
        ),
    )


def parse_anthropic_response(raw_response: dict, llm_request: LLMRequest) -> NormalizedResponse:
    text_blocks = [
        block.get("text", "")
        for block in raw_response.get("content", [])
        if block.get("type") == "text"
    ]
    usage = raw_response.get("usage", {})
    input_tokens = usage.get("input_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)

    return NormalizedResponse(
        provider="anthropic",
        model=llm_request.model,
        text="\n".join(text_blocks),
        raw_id=raw_response.get("id", ""),
        usage=UsageMetrics(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
        ),
        stop_reason=raw_response.get("stop_reason"),
    )


def run_request(llm_request: LLMRequest) -> NormalizedResponse:
    if llm_request.provider == "mock":
        return build_mock_response("mock", llm_request.model, llm_request.prompt)

    if llm_request.provider == "openai":
        api_key = config.get_openai_api_key()
        if not api_key:
            raise ProviderConfigurationError("OPENAI_API_KEY is required for live OpenAI requests.")

        payload = build_openai_payload(llm_request)
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        started_at = time.perf_counter()
        raw_response = post_json(
            "https://api.openai.com/v1/responses",
            headers=headers,
            payload=payload,
            timeout_seconds=config.get_timeout_seconds(),
        )
        normalized = parse_openai_response(raw_response, llm_request)
        normalized.latency_seconds = time.perf_counter() - started_at
        return normalized

    if llm_request.provider == "anthropic":
        api_key = config.get_anthropic_api_key()
        if not api_key:
            raise ProviderConfigurationError("ANTHROPIC_API_KEY is required for live Anthropic requests.")

        payload = build_anthropic_payload(llm_request)
        headers = {
            "x-api-key": api_key,
            "anthropic-version": config.get_anthropic_version(),
            "content-type": "application/json",
        }

        started_at = time.perf_counter()
        raw_response = post_json(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            payload=payload,
            timeout_seconds=config.get_timeout_seconds(),
        )
        normalized = parse_anthropic_response(raw_response, llm_request)
        normalized.latency_seconds = time.perf_counter() - started_at
        return normalized

    raise ProviderConfigurationError(f"Unsupported provider: {llm_request.provider}")
