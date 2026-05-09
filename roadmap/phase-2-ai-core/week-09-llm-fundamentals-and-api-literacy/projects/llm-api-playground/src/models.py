from dataclasses import dataclass, field


@dataclass
class LLMRequest:
    provider: str
    model: str
    prompt: str
    instructions: str = ""
    max_output_tokens: int = 400
    previous_response_id: str | None = None


@dataclass
class UsageMetrics:
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0


@dataclass
class NormalizedResponse:
    provider: str
    model: str
    text: str
    raw_id: str
    usage: UsageMetrics = field(default_factory=UsageMetrics)
    stop_reason: str | None = None
    latency_seconds: float = 0.0
