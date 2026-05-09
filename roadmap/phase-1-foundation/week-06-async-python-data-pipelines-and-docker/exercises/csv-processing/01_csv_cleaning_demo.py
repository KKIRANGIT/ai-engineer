"""
Week 06 - CSV Processing: Clean rows before using them
"""

import csv
from io import StringIO

RAW_CSV_TEXT = """user_name,event_name,duration_minutes,status
Asha,watch_intro,15,done
Ravi,watch_intro,,done
Neha,build_demo,45,done
Om,review_notes,not-a-number,pending
"""


def clean_duration(raw_duration):
    """Convert the duration to an integer, or return 0 when invalid."""
    try:
        return int(raw_duration)
    except ValueError:
        return 0


def parse_and_clean_rows(csv_text):
    """Read CSV rows and normalize selected fields."""
    input_stream = StringIO(csv_text)
    reader = csv.DictReader(input_stream)
    cleaned_rows = []

    for row in reader:
        cleaned_rows.append(
            {
                "user_name": row["user_name"].strip(),
                "event_name": row["event_name"].strip(),
                "duration_minutes": clean_duration(row["duration_minutes"]),
                "status": row["status"].strip().lower(),
            }
        )

    return cleaned_rows


def main():
    """Run the small CSV cleaning demonstration."""
    cleaned_rows = parse_and_clean_rows(RAW_CSV_TEXT)
    for row in cleaned_rows:
        print(row)


if __name__ == "__main__":
    main()
