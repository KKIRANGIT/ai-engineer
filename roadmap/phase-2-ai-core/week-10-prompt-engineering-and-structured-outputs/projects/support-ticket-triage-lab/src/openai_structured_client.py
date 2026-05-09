import json
from urllib import error, request

from src import config


def build_openai_structured_payload(model: str, prompt_text: str, schema: dict) -> dict:
    return {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": prompt_text,
            }
        ],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "ticket_triage",
                "strict": True,
                "schema": schema,
            }
        },
    }


def call_openai_structured_output(model: str, prompt_text: str, schema: dict) -> dict:
    api_key = config.get_openai_api_key()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for live OpenAI structured-output calls.")

    payload = build_openai_structured_payload(model, prompt_text, schema)
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    prepared_request = request.Request(
        url="https://api.openai.com/v1/responses",
        data=body,
        headers=headers,
        method="POST",
    )

    try:
        with request.urlopen(prepared_request, timeout=30) as response:
            raw_response = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI request failed: HTTP {exc.code}: {error_body}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"OpenAI request failed: {exc.reason}") from exc

    if raw_response.get("refusal"):
        return {
            "refusal": raw_response["refusal"],
        }

    output_text = raw_response.get("output_text", "")
    if not output_text:
        raise RuntimeError("OpenAI response did not include output_text.")

    return json.loads(output_text)
