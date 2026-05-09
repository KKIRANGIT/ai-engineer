"""Write evaluation reports to disk."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ARTIFACT_DIR = Path("artifacts")


def write_report(filename: str, payload: dict[str, Any]) -> Path:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    path = ARTIFACT_DIR / filename
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)
    return path
