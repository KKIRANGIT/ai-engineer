"""Retry and fallback helpers for the Week 17 project."""

from __future__ import annotations


def simulate_generation(user_input: str) -> tuple[bool, str]:
    if "timeout" in user_input.lower():
        return False, "simulated timeout"
    return True, "generation completed"


def retry_once(user_input: str) -> tuple[int, str]:
    attempts = 1
    ok, message = simulate_generation(user_input)
    if ok:
        return attempts, message

    attempts += 1
    return attempts, "fallback response after retry"
