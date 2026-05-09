"""Dataset loading for the Week 15 eval lab."""

from __future__ import annotations

import json
from pathlib import Path

from .models import EvalCase


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def load_eval_cases() -> list[EvalCase]:
    path = DATA_DIR / "eval_cases.json"
    with path.open("r", encoding="utf-8") as file:
        raw_cases = json.load(file)

    return [EvalCase(**raw_case) for raw_case in raw_cases]
