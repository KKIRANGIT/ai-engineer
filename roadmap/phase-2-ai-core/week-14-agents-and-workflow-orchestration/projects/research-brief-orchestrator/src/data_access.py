"""Load local documents used by the Week 14 orchestration project."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "documents.json"


class DocumentStore:
    def __init__(self, path: Path | None = None) -> None:
        self.path = path or DATA_PATH
        with self.path.open("r", encoding="utf-8") as file:
            self.documents: list[dict[str, object]] = json.load(file)

    def all_documents(self) -> list[dict[str, object]]:
        return list(self.documents)
