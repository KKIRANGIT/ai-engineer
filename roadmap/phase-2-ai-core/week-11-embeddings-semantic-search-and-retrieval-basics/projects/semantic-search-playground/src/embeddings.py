import json
from math import sqrt
from urllib import error, request

from src import config


TOPIC_KEYWORDS = {
    "billing": {"refund", "charged", "billing", "invoice", "charge", "payment"},
    "account_access": {"password", "sign", "login", "log", "account", "reset", "locked"},
    "reporting": {"report", "csv", "export", "spreadsheet", "download", "invoice"},
    "bug": {"crash", "upload", "error", "logs", "failed", "issue"},
    "feature_request": {"feature", "request", "dark", "mode", "improvement", "dashboard"},
}


def normalize_vector(values: list[float]) -> list[float]:
    norm = sqrt(sum(value * value for value in values))
    if norm == 0:
        return values
    return [value / norm for value in values]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


class MockEmbeddingClient:
    def embed_text(self, text: str) -> list[float]:
        text_lower = text.lower()
        vector = []

        for keywords in TOPIC_KEYWORDS.values():
            score = sum(text_lower.count(keyword) for keyword in keywords)
            vector.append(float(score))

        return normalize_vector(vector)


class OpenAIEmbeddingClient:
    def embed_text(self, text: str) -> list[float]:
        api_key = config.get_openai_api_key()
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is required for live embeddings.")

        payload = {
            "model": config.get_openai_embedding_model(),
            "input": text,
        }
        body = json.dumps(payload).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        prepared_request = request.Request(
            url="https://api.openai.com/v1/embeddings",
            data=body,
            headers=headers,
            method="POST",
        )

        try:
            with request.urlopen(prepared_request, timeout=30) as response:
                raw_response = json.loads(response.read().decode("utf-8"))
        except error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenAI embeddings request failed: HTTP {exc.code}: {error_body}") from exc
        except error.URLError as exc:
            raise RuntimeError(f"OpenAI embeddings request failed: {exc.reason}") from exc

        return raw_response["data"][0]["embedding"]


def build_embedding_client():
    if config.get_embedding_mode() == "live":
        return OpenAIEmbeddingClient()
    return MockEmbeddingClient()
