"""Provider-specific payload builders built from the shared internal tool registry."""

from __future__ import annotations

from .tool_schemas import get_tool_definitions


def build_openai_tools_payload() -> list[dict[str, object]]:
    payload: list[dict[str, object]] = []

    for tool in get_tool_definitions():
        payload.append(
            {
                "type": "function",
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["parameters"],
                "strict": True,
            }
        )

    return payload


def build_anthropic_tools_payload() -> list[dict[str, object]]:
    payload: list[dict[str, object]] = []

    for tool in get_tool_definitions():
        payload.append(
            {
                "name": tool["name"],
                "description": tool["description"],
                "input_schema": tool["parameters"],
            }
        )

    return payload
