import json

from src import config
from src.models import Document


def load_documents() -> list[Document]:
    raw_items = json.loads(config.get_documents_path().read_text(encoding="utf-8"))
    return [Document(**item) for item in raw_items]


def load_evaluation_queries() -> list[dict]:
    return json.loads(config.get_evaluation_queries_path().read_text(encoding="utf-8"))
