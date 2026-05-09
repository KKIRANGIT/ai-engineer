from dataclasses import asdict

from src.mock_engine import classify_ticket
from src.models import RegressionOutcome
from src.prompt_library import get_ticket_by_id, load_regression_cases
from src.validators import ValidationError, validate_structured_output


def run_mock_regression() -> list[RegressionOutcome]:
    outcomes = []

    for case in load_regression_cases():
        ticket = get_ticket_by_id(case.ticket_id)
        result = asdict(classify_ticket(ticket))
        failures = []

        try:
            validate_structured_output(result)
        except ValidationError as error:
            failures.extend(error.errors)

        for field_name, expected_value in case.expected.items():
            actual_value = result.get(field_name)
            if actual_value != expected_value:
                failures.append(
                    f"{field_name} expected {expected_value!r} but got {actual_value!r}"
                )

        outcomes.append(
            RegressionOutcome(
                ticket_id=case.ticket_id,
                passed=len(failures) == 0,
                failures=failures,
                result=result,
            )
        )

    return outcomes
