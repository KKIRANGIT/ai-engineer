"""
Pipeline stages for the Week 06 event ingestion project.
"""

import csv
import json

from app.models import CleanEventRecord


def parse_duration(raw_duration):
    """Convert a raw duration string into an integer with safe fallback."""
    try:
        return int(raw_duration)
    except ValueError:
        return 0


def normalize_status(raw_status):
    """Normalize status text into a predictable lowercase value."""
    return raw_status.strip().lower()


def clean_and_enrich_events(raw_events, score_mapping):
    """Convert raw event records into cleaned enriched records."""
    cleaned_events = []

    for raw_event in raw_events:
        event_name = raw_event.event_name.strip().lower()
        cleaned_events.append(
            CleanEventRecord(
                user_name=raw_event.user_name.strip().title(),
                event_name=event_name,
                duration_minutes=parse_duration(raw_event.duration_minutes),
                status=normalize_status(raw_event.status),
                score=score_mapping.get(event_name, 0),
            )
        )

    return cleaned_events


def write_cleaned_csv(cleaned_events, output_file_path):
    """Write cleaned event records to a CSV file."""
    with open(output_file_path, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = [
            "user_name",
            "event_name",
            "duration_minutes",
            "status",
            "score",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for event in cleaned_events:
            writer.writerow(
                {
                    "user_name": event.user_name,
                    "event_name": event.event_name,
                    "duration_minutes": event.duration_minutes,
                    "status": event.status,
                    "score": event.score,
                }
            )


def write_summary_report(summary_data, output_file_path):
    """Write summary data to JSON for easy inspection."""
    with open(output_file_path, "w", encoding="utf-8") as json_file:
        json.dump(summary_data, json_file, indent=2)
