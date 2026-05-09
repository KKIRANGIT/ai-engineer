from src.models import NormalizedResponse, UsageMetrics


def build_mock_response(provider: str, model: str, prompt: str) -> NormalizedResponse:
    trimmed_prompt = prompt.strip() or "No prompt supplied."
    text = (
        f"[mock:{provider}] This is a practice response for: {trimmed_prompt} "
        "It exists so you can inspect response handling without making a live API call."
    )

    usage = UsageMetrics(
        input_tokens=max(20, len(trimmed_prompt.split()) * 6),
        output_tokens=42,
        total_tokens=max(20, len(trimmed_prompt.split()) * 6) + 42,
    )

    return NormalizedResponse(
        provider=provider,
        model=model,
        text=text,
        raw_id=f"mock-{provider}-001",
        usage=usage,
        stop_reason="mock_complete",
    )
