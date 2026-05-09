import json

from src import config
from src.models import PolicyDocument


def load_policy_documents() -> list[PolicyDocument]:
    raw_items = json.loads(config.get_policy_documents_path().read_text(encoding="utf-8"))
    return [PolicyDocument(**item) for item in raw_items]


def load_evaluation_questions() -> list[dict]:
    return json.loads(config.get_evaluation_questions_path().read_text(encoding="utf-8"))
