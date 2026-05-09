"""
This script demonstrates the rough shape of an OpenAI Responses API request
and the parts of the response that application code usually cares about.
"""

import json


def build_sample_request():
    return {
        "model": "gpt-5",
        "instructions": "You are a concise assistant.",
        "input": "Explain embeddings in two short paragraphs.",
    }


def build_sample_response():
    return {
        "id": "resp_123",
        "output": [
            {
                "type": "message",
                "role": "assistant",
                "content": [
                    {
                        "type": "output_text",
                        "text": "Embeddings turn text into numerical vectors that capture meaning.",
                    }
                ],
            }
        ],
        "output_text": "Embeddings turn text into numerical vectors that capture meaning.",
        "usage": {
            "input_tokens": 145,
            "output_tokens": 31,
            "total_tokens": 176,
        },
    }


def main():
    print("SAMPLE OPENAI REQUEST:")
    print(json.dumps(build_sample_request(), indent=2))

    print("\nSAMPLE OPENAI RESPONSE:")
    print(json.dumps(build_sample_response(), indent=2))


if __name__ == "__main__":
    main()
