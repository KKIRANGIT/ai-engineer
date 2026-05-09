from pathlib import Path
from wsgiref.simple_server import make_server

from src.app import create_app
from src.config import get_database_path, get_host, get_port
from src.db import initialize_database
from src.repository import StudyTrackerRepository
from src.service import StudyTrackerService


def main() -> None:
    database_path = get_database_path()
    initialize_database(database_path)

    repository = StudyTrackerRepository(database_path)
    service = StudyTrackerService(repository)
    static_directory = Path(__file__).resolve().parent / "static"
    app = create_app(service, static_directory)

    host = get_host()
    port = get_port()

    with make_server(host, port, app) as server:
        print(f"Study Session Tracker running at http://{host}:{port}")
        print(f"Database path: {database_path}")
        server.serve_forever()


if __name__ == "__main__":
    main()
