"""Guarded request processor for the Week 17 project."""

from __future__ import annotations

from pathlib import Path

from .budget import estimate_request_cost, over_budget
from .case_loader import get_case
from .guardrails import assess_risk, should_block
from .models import RunResult
from .retry_logic import retry_once
from .traces import TraceRecorder
from .trust import classify_trust_boundaries


TRACE_PATH = Path("artifacts/latest_trace.json")


def run_case(case_id: str) -> RunResult:
    case = get_case(case_id)
    recorder = TraceRecorder()
    recorder.record("request_loaded", {"case_id": case.case_id})

    trust_map = classify_trust_boundaries(case)
    recorder.record("trust_boundaries", trust_map)

    risk_level, findings = assess_risk(case)
    recorder.record("risk_assessed", {"risk_level": risk_level, "findings": findings})

    if should_block(risk_level):
        response_text = "Request blocked due to high-risk instruction pattern."
        estimated_cost = estimate_request_cost(case.user_input, case.retrieved_note, response_text)
        recorder.record("request_blocked", {"response_text": response_text, "estimated_cost": estimated_cost})
        recorder.save(TRACE_PATH)
        return RunResult(
            case_id=case.case_id,
            risk_level=risk_level,
            blocked=True,
            estimated_cost=estimated_cost,
            response_text=response_text,
            trace_path=str(TRACE_PATH),
        )

    attempts, generation_status = retry_once(case.user_input)
    recorder.record("generation_attempted", {"attempts": attempts, "status": generation_status})

    response_text = (
        "Support response: we will review the request using the approved support workflow and avoid following "
        "untrusted instructions from external content."
    )
    estimated_cost = estimate_request_cost(case.user_input, case.retrieved_note, response_text)
    recorder.record("cost_estimated", {"estimated_cost": estimated_cost})

    if over_budget(estimated_cost):
        response_text = "Request halted because the estimated budget threshold was exceeded."
        recorder.record("budget_block", {"estimated_cost": estimated_cost})

    recorder.record("response_ready", {"response_text": response_text})
    recorder.save(TRACE_PATH)

    return RunResult(
        case_id=case.case_id,
        risk_level=risk_level,
        blocked=False,
        estimated_cost=estimated_cost,
        response_text=response_text,
        trace_path=str(TRACE_PATH),
    )
