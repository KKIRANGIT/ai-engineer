# Week 10: Prompt Engineering and Structured Outputs

Back to [Phase 2](../README.md)

## Goal

Learn how to produce outputs that are not only fluent, but useful, reliable, and safely consumable by application code.

This week is about moving from prompt experimentation to prompt engineering.

## Why This Week Matters

Prompting is often taught too casually. Real prompt engineering is not:

- adding random instructions
- trying ten prompt tricks without measurement
- treating output formatting as a matter of luck

Real prompt engineering means:

- clear task definition
- explicit success criteria
- controlled context
- schema-aware outputs
- known failure modes

Structured outputs are now one of the most important practical skills in AI application development because downstream systems often need valid data, not just nice prose.

## Week 10 Outcomes

By the end of this week, you should be able to:

- write clearer, more controllable prompts
- use decomposition and examples intentionally
- distinguish plain text generation from schema-constrained generation
- design JSON-schema outputs for real application tasks
- detect refusals and validation failures programmatically
- build a prompt library with testable templates
- create a small regression set for prompt quality

## What To Learn

## 1. Prompt engineering as specification design

Treat prompts as task specifications.

Good prompt design defines:

- the task
- the role
- the constraints
- the expected output shape
- what success and failure look like

Weak prompt design says:

- "please be smart and figure it out"

Strong prompt design says:

- here is the task
- here is the context
- here is the format
- here is how to behave on ambiguity

## 2. Clear instructions first

Anthropic's guidance emphasizes clarity and directness before more specialized techniques. That is the right starting point.

You should learn to write:

- short but precise instructions
- explicit behavioral boundaries
- output requirements
- ambiguity handling rules

## 3. Few-shot prompting

Examples are often more powerful than stronger wording.

Use few-shot examples when:

- output shape matters
- subtle task distinctions matter
- edge-case behavior matters

Important rule:

Examples should be representative, not decorative.

## 4. Task decomposition

Many prompt failures come from asking the model to do too much in one unstructured step.

Learn when to:

- separate classification from generation
- extract before summarizing
- identify evidence before drafting a conclusion

This matters because structure often improves both reliability and debuggability.

## 5. Roles, XML tags, and context organization

You should understand:

- when role framing helps
- when XML or tagged sections help organize complex prompts
- when excessive prompt decoration stops helping

Use tags when they improve clarity for:

- examples
- reference material
- required response sections

Do not use tags just because they look advanced.

## 6. Structured outputs and JSON schema

This is the central technical topic of the week.

You should learn:

- why schema-constrained output is safer than freeform parsing
- how to define JSON schema for an application response
- how structured output differs from simple "respond in JSON" prompting
- how to detect refusals and invalid generations cleanly

Current practical direction:

- OpenAI supports structured outputs against JSON schema
- SDK helpers can make schema handling easier using typed models

## 7. Validation and application safety

Even with structured outputs, your application should still think about:

- field presence
- enum correctness
- missing information
- user-visible error handling

Structured generation reduces risk. It does not eliminate engineering responsibility.

## 8. Prompt regression testing

A prompt is part of your system. It should be tested like one.

Create a small regression set containing:

- easy cases
- ambiguous cases
- malformed input
- edge cases
- refusal-worthy cases where appropriate

This is the first step toward the eval mindset of Week 15.

## Best Learning Sequence For This Week

1. clear instructions
2. examples and decomposition
3. tagged prompt organization
4. structured outputs
5. validation logic
6. regression test set

## Recommended Daily Breakdown

### Day 1: Prompt clarity fundamentals

Focus:

- rewrite vague prompts into precise prompts
- define success criteria

### Day 2: Examples and decomposition

Focus:

- few-shot patterns
- multi-step task splitting

### Day 3: Tagged prompt structure

Focus:

- organize long prompts cleanly
- compare readability and performance

### Day 4: Structured outputs

Focus:

- JSON schema thinking
- provider-specific structured generation support

Build:

- one extraction task with schema-constrained output

### Day 5: Validation and failure handling

Focus:

- invalid fields
- missing fields
- refusals

### Day 6: Prompt library

Focus:

- reusable template structure
- prompt naming and organization

### Day 7: Regression set

Focus:

- define 15-20 cases
- compare prompt variants

## Build Plan

Build three artifacts:

### 1. Prompt template library

Organize by task type:

- extraction
- classification
- summarization
- transformation
- tool-routing or decision support

### 2. Structured extraction tool

Choose one task such as:

- meeting note extraction
- resume parsing
- support ticket labeling
- invoice field extraction

Use schema-constrained output rather than naive JSON prompting.

### 3. Prompt regression set

Create:

- test inputs
- expected properties
- failure notes

## Deliverables

- prompt template library
- one structured-output tool
- 15-20 prompt regression cases
- notes on failure modes and prompt revisions

## Exit Criteria

- you can write prompts with explicit constraints
- you can choose when examples are needed
- you can design a useful JSON schema for output
- your outputs are stable enough to drive code
- you have at least a minimal regression set

## Common Mistakes To Avoid

- using formatting instructions instead of real schema support
- overcomplicating prompts before clarifying the task
- assuming a pretty response is a good response
- skipping edge-case cases in prompt testing

## Expert Notes That Matter Early

### Prompting is systems work

The prompt, the context, the schema, and the validation logic are one system.

### Structured outputs reduce downstream complexity

They are often worth more than small gains in prose quality.

### Measure prompt changes

Without a regression set, prompt iteration becomes guesswork.

## Suggested Official References

- OpenAI structured outputs guide
- Anthropic prompt engineering overview

## Final Standard For This Week

The correct outcome of Week 10 is not "I know prompt tricks."

The correct outcome is:

"I can specify tasks clearly, generate reliable structured outputs, and test prompt behavior like part of a real application."
