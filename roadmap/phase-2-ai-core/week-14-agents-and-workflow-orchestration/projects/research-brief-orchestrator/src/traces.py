"""Trace recording for workflow runs."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class TraceRecorder:
    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def record(self, stage: str, payload: dict[str, Any]) -> None:
        self.events.append(
            {
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "stage": stage,
                "payload": payload,
            }
        )

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(self.events, file, indent=2)
