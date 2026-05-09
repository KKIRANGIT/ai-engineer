"""
Database setup helpers for the Week 05 project tracker.
"""

import os
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = PROJECT_ROOT / "data" / "project_tracker.db"
SCHEMA_FILE = PROJECT_ROOT / "sql" / "schema.sql"
SEED_FILE = PROJECT_ROOT / "sql" / "seed.sql"


def get_database_path():
    """Return the configured database path or the default local file."""
    override_value = os.getenv("PROJECT_TRACKER_DB_PATH", "").strip()

    if not override_value:
        return DEFAULT_DB_PATH

    override_path = Path(override_value).expanduser()

    if not override_path.is_absolute():
        override_path = Path.cwd() / override_path

    return override_path


def connect(db_path=None):
    """Create a database connection with row access by column name."""
    target_path = Path(db_path) if db_path else get_database_path()
    target_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(target_path)
    connection.row_factory = sqlite3.Row

    # SQLite keeps foreign-key checks off by default, so turn them on explicitly.
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database(connection):
    """Create the schema from the schema.sql file."""
    schema_sql = SCHEMA_FILE.read_text(encoding="utf-8")
    connection.executescript(schema_sql)


def seed_database(connection):
    """Load the starter data from seed.sql."""
    seed_sql = SEED_FILE.read_text(encoding="utf-8")
    connection.executescript(seed_sql)
