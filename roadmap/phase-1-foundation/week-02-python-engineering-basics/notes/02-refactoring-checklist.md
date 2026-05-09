# Refactoring Checklist

Use this checklist whenever you improve a small Python project.

- Does each file have one main responsibility?
- Is user input handling separate from core logic?
- Is file storage separate from task manipulation logic?
- Are invalid inputs rejected early?
- Are error messages understandable?
- Can at least some logic be tested without running the CLI?
- Are data shapes explicit?
- Are names clear enough that comments are minimal?
- Does the project folder explain itself at a glance?

If several answers are "no," the structure is not stable enough yet.
