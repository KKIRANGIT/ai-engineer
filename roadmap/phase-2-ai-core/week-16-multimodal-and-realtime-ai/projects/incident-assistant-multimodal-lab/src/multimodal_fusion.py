"""Combine text, transcript, and image observations into a unified context."""

from __future__ import annotations

from .models import IncidentCase


def build_context(case: IncidentCase, mode: str) -> dict[str, object]:
    if mode == "text":
        return {
            "title": case.title,
            "text_report": case.text_report,
            "transcript_excerpt": "",
            "image_observations": [],
        }

    if mode in {"multimodal", "session"}:
        return {
            "title": case.title,
            "text_report": case.text_report,
            "transcript_excerpt": case.transcript_excerpt,
            "image_observations": case.image_observations,
        }

    raise ValueError(f"Unsupported mode: {mode}")
