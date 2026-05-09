"""
Asynchronous loading helpers for the Week 06 pipeline.
"""

import asyncio
import csv
import json

from app.models import RawEventRecord


def _read_csv_rows(csv_file_path):
    """Read CSV rows synchronously and return raw event records."""
    with open(csv_file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            RawEventRecord(
                user_name=row["user_name"],
                event_name=row["event_name"],
                duration_minutes=row["duration_minutes"],
                status=row["status"],
            )
            for row in reader
        ]


def _read_score_mapping(scores_file_path):
    """Read the local JSON score mapping synchronously."""
    with open(scores_file_path, encoding="utf-8") as json_file:
        return json.load(json_file)


async def load_raw_events(csv_file_path):
    """Load raw event rows using a thread so the async pipeline can keep flowing."""
    await asyncio.sleep(0.05)
    return await asyncio.to_thread(_read_csv_rows, csv_file_path)


async def load_event_scores(scores_file_path):
    """Load score metadata using a thread-backed async wrapper."""
    await asyncio.sleep(0.05)
    return await asyncio.to_thread(_read_score_mapping, scores_file_path)
