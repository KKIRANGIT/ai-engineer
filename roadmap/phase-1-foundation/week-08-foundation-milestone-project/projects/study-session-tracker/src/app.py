import json
from pathlib import Path

from src.response_utils import json_response
from src.static_handler import serve_static_file
from src.validation import ValidationError


def read_json_body(environ) -> dict:
    content_length = int(environ.get("CONTENT_LENGTH") or 0)
    raw_body = environ["wsgi.input"].read(content_length).decode("utf-8")

    if not raw_body.strip():
        return {}

    return json.loads(raw_body)


def create_app(service, static_directory: Path):
    def application(environ, start_response):
        method = environ["REQUEST_METHOD"]
        path = environ.get("PATH_INFO", "/")

        try:
            if method == "GET" and path == "/api/health":
                return json_response(start_response, "200 OK", {"status": "ok", "service": "study-session-tracker"})

            if method == "GET" and path == "/api/subjects":
                return json_response(start_response, "200 OK", {"data": service.list_subjects()})

            if method == "POST" and path == "/api/subjects":
                payload = read_json_body(environ)
                subject = service.create_subject(payload)
                return json_response(start_response, "201 Created", {"data": subject})

            if method == "GET" and path == "/api/sessions":
                return json_response(start_response, "200 OK", {"data": service.list_sessions()})

            if method == "POST" and path == "/api/sessions":
                payload = read_json_body(environ)
                session = service.create_session(payload)
                return json_response(start_response, "201 Created", {"data": session})

            if method == "GET" and path == "/api/summary":
                return json_response(start_response, "200 OK", {"data": service.get_summary()})

            if method == "DELETE" and path.startswith("/api/sessions/"):
                session_id = int(path.rsplit("/", maxsplit=1)[-1])
                deleted = service.delete_session(session_id)

                if not deleted:
                    return json_response(
                        start_response,
                        "404 Not Found",
                        {
                            "error": "Request Error",
                            "message": "Session not found.",
                            "details": [],
                        },
                    )

                return json_response(start_response, "200 OK", {"message": "Session deleted."})

            if path == "/" or path.startswith("/static/"):
                return serve_static_file(start_response, static_directory, path)

            return json_response(
                start_response,
                "404 Not Found",
                {"error": "Request Error", "message": "Route not found.", "details": []},
            )
        except ValidationError as error:
            return json_response(
                start_response,
                "400 Bad Request",
                {
                    "error": "Request Error",
                    "message": error.message,
                    "details": error.errors,
                },
            )
        except ValueError:
            return json_response(
                start_response,
                "400 Bad Request",
                {
                    "error": "Request Error",
                    "message": "Request data could not be processed.",
                    "details": [],
                },
            )
        except Exception as error:
            return json_response(
                start_response,
                "500 Internal Server Error",
                {
                    "error": "Server Error",
                    "message": str(error),
                    "details": [],
                },
            )

    return application
