from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = PROJECT_ROOT / "data" / "study_tracker.db"


def get_host() -> str:
    return os.getenv("HOST", "127.0.0.1")


def get_port() -> int:
    return int(os.getenv("PORT", "8000"))


def get_database_path() -> Path:
    configured_path = os.getenv("APP_DB_PATH")
    if configured_path:
        return Path(configured_path)
    return DEFAULT_DB_PATH
