# Week 15: Evals, Prompt Optimization, and Fine-Tuning Decisions

Back to [Phase 2](../README.md)

## Goal

Learn how to improve AI systems with evidence instead of instinct, and learn how to decide whether a problem needs prompt changes, retrieval changes, tool changes, or fine-tuning.

This is the week where iteration stops being "I changed something and it felt better" and starts becoming measurement-driven engineering.

## Why This Week Matters

Without evals:

- prompt changes are guesswork
- RAG changes are guesswork
- tool changes are guesswork
- model swaps are guesswork
- fine-tuning decisions are guesswork
- regressions go unnoticed

Evals are what turn iteration into a reproducible optimization loop.

## What This Week Is Actually Training

Week 15 is training five deeper skills:

1. defining success criteria before optimizing
2. building representative datasets instead of relying on happy-path examples
3. grading outputs with explicit checks and rubrics
4. comparing versions against the same cases
5. deciding which lever to pull next based on failure patterns

The real outcome is not just "I know what evals are." The real outcome is "I know how to diagnose an AI system."

## Scope Boundary For This Week

This week focuses on:

- eval datasets
- graders and rubrics
- regression testing
- prompt and retrieval comparisons
- baseline vs improved analysis
- fine-tuning decision logic

This week does not require:

- training a real fine-tuned model
- building large-scale eval infrastructure
- external judge models
- production monitoring systems

The correct first goal is not "fine-tune something." The correct first goal is "build enough measurement discipline to know whether tuning is even justified."

## Week 15 Outcomes

By the end of this week, you should be able to:

- define measurable success criteria for an AI task
- build a small representative eval dataset
- compare multiple system versions against the same cases
- reason about output quality using programmatic checks and simple rubrics
- explain when prompt engineering is enough
- explain when retrieval or tool design is the real fix
- explain when fine-tuning is justified and when it is premature

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 15 workspace
2. official provider docs for current eval and optimization guidance
3. your own results, failure notes, and comparison reports

Do not jump straight into fine-tuning tutorials. This week should strengthen diagnosis before optimization complexity.

## Recommended Official References

Primary sources:

- OpenAI Agent Evals guide: <https://platform.openai.com/docs/guides/agent-evals>
- OpenAI Model Optimization guide: <https://platform.openai.com/docs/guides/fine-tuning>
- OpenAI Supervised Fine-Tuning guide: <https://platform.openai.com/docs/guides/supervised-fine-tuning>
- OpenAI Fine-Tuning Best Practices: <https://platform.openai.com/docs/guides/fine-tuning-best-practices>
- OpenAI Reinforcement Fine-Tuning guide: <https://platform.openai.com/docs/guides/reinforcement-fine-tuning>
- Anthropic Evaluation Tool: <https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool>
- Anthropic empirical evaluation guidance: <https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests>
- Anthropic prompt engineering overview: <https://docs.anthropic.com/en/docs/prompt-engineering>

These references were chosen because evals and fine-tuning guidance are time-sensitive and provider recommendations evolve.

## Core Mental Models

## 1. Evals are the optimization foundation

Current official guidance from OpenAI emphasizes an optimization flywheel:

1. build evals
2. establish a baseline
3. improve prompt, context, tools, retrieval, or model
4. re-run the same evals
5. compare results

That should become your default mental model.

## 2. Success criteria come before grading

Before you evaluate, define what "good" means.

Depending on the task, that may include:

- correctness
- grounding or faithfulness
- schema validity
- task completion
- classification precision
- required-field coverage
- tone or response policy adherence

Weak evals almost always come from weak success criteria.

## 3. Golden datasets should be representative

You need a small but representative set of test cases, not only easy happy paths.

Include:

- normal cases
- ambiguous cases
- edge cases
- malformed or noisy inputs
- cases that previously failed

The goal is not dataset size for its own sake. The goal is meaningful coverage.

## 4. Human and automated grading each have a role

You should understand both:

- rubric-based human review
- automated graders or programmatic checks

Some things are easy to grade programmatically:

- schema validity
- exact labels
- presence of required fields
- simple policy phrase checks

Some things are harder and may need rubric logic or human review:

- faithfulness
- nuance
- prioritization judgment
- overall helpfulness

## 5. Prompt engineering is only one lever

Prompt changes can fix:

- unclear task framing
- missing output instructions
- inconsistent formatting
- weak refusal behavior
- lack of decomposition

But prompt changes are not the fix for everything.

Important judgment:

- if the model lacks the right knowledge, retrieval may be the real fix
- if tool actions are wrong, tool design may be the real fix
- if formatting remains unstable across many cases, structured output or fine-tuning may be the real fix

