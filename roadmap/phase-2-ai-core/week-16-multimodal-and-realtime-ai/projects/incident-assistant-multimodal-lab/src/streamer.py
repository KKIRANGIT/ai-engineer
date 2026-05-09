"""Streaming helpers for partial response output."""

from __future__ import annotations


def stream_text(summary: str, chunk_size: int = 80) -> list[str]:
    chunks: list[str] = []
    for start in range(0, len(summary), chunk_size):
        chunks.append(summary[start : start + chunk_size])
    return chunks
