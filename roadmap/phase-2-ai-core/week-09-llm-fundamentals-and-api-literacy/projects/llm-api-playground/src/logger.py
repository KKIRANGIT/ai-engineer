import json
from datetime import datetime
from pathlib import Path

from src.cost_utils import estimate_cost
from src.models import LLMRequest, NormalizedResponse


def append_trace(log_path: Path, llm_request: LLMRequest, response: NormalizedResponse) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)

    trace = {
        "timestamp": datetime.utcnow().isoformat(timespec="seconds"),
        "provider": response.provider,
        "model": response.model,
        "prompt": llm_request.prompt,
        "instructions": llm_request.instructions,
        "text": response.text,
        "raw_id": response.raw_id,
        "stop_reason": response.stop_reason,
        "latency_seconds": response.latency_seconds,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "total_tokens": response.usage.total_tokens,
        },
        "estimated_cost_usd": estimate_cost(response.provider, response.usage),
    }

    with log_path.open("a", encoding="utf-8") as file_handle:
        file_handle.write(json.dumps(trace) + "\n")
