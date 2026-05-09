from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def get_documents_path() -> Path:
    return PROJECT_ROOT / "data" / "documents.json"


def get_evaluation_queries_path() -> Path:
    return PROJECT_ROOT / "data" / "evaluation_queries.json"


def get_embedding_mode() -> str:
    return os.getenv("EMBEDDING_MODE", "mock")


def get_openai_api_key() -> str:
    return os.getenv("OPENAI_API_KEY", "")


def get_openai_embedding_model() -> str:
    return os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
