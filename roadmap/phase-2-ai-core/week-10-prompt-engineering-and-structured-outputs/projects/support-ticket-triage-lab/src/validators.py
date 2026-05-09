import json

from src import config


class ValidationError(Exception):
    def __init__(self, errors: list[str]) -> None:
        super().__init__("Structured output validation failed.")
        self.errors = errors


def load_schema() -> dict:
    return json.loads(config.get_schema_path().read_text(encoding="utf-8"))


def validate_structured_output(payload: dict) -> None:
    schema = load_schema()
    errors = []

    required_fields = schema.get("required", [])
    for field_name in required_fields:
        if field_name not in payload:
            errors.append(f"Missing required field: {field_name}")

    allowed_fields = set(schema.get("properties", {}).keys())
    if schema.get("additionalProperties") is False:
        extra_fields = set(payload.keys()) - allowed_fields
        for field_name in sorted(extra_fields):
            errors.append(f"Unexpected field: {field_name}")

    for field_name, field_definition in schema.get("properties", {}).items():
        if field_name not in payload:
            continue

        value = payload[field_name]
        field_type = field_definition.get("type")

        if field_type == "string" and not isinstance(value, str):
            errors.append(f"Field {field_name} must be a string")
        elif field_type == "boolean" and not isinstance(value, bool):
            errors.append(f"Field {field_name} must be a boolean")

        allowed_values = field_definition.get("enum")
        if allowed_values and value not in allowed_values:
            errors.append(f"Field {field_name} must be one of {allowed_values}")

    if errors:
        raise ValidationError(errors)
