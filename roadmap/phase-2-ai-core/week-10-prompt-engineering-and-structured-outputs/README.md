# Week 10: Prompt Engineering and Structured Outputs

Back to [Phase 2](../README.md)

## Goal

Learn how to produce outputs that are not only fluent, but useful, reliable, and safely consumable by application code.

This week is about moving from prompt experimentation to prompt engineering.

## Why This Week Matters

Prompting is often taught too casually. Real prompt engineering is not:

- adding random instructions
- trying isolated prompt tricks without measurement
- treating output formatting as a matter of luck

Real prompt engineering means:

- clear task definition
- explicit success criteria
- controlled context
- schema-aware outputs
- known failure modes
- validation and regression habits

Structured outputs are one of the most practical AI engineering skills because downstream systems usually need valid data, not just nice prose.

## What This Week Is Really Training

At a deeper level, this week trains six important habits.

### 1. Prompting as specification design

You should learn to treat prompts as behavioral specifications:

- what the task is
- what the model should and should not do
- what the output must contain
- how ambiguity should be handled

### 2. Output contract thinking

The moment model output becomes application input, structure matters.

That means:

- stable fields
- typed values
- validation paths
- refusal handling

### 3. Decomposition discipline

Many weak prompts ask the model to do too much in one loose step.

This week should train you to separate:

- extraction from summarization
- classification from explanation
- evidence identification from conclusion generation

### 4. Regression mindset

Prompt changes should not be judged by vibes. You should start building the reflex of:

- keeping cases
- comparing variants
- recording failures

### 5. Failure-aware design

You must think beyond "best-case output." Real systems need to handle:

- missing fields
- unsupported inputs
- low-confidence cases
- safe refusals

### 6. Prompt library organization

Prompts should be stored, named, versioned, and compared like real engineering artifacts.

## Scope Boundary

This week is not for:

- full agent workflows
- external retrieval systems
- tool calling
- advanced eval automation
- production UI polish

This week is for:

- clear task prompts
- structured JSON outputs
- local validation
- prompt template organization
- small regression sets

## Week 10 Outcomes

By the end of this week, you should be able to:

- write clearer, more controllable prompts
- use decomposition and examples intentionally
- distinguish plain text generation from schema-constrained generation
- design JSON-schema outputs for real application tasks
- detect refusals and validation failures programmatically
- build a prompt library with reusable templates
- create a small regression set for prompt quality
- explain why structured outputs reduce downstream complexity

## Workspace Structure

This week now includes a full hands-on workspace:

```text
week-10-prompt-engineering-and-structured-outputs/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- prompt-clarity/
|   |   `-- 01_rewrite_vague_prompts.py
|   |-- decomposition-and-examples/
|   |   `-- 01_task_decomposition.py
|   |-- prompt-organization/
|   |   `-- 01_xml_and_sections.py
|   `-- structured-output-thinking/
|       |-- 01_schema_design_patterns.py
|       `-- 02_refusal_and_validation_review.py
|-- projects/
|   `-- support-ticket-triage-lab/
|       |-- README.md
|       |-- .env.example
|       |-- data/
|       |   |-- regression_cases.json
|       |   `-- sample_tickets.json
|       |-- prompt_library/
|       |   |-- classify_ticket_v1.md
|       |   |-- classify_ticket_v2_few_shot.md
|       |   `-- classify_ticket_v3_xml.md
|       |-- schemas/
|       |   `-- ticket_triage_schema.json
|       |-- src/
|       |   |-- __init__.py
|       |   |-- config.py
|       |   |-- main.py
|       |   |-- mock_engine.py
|       |   |-- models.py
|       |   |-- openai_structured_client.py
|       |   |-- prompt_library.py
|       |   |-- regression.py
|       |   `-- validators.py
|       `-- tests/
|           |-- test_openai_structured_client.py
|           |-- test_regression.py
|           |-- test_validators.py
|           `-- test_prompt_library.py
`-- notes/
    |-- 01-week-plan.md
    |-- 02-prompt-design-principles.md
    `-- 03-structured-output-checklist.md
```

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

Anthropic’s prompt guidance emphasizes clarity and directness before more specialized techniques. That is the right default.

You should learn to write:

- short but precise instructions
- explicit behavioral boundaries
- output requirements
- ambiguity-handling rules

Clarity usually beats decoration.

## 3. Few-shot prompting

Examples are often more powerful than more intense wording.

Use few-shot examples when:

- output shape matters
- subtle distinctions matter
- borderline cases matter
- you want to show the model what "good" looks like

Important rule:

