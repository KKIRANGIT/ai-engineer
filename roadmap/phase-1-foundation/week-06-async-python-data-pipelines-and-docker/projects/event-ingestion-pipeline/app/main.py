"""
CLI entry point for the Week 06 event ingestion pipeline.
"""

import asyncio

from app.config import get_event_scores_file, get_output_dir, get_raw_events_file
from app.data_loader import load_event_scores, load_raw_events
from app.pipeline import clean_and_enrich_events, write_cleaned_csv, write_summary_report
from app.reports import build_summary


async def run_pipeline():
    """Run the end-to-end pipeline asynchronously."""
    raw_events_file = get_raw_events_file()
    event_scores_file = get_event_scores_file()
    output_dir = get_output_dir()

    raw_events, score_mapping = await asyncio.gather(
        load_raw_events(raw_events_file),
        load_event_scores(event_scores_file),
    )

    cleaned_events = clean_and_enrich_events(raw_events, score_mapping)
    summary = build_summary(cleaned_events)

    write_cleaned_csv(cleaned_events, output_dir / "cleaned_events.csv")
    write_summary_report(summary, output_dir / "summary_report.json")

    return summary


def main():
    """Run the pipeline and print the summary."""
    summary = asyncio.run(run_pipeline())
    print("Pipeline summary:")
    print(summary)


if __name__ == "__main__":
    main()
