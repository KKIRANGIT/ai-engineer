import json
from urllib import error, request


class HTTPRequestError(Exception):
    """Raised when an HTTP provider request fails."""


def post_json(url: str, headers: dict[str, str], payload: dict, timeout_seconds: int) -> dict:
    body = json.dumps(payload).encode("utf-8")
    prepared_request = request.Request(url=url, data=body, headers=headers, method="POST")

    try:
        with request.urlopen(prepared_request, timeout=timeout_seconds) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise HTTPRequestError(f"HTTP {exc.code}: {error_body}") from exc
    except error.URLError as exc:
        raise HTTPRequestError(f"Network error: {exc.reason}") from exc
