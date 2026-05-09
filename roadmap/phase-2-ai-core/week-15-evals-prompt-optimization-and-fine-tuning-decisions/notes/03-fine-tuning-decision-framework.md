# Fine-Tuning Decision Framework

Back to [Week 15 README](../README.md)

## Why This Note Exists

Many learners ask "Should I fine-tune?" too early.

The better question is:

"What failure pattern is left after prompt, retrieval, and tool improvements?"

## Start With These Checks

### Prompt-first checks

- Are instructions clear?
- Is the output contract explicit?
- Did examples improve results?
- Are failures mostly formatting or task-framing issues?

If yes, keep working on prompts first.

### Retrieval or context checks

- Does the system lack needed knowledge?
- Are policy or factual failures common?
- Do answers improve when better evidence is present?

If yes, fix retrieval or context before tuning.

### Tool and workflow checks

- Are actions wrong because the system used the wrong tool?
- Is the workflow missing validation?
- Are outputs correct only when the orchestration path is correct?

If yes, fix system design before tuning.

### Fine-tuning checks

Consider fine-tuning when:

- failures remain consistent across many examples
- the desired behavior is stable and teachable
- prompt and context improvements are no longer enough
- latency or cost pressures favor a smaller tuned model

## Practical Week 15 Rule

If you cannot clearly describe the remaining failure pattern, you are not ready to fine-tune.
