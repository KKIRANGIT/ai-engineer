from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def get_policy_documents_path() -> Path:
    return PROJECT_ROOT / "data" / "policy_documents.json"


def get_evaluation_questions_path() -> Path:
    return PROJECT_ROOT / "data" / "evaluation_questions.json"


def get_top_k() -> int:
    return int(os.getenv("RAG_TOP_K", "3"))


def get_sentences_per_chunk() -> int:
    return int(os.getenv("RAG_SENTENCES_PER_CHUNK", "2"))