## 6. Fine-tuning should follow diagnosis

Current OpenAI guidance treats fine-tuning as one part of a larger optimization system, not the default first move.

Good reasons to consider fine-tuning:

- stable formatting needs at scale
- many examples that cannot fit well into prompts
- domain-specific style or behavior
- cost or latency pressure that favors a smaller tuned model
- instruction-following behavior that remains inconsistent after prompt and context improvements

Bad reasons:

- you have not built evals
- your retrieval is weak
- your prompt is still unclear
- you have not isolated the failure pattern

## Best Learning Sequence For This Week

1. define success criteria
2. build an eval dataset
3. create a baseline
4. change one system variable
5. compare results
6. reason about whether fine-tuning is warranted

## Recommended Daily Breakdown

### Day 1: Define quality

Focus:

- choose a concrete AI task
- define what good looks like

### Day 2: Build the eval set

Focus:

- create representative cases
- include edge cases and previous failures

### Day 3: Baseline run

Focus:

- run the current system
- capture failures

### Day 4: Improvement cycle

Focus:

- improve one lever such as prompt or retrieval
- re-run the same dataset

### Day 5: Scoring and analysis

Focus:

- compare before and after
- identify which change actually helped

### Day 6: Fine-tuning decision analysis

Focus:

- ask whether the remaining failures truly justify tuning

### Day 7: Write the optimization report

Focus:

- summarize baseline, changes, grading, and evidence

## Hands-On Workspace Structure

```text
week-15-evals-prompt-optimization-and-fine-tuning-decisions/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- dataset-design/
|   |-- fine-tuning-decisions/
|   |-- graders-and-regressions/
|   `-- success-criteria/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-eval-design-checklist.md
|   `-- 03-fine-tuning-decision-framework.md
`-- projects/
    `-- ticket-triage-eval-lab/
```

## Exercises

The exercises isolate the main evaluation concepts before the larger project combines them.

You will practice:

- defining measurable success criteria
- designing good eval sets
- comparing weak and strong graders
- interpreting failure patterns
- deciding when fine-tuning is or is not justified

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [ticket-triage-eval-lab](projects/ticket-triage-eval-lab/README.md)

This project is a local eval harness for a support-ticket triage task. It compares several system versions:

- `baseline`
- `prompt_v2`
- `retrieval_v1`

It includes:

- a representative eval dataset
- programmatic graders
- aggregate score reporting
- case-level regression analysis
- a decision memo that recommends prompt, retrieval, or fine-tuning next steps

The project is intentionally local-first and deterministic so the eval mechanics stay visible.

## Build Plan

Build and study one evaluation harness that can:

- load a small dataset of ticket cases
- run multiple system versions against the same cases
- grade outputs consistently
- compare aggregated results
- explain which optimization lever seems justified next

Required qualities:

- readable dataset
- explicit graders
- baseline vs improved comparison
- failure inspection
- fine-tuning decision support

## Suggested Study Order Inside This Week

1. read this README fully
2. complete the exercises
3. read the project README
4. run the baseline version
5. run the improved versions
6. compare the reports
7. read the notes after you have seen the outputs

## Deliverables

By the end of Week 15, you should have:

- completed the exercises
- run an eval dataset across multiple versions
- inspected case-level failures
- compared baseline and improved scores
- written your own explanation of why the next step should be prompt work, retrieval work, or fine-tuning

## Exit Criteria

You should not leave Week 15 until you can:

- define success criteria before you optimize
- explain why a dataset should include edge cases
- show how your grader works
- compare multiple system versions against the same cases
- explain at least one failure pattern that points to prompt, retrieval, or fine-tuning
- justify why fine-tuning is or is not the right next step

## Common Mistakes To Avoid

- optimizing prompts without a baseline
- using only easy test cases
- changing too many variables at once
- confusing overall intuition with measured improvement
- jumping to fine-tuning before fixing context or retrieval issues
- treating one or two examples as proof of improvement

## Expert Notes That Matter Early

### Evals create engineering leverage

Once you can measure, you can improve faster and with less confusion.

### Fine-tuning is downstream of diagnosis

It should solve a known problem, not compensate for unclear system design.

### Small eval sets still matter

Even a 15-30 case set is far better than no evaluation discipline at all.

### Aggregate scores are not enough

Always inspect representative failures. A higher average score can still hide an important regression.

## Final Standard For This Week

The correct outcome of Week 15 is not:

"I learned what evals are."

The correct outcome is:

"I can measure AI-system quality, improve it in a controlled way, and make evidence-based decisions about prompts, retrieval, tools, and fine-tuning."
