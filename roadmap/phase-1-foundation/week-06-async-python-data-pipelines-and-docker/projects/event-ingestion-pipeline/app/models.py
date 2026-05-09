"""
Data models for the Week 06 event ingestion pipeline.
"""

from dataclasses import dataclass


@dataclass
class RawEventRecord:
    """Represent one raw row from the CSV source."""

    user_name: str
    event_name: str
    duration_minutes: str
    status: str


@dataclass
class CleanEventRecord:
    """Represent one cleaned and enriched event record."""

    user_name: str
    event_name: str
    duration_minutes: int
    status: str
    score: int
