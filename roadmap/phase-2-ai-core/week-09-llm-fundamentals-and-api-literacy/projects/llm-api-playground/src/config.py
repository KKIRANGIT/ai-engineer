from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOG_PATH = PROJECT_ROOT / "logs" / "traces.jsonl"


def get_openai_api_key() -> str:
    return os.getenv("OPENAI_API_KEY", "")


def get_anthropic_api_key() -> str:
    return os.getenv("ANTHROPIC_API_KEY", "")


def get_anthropic_version() -> str:
    return os.getenv("ANTHROPIC_VERSION", "2023-06-01")


def get_log_path() -> Path:
    configured_path = os.getenv("LLM_PLAYGROUND_LOG_PATH")
    return Path(configured_path) if configured_path else DEFAULT_LOG_PATH


def get_timeout_seconds() -> int:
    return int(os.getenv("LLM_PLAYGROUND_TIMEOUT_SECONDS", "30"))
