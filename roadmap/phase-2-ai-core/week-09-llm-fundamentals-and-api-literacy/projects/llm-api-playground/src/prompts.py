DEFAULT_INSTRUCTIONS = (
    "You are a careful AI engineering study assistant. "
    "Explain concepts clearly, avoid hype, and prefer practical language."
)


def build_default_prompt(task: str) -> str:
    return task.strip()
