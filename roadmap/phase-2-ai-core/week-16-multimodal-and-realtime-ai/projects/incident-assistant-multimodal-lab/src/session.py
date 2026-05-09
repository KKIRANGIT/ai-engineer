"""Realtime-style session simulation for the Week 16 lab."""

from __future__ import annotations

from pathlib import Path

from .analysis import generate_summary
from .case_loader import get_case
from .models import IncidentResult
from .multimodal_fusion import build_context
from .streamer import stream_text
from .traces import TraceRecorder


TRACE_PATH = Path("artifacts/latest_trace.json")


def run_case(case_id: str, mode: str) -> IncidentResult:
    case = get_case(case_id)
    recorder = TraceRecorder()
    recorder.record("session_started", {"case_id": case.case_id, "mode": mode})

    context = build_context(case, mode)
    recorder.record("context_loaded", {"fields": list(context.keys())})

    if mode in {"multimodal", "session"}:
        recorder.record("transcript_ready", {"transcript_excerpt": context["transcript_excerpt"]})
        recorder.record("vision_ready", {"image_observation_count": len(context["image_observations"])})

    summary = generate_summary(context, mode)
    chunks = stream_text(summary)

    for index, chunk in enumerate(chunks, start=1):
        recorder.record("response_chunk", {"index": index, "text": chunk})

    recorder.record("session_completed", {"chunk_count": len(chunks)})
    recorder.save(TRACE_PATH)

    return IncidentResult(
        case_id=case.case_id,
        mode=mode,
        summary=summary,
        streamed_chunks=chunks,
        trace_path=str(TRACE_PATH),
    )
