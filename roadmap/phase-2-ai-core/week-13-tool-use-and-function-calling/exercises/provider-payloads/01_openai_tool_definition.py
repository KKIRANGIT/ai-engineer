"""Render OpenAI function-tool payloads from a shared tool registry."""

from __future__ import annotations

import json
from pathlib import Path
import sys


PROJECT_SRC = Path(__file__).resolve().parents[2] / "projects" / "operations-assistant-lab"
sys.path.insert(0, str(PROJECT_SRC))

from src.providers import build_openai_tools_payload  # noqa: E402


def main() -> None:
    payload = build_openai_tools_payload()
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
