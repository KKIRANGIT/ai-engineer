import asyncio
import tempfile
import unittest
from pathlib import Path

from app.data_loader import load_event_scores, load_raw_events
from app.models import RawEventRecord
from app.pipeline import clean_and_enrich_events, parse_duration
from app.reports import build_summary


class PipelineTests(unittest.TestCase):
    def test_parse_duration_returns_zero_for_invalid_value(self):
        self.assertEqual(parse_duration("not-a-number"), 0)
        self.assertEqual(parse_duration("25"), 25)

    def test_clean_and_enrich_events_builds_expected_output(self):
        raw_events = [
            RawEventRecord(" asha ", "watch_intro", "15", "DONE"),
            RawEventRecord("ravi", "review_notes", "bad", "pending"),
        ]
        score_mapping = {"watch_intro": 5, "review_notes": 3}

        cleaned_events = clean_and_enrich_events(raw_events, score_mapping)

        self.assertEqual(cleaned_events[0].user_name, "Asha")
        self.assertEqual(cleaned_events[0].score, 5)
        self.assertEqual(cleaned_events[1].duration_minutes, 0)

    def test_build_summary_counts_events(self):
        raw_events = [
            RawEventRecord("Asha", "watch_intro", "15", "done"),
            RawEventRecord("Ravi", "review_notes", "10", "pending"),
        ]
        score_mapping = {"watch_intro": 5, "review_notes": 3}
        cleaned_events = clean_and_enrich_events(raw_events, score_mapping)

        summary = build_summary(cleaned_events)

        self.assertEqual(summary["total_events"], 2)
        self.assertEqual(summary["completed_events"], 1)
        self.assertEqual(summary["total_score"], 8)

    def test_async_loaders_read_local_files(self):
        with tempfile.TemporaryDirectory() as temp_dir_name:
            temp_dir = Path(temp_dir_name)
            csv_file = temp_dir / "events.csv"
            json_file = temp_dir / "scores.json"

            csv_file.write_text(
                "user_name,event_name,duration_minutes,status\n"
                "Asha,watch_intro,15,done\n",
                encoding="utf-8",
            )
            json_file.write_text('{"watch_intro": 5}', encoding="utf-8")

            async def run_loaders():
                return await asyncio.gather(
                    load_raw_events(csv_file),
                    load_event_scores(json_file),
                )

            raw_events, score_mapping = asyncio.run(run_loaders())

            self.assertEqual(len(raw_events), 1)
            self.assertEqual(score_mapping["watch_intro"], 5)


if __name__ == "__main__":
    unittest.main()
