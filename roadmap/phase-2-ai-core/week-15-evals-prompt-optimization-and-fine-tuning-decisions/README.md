# Week 15: Evals, Prompt Optimization, and Fine-Tuning Decisions

Back to [Phase 2](../README.md)

## Goal

Learn how to improve AI systems with evidence instead of instinct, and learn how to decide whether a problem needs prompt changes, retrieval changes, tool changes, or fine-tuning.

## Why This Week Matters

This is the week that turns you from a demo-builder into a more credible AI engineer.

Without evals:

- prompt changes are guesswork
- RAG changes are guesswork
- fine-tuning decisions are guesswork
- regressions go unnoticed

Evals are what allow iteration to become engineering rather than taste.

## Week 15 Outcomes

By the end of this week, you should be able to:

- define measurable success criteria for an AI task
- build a small representative eval dataset
- compare system versions against the same test set
- reason about output quality using rubrics or programmatic checks
- explain when prompt engineering is enough
- explain when RAG or tool changes are the real fix
- explain when fine-tuning is justified

## What To Learn

## 1. Evals as the optimization foundation

Current official guidance from OpenAI emphasizes the optimization flywheel:

- build evals
- establish baseline
- improve prompt, context, or model
- re-run evals

That should become your core mental model.

## 2. Success criteria

Before you evaluate, define what "good" means.

Depending on the task, that may include:

- correctness
- faithfulness
- schema validity
- task completion
- citation accuracy
- classification precision
- tone or style adherence

Weak evals usually come from weak success criteria.

## 3. Golden datasets and representative cases

You need a small but representative set of test cases, not only easy happy paths.

Include:

- normal cases
- ambiguous cases
- adversarial or edge cases
- malformed inputs
- cases that previously failed

## 4. Human and automated grading

You should understand both:

- rubric-based human review
- automated graders or programmatic checks

Some aspects are easier to check programmatically:

- schema validity
- presence of required fields
- exact string matches

Some aspects may require more nuanced grading:

- faithfulness
- helpfulness
- completeness

## 5. Prompt optimization as one lever

Prompt changes can fix:

- unclear task framing
- missing examples
- output inconsistency
- weak refusal behavior

But prompt changes are not the fix for everything.

Important judgment:

- if the model lacks the right knowledge, retrieval may be the real fix
- if tool actions are wrong, tool design may be the real fix
- if formatting remains unstable across many cases, structured output or fine-tuning may be the real fix

## 6. Fine-tuning decision framework

Current OpenAI guidance frames fine-tuning as one part of a larger optimization system, not the first step.

Good reasons to consider fine-tuning:

- stable formatting needs at scale
- large example set that cannot fit easily in prompts
- domain-specific style or behavior
- cost or latency pressure that favors a smaller tuned model

Bad reasons:

- you have not built evals
- your retrieval is weak
- your prompt is still unclear
- you have not isolated the true failure pattern

## 7. Fine-tuning modes at a conceptual level

Know the high-level landscape:

- supervised fine-tuning
- preference optimization
- reinforcement-style optimization for harder tasks

You do not need to become a training expert this week. You do need to know what problems these methods are trying to solve.

## Best Learning Sequence For This Week

1. define success criteria
2. build eval dataset
3. create baseline
4. change one system variable
5. compare results
6. reason about whether fine-tuning is warranted

## Recommended Daily Breakdown

### Day 1: Define quality

Focus:

- choose one existing AI app from earlier weeks
- define what good looks like

### Day 2: Build eval set

Focus:

- create 15-30 representative test cases

### Day 3: Baseline run

Focus:

- run the current system
- capture failures

### Day 4: One improvement cycle

Focus:

- improve prompt, retrieval, or tool design
- re-run on the same cases

### Day 5: Scoring and analysis

Focus:

- compare before and after
- document which change helped

### Day 6: Fine-tuning decision analysis

Focus:

- ask whether this problem truly needs fine-tuning

### Day 7: Write the optimization report

Focus:

- summarize baseline, changes, and evidence

## Build Plan

Choose one earlier AI system and create:

- eval dataset
- scoring rubric
- baseline results
- one optimization iteration
- one decision memo on whether fine-tuning makes sense

Optional stretch:

- run a very small fine-tuning experiment only if your eval setup is already stable

## Deliverables

- one eval dataset
- one scoring rubric
- one baseline-vs-improved comparison
- one brief fine-tuning decision memo

## Exit Criteria

- you can define and measure success criteria
- you can compare AI system changes against the same dataset
- you no longer rely only on intuition when iterating
- you can explain when fine-tuning is or is not justified

## Common Mistakes To Avoid

- optimizing prompts without a baseline
- using only easy test cases
- changing too many variables at once
- jumping to fine-tuning before fixing context or retrieval issues

## Expert Notes That Matter Early

### Evals create engineering leverage

Once you can measure, you can improve faster and with less confusion.

### Fine-tuning is downstream of diagnosis

It should solve a known problem, not compensate for unclear system design.

### Small eval sets still matter

Even a 20-case test set is better than no evaluation discipline at all.

## Suggested Official References

- OpenAI agent evals guide
- OpenAI model optimization and fine-tuning guides
- Anthropic prompt-engineering guidance on empirical success criteria

## Final Standard For This Week

The correct outcome of Week 15 is not "I learned what evals are."

The correct outcome is:

"I can measure AI-system quality, improve it in a controlled way, and make evidence-based decisions about prompts, retrieval, tools, and fine-tuning."
