import json
from pathlib import Path

from src import config
from src.models import RegressionCase, Ticket


def load_prompt_template(template_name: str) -> str:
    template_path = config.get_prompt_library_path() / f"{template_name}.md"
    return template_path.read_text(encoding="utf-8")


def render_prompt(template_name: str, ticket_text: str) -> str:
    template = load_prompt_template(template_name)
    return template.format(ticket_text=ticket_text)


def load_tickets() -> list[Ticket]:
    raw_items = json.loads(config.get_sample_tickets_path().read_text(encoding="utf-8"))
    return [Ticket(**item) for item in raw_items]


def load_regression_cases() -> list[RegressionCase]:
    raw_items = json.loads(config.get_regression_cases_path().read_text(encoding="utf-8"))
    return [RegressionCase(**item) for item in raw_items]


def get_ticket_by_id(ticket_id: str) -> Ticket:
    for ticket in load_tickets():
        if ticket.ticket_id == ticket_id:
            return ticket
    raise ValueError(f"Unknown ticket_id: {ticket_id}")
