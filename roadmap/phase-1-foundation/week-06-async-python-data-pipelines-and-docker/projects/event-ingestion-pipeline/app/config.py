"""
Configuration helpers for the Week 06 event ingestion pipeline.
"""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RAW_EVENTS_FILE = PROJECT_ROOT / "data" / "raw_events.csv"
DEFAULT_EVENT_SCORES_FILE = PROJECT_ROOT / "data" / "event_scores.json"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"


def _resolve_path(env_name, default_path):
    """Return an override path when provided, otherwise the default path."""
    override_value = os.getenv(env_name, "").strip()

    if not override_value:
        return default_path

    override_path = Path(override_value).expanduser()

    if not override_path.is_absolute():
        override_path = Path.cwd() / override_path

    return override_path


def get_raw_events_file():
    """Return the CSV input path."""
    return _resolve_path("RAW_EVENTS_FILE", DEFAULT_RAW_EVENTS_FILE)


def get_event_scores_file():
    """Return the JSON enrichment path."""
    return _resolve_path("EVENT_SCORES_FILE", DEFAULT_EVENT_SCORES_FILE)


def get_output_dir():
    """Return the output directory path."""
    output_dir = _resolve_path("PIPELINE_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir
