"""Deterministic incident analysis for the Week 16 lab."""

from __future__ import annotations


def generate_summary(context: dict[str, object], mode: str) -> str:
    text_report = str(context["text_report"])
    transcript = str(context["transcript_excerpt"])
    image_observations = list(context["image_observations"])

    lines = [f"Incident summary ({mode} mode):", ""]
    lines.append(f"Reported issue: {text_report}")

    if transcript:
        lines.append(f"Transcript signal: {transcript}")

    if image_observations:
        lines.append("Image observations:")
        for observation in image_observations:
            lines.append(f"- {observation}")

    if image_observations or transcript:
        lines.append("")
        lines.append("Assessment: Multimodal context provides additional grounding for urgency and next action.")
    else:
        lines.append("")
        lines.append("Assessment: Text-only context gives a usable summary but may miss visible or spoken details.")

    return "\n".join(lines)
