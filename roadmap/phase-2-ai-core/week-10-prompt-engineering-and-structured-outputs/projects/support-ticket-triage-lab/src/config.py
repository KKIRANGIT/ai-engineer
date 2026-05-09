from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def get_openai_api_key() -> str:
    return os.getenv("OPENAI_API_KEY", "")


def get_openai_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-4.1")


def get_prompt_library_path() -> Path:
    return PROJECT_ROOT / "prompt_library"


def get_schema_path() -> Path:
    return PROJECT_ROOT / "schemas" / "ticket_triage_schema.json"


def get_sample_tickets_path() -> Path:
    return PROJECT_ROOT / "data" / "sample_tickets.json"


def get_regression_cases_path() -> Path:
    return PROJECT_ROOT / "data" / "regression_cases.json"
