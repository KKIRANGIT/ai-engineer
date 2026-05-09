"""Local data loading and lightweight search helpers for the Week 13 lab."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def _normalize(text: str) -> str:
    return " ".join(text.lower().split())


class WorkspaceDataStore:
    """Load local JSON data so the tool loop stays fully inspectable."""

    def __init__(self, data_dir: Path | None = None) -> None:
        self.data_dir = data_dir or DATA_DIR
        self.tickets = self._load_json("tickets.json")
        self.knowledge_base = self._load_json("knowledge_base.json")
        self.weather = self._load_json("weather.json")

    def _load_json(self, filename: str) -> list[dict[str, object]]:
        path = self.data_dir / filename
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_ticket(self, ticket_id: str) -> dict[str, object] | None:
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id:
                return ticket
        return None

    def search_policies(self, query: str, topic: str | None = None, limit: int = 2) -> list[dict[str, object]]:
        query_terms = set(_normalize(query).split())
        topic_value = _normalize(topic) if topic else None
        ranked_matches: list[tuple[int, dict[str, object]]] = []

        for document in self.knowledge_base:
            haystack = _normalize(
                f"{document['title']} {document['topic']} {document['summary']}"
            )
            if topic_value and _normalize(str(document["topic"])) != topic_value:
                continue

            score = sum(1 for term in query_terms if term in haystack)
            if score > 0:
                ranked_matches.append((score, document))

        ranked_matches.sort(key=lambda item: item[0], reverse=True)
        return [document for _, document in ranked_matches[:limit]]

    def get_weather(self, city: str) -> dict[str, object] | None:
        city_normalized = _normalize(city)
        for snapshot in self.weather:
            if _normalize(str(snapshot["city"])) == city_normalized:
                return snapshot
        return None

    def list_supported_cities(self) -> list[str]:
        return [str(item["city"]) for item in self.weather]
