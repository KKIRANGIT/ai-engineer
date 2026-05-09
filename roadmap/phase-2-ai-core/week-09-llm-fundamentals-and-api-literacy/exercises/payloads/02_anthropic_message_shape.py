"""
This script demonstrates the rough shape of an Anthropic Messages API request
and the assistant content blocks returned in the response.
"""

import json


def build_sample_request():
    return {
        "model": "claude-sonnet-4-20250514",
        "system": "You are a concise assistant.",
        "max_tokens": 300,
        "messages": [
            {
                "role": "user",
                "content": "Explain embeddings in two short paragraphs.",
            }
        ],
    }


def build_sample_response():
    return {
        "id": "msg_123",
        "type": "message",
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Embeddings convert text into vectors that represent semantic meaning.",
            }
        ],
        "stop_reason": "end_turn",
        "usage": {
            "input_tokens": 142,
            "output_tokens": 29,
        },
    }


def main():
    print("SAMPLE ANTHROPIC REQUEST:")
    print(json.dumps(build_sample_request(), indent=2))

    print("\nSAMPLE ANTHROPIC RESPONSE:")
    print(json.dumps(build_sample_response(), indent=2))


if __name__ == "__main__":
    main()
