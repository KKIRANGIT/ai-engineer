# Prompt Design Principles

Back to [Week 10](../README.md)

## Principle 1: Clarity before cleverness

A plain, explicit prompt usually beats a prompt that is trying to sound sophisticated.

## Principle 2: Examples are teaching tools

Few-shot examples are useful when they show:

- subtle distinctions
- edge-case handling
- exact shape expectations

Examples are weak when they are ornamental or repetitive.

## Principle 3: Prompt and schema work together

The prompt explains what the model should do.

The schema defines what the output is allowed to look like.

Neither one fully replaces the other.

## Principle 4: Validation is still required

Even with structured outputs, the application should still check:

- required fields
- enum membership
- unsupported or empty content
- refusal cases

## Principle 5: Prompt quality is a system property

The quality of a prompt depends on:

- the task
- the context
- the examples
- the output contract
- the model
- the failure handling

This is why Week 10 is systems work, not just wording work.
