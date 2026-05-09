"""Load local incident cases for the Week 16 project."""

from __future__ import annotations

import json
from pathlib import Path

from .models import IncidentCase


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "incident_cases.json"


def load_cases() -> list[IncidentCase]:
    with DATA_PATH.open("r", encoding="utf-8") as file:
        raw_cases = json.load(file)
    return [IncidentCase(**raw_case) for raw_case in raw_cases]


def get_case(case_id: str) -> IncidentCase:
    for case in load_cases():
        if case.case_id == case_id:
            return case
    raise ValueError(f"Unknown case_id: {case_id}")
