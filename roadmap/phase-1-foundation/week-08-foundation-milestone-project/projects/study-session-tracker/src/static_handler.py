from pathlib import Path

from src.response_utils import text_response


CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
}


def serve_static_file(start_response, static_directory: Path, requested_path: str):
    relative_path = "index.html" if requested_path == "/" else requested_path.removeprefix("/static/")
    file_path = static_directory / relative_path

    if not file_path.exists() or not file_path.is_file():
        return text_response(start_response, "404 Not Found", "Static file not found.")

    content_type = CONTENT_TYPES.get(file_path.suffix, "text/plain; charset=utf-8")
    return text_response(start_response, "200 OK", file_path.read_text(encoding="utf-8"), content_type)
