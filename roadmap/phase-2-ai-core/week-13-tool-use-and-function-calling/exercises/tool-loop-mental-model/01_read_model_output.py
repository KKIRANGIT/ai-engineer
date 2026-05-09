"""Read tool-call shaped output like an application would."""

from __future__ import annotations

import json


def main() -> None:
    mock_response = {
        "output": [
            {"type": "reasoning", "summary": "The user asked for ticket data and a refund calculation."},
            {
                "type": "function_call",
                "name": "lookup_ticket",
                "arguments": json.dumps({"ticket_id": "T-1002"}),
            },
            {
                "type": "function_call",
                "name": "calculate_refund",
                "arguments": json.dumps({"amount": 1200, "percent": 50}),
            },
        ]
    }

    print("Reading model output items...\n")

    for item in mock_response["output"]:
        if item["type"] != "function_call":
            print(f"Skipping non-tool item: {item['type']}")
            continue

        arguments = json.loads(item["arguments"])
        print(f"Tool requested: {item['name']}")
        print(f"Arguments: {arguments}")
        print("The application still needs to validate and execute this call.\n")


if __name__ == "__main__":
    main()