Examples should be representative, not decorative.

## 4. Task decomposition

Many prompt failures come from asking the model to do too much in one loose step.

Learn when to:

- classify before explaining
- extract before summarizing
- identify evidence before writing a conclusion

This matters because structured tasks are usually easier to debug than blended tasks.

## 5. Roles, XML tags, and context organization

You should understand:

- when role framing helps
- when XML-like tags help separate context, examples, and instructions
- when excessive prompt decoration stops helping

Use tags when they improve clarity for:

- examples
- references
- required response sections

Do not use tags only because they look advanced.

## 6. Structured outputs and JSON schema

This is the central technical topic of the week.

You should learn:

- why schema-constrained output is safer than freeform parsing
- how to define JSON schema for an application response
- how structured output differs from simple "respond in JSON" prompting
- how to detect refusals and invalid generations cleanly

Current practical direction:

- OpenAI supports structured outputs against JSON schema in the Responses API
- structured outputs are preferred over older JSON mode when supported
- even with schema support, application validation still matters

## 7. Validation and application safety

Even with structured outputs, your application should still think about:

- required field presence
- enum correctness
- supported ranges
- missing information
- user-visible error handling

Structured generation reduces risk. It does not remove engineering responsibility.

## 8. Prompt regression testing

A prompt is part of your system. It should be tested like one.

Create a small regression set containing:

- easy cases
- ambiguous cases
- malformed input
- edge cases
- refusal-worthy or unsupported cases when appropriate

This is an early version of the eval mindset you will need later.

## Best Learning Sequence For This Week

Use this order:

1. clear instruction design
2. examples and decomposition
3. tagged prompt organization
4. structured outputs and schema design
5. validation logic
6. regression testing

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
- compare readability across prompt styles

### Day 4: Structured outputs

Focus:

- JSON schema thinking
- OpenAI structured output request shape

Build:

- one extraction or classification task with schema-constrained output

### Day 5: Validation and failure handling

Focus:

- invalid fields
- missing fields
- refusals

### Day 6: Prompt library organization

Focus:

- reusable template structure
- version naming
- prompt comparison

### Day 7: Regression set

Focus:

- define and run prompt cases
- compare output stability

## Main Project

The main project for this week is:

- [projects/support-ticket-triage-lab](projects/support-ticket-triage-lab/README.md)

It is intentionally practical:

- input is messy text from support tickets
- output must be structured and application-safe
- prompt variants can be compared
- regression cases can be run repeatedly

The project teaches:

- prompt template organization
- schema-driven output design
- structured output request construction
- local validation
- regression harness thinking

## Build Quality Standard

For this week, "the model returned JSON once" is not enough.

Minimum quality bar:

- prompts are named and reusable
- schema constraints are explicit
- outputs are validated
- failures are visible
- a regression set exists
- the README explains how prompt variants and structured outputs fit together

## Deliverables

By the end of this week, you should have:

- prompt clarity and decomposition exercises
- one prompt library with named variants
- one structured-output project
- a regression set
- notes on failure modes and prompt revisions

## Exit Criteria

You are ready to move on only if:

- you can write prompts with explicit constraints
- you can explain when examples help
- you can design a useful JSON schema for output
- you can validate structured outputs instead of trusting them blindly
- you have at least a minimal regression harness

## Common Mistakes To Avoid

- using formatting instructions instead of real schema support
- overcomplicating prompts before clarifying the task
- assuming a pretty response is a good response
- skipping unsupported or edge cases in prompt testing
- treating "respond in JSON" as equivalent to structured outputs

## Expert Notes That Matter Early

### Prompting is systems work

The prompt, the context, the schema, and the validation logic form one system.

### Structured outputs reduce downstream complexity

They are often more valuable than small gains in prose quality.

### Measure prompt changes

Without regression cases, prompt iteration becomes guesswork.

## Suggested Official References

Prioritize these official sources:

1. OpenAI Structured Outputs guide  
   https://platform.openai.com/docs/guides/structured-outputs?lang=javascript
2. OpenAI Responses API text format reference  
   https://platform.openai.com/docs/api-reference/responses
3. Anthropic prompting best practices  
   https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/system-prompts
4. Anthropic XML tag guidance  
   https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags

Use the official docs for correctness, but use this workspace as the place where the ideas become operational.

## Final Standard For This Week

The correct outcome of Week 10 is not:

"I know some prompt tricks."

The correct outcome is:

"I can specify tasks clearly, organize prompts deliberately, generate structured outputs against a schema, and test prompt behavior like part of a real application."
