"""
Week 06 - Pipeline Thinking: Stages before cleverness
"""


def ingest(raw_rows):
    """Stage 1: accept incoming raw records."""
    return raw_rows


def validate(rows):
    """Stage 2: keep only rows with a minimum required shape."""
    valid_rows = []

    for row in rows:
        if row.get("user_name") and row.get("event_name"):
            valid_rows.append(row)

    return valid_rows


def normalize(rows):
    """Stage 3: normalize field formatting."""
    normalized_rows = []

    for row in rows:
        normalized_rows.append(
            {
                "user_name": row["user_name"].strip().title(),
                "event_name": row["event_name"].strip().lower(),
            }
        )

    return normalized_rows


def main():
    """Demonstrate a clear stage-by-stage pipeline."""
    raw_rows = [
        {"user_name": " asha ", "event_name": "Watch_Intro"},
        {"user_name": "", "event_name": "review_notes"},
    ]

    rows = ingest(raw_rows)
    rows = validate(rows)
    rows = normalize(rows)

    print("Pipeline output:", rows)


if __name__ == "__main__":
    main()
