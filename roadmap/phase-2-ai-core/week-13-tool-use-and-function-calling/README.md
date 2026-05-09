# Week 13: Tool Use and Function Calling

Back to [Phase 2](../README.md)

## Goal

Learn how to let a model take structured actions through software interfaces instead of only generating text.

This is the week where your AI systems stop being passive responders and start becoming controlled application components.

## Why This Week Matters

A large percentage of useful AI applications depend on tool use rather than raw text generation alone. The model often needs to:

- look up current or internal state
- search knowledge bases
- inspect tickets, tasks, or CRM records
- run deterministic calculations
- return structured decisions that application code can trust

If you do not understand tool use, you will keep building systems that sound capable but cannot reliably act.

If you do understand tool use, you can build:

- support copilots
- operations assistants
- workflow automation features
- research assistants with real data access
- product features that mix reasoning with software execution

## What This Week Is Actually Training

Week 13 is not mainly about memorizing one provider's JSON shape. It is training five deeper capabilities:

1. translating user intent into safe action boundaries
2. designing tool interfaces the model can use correctly
3. validating model-produced arguments before execution
4. tracing multi-step tool loops so failures are inspectable
5. separating deterministic application work from model judgment

That distinction matters. Strong Week 13 work makes Week 14 much easier, because many so-called "agents" are just badly designed tool loops with poor visibility.

## Scope Boundary For This Week

This week focuses on:

- function or tool schemas
- tool-result loops
- validation
- execution boundaries
- local inspectable tool systems
- provider payload literacy

This week does not require:

- autonomous browser control
- long-running background agents
- multi-agent planning
- full hosted tool integration against live APIs

The correct first step is not "make an agent." The correct first step is "make tool use understandable and safe."

## Week 13 Outcomes

By the end of this week, you should be able to:

- explain the full tool-calling loop from model request to final answer
- design high-quality tool schemas with clear descriptions and inputs
- distinguish client-side tools from provider-hosted tools
- validate model-generated arguments before running any tool
- log tool choice, arguments, results, and failures
- build one assistant with multiple tools and traceable behavior
- explain when a tool should exist and when plain application logic is better

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 13 workspace
2. official provider docs for current API shapes
3. your own traces and experiments

Do not jump between random blog posts for tool use. This topic becomes confusing fast when the vocabulary is inconsistent.

## Recommended Official References

Primary sources:

- OpenAI Responses API overview: <https://platform.openai.com/docs/api-reference/responses>
- OpenAI function calling guide: <https://platform.openai.com/docs/guides/function-calling?api-mode=responses&lang=python>
- OpenAI tools guide: <https://platform.openai.com/docs/guides/tools?api-mode=responses>
- OpenAI Responses migration guidance: <https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses.html>
- Anthropic tool use overview: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview>
- Anthropic implementation guide: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use>

These references were chosen because tool use is highly time-sensitive and provider semantics change.

## Tool-Use Mental Model

The core loop is:

1. the application sends the user goal and available tools
2. the model decides whether a tool is needed
3. the model emits one or more structured tool calls
4. the application validates each requested call
5. the application executes allowed tools
6. the application returns tool outputs to the model or a response composer
7. the system produces a final user-facing answer

Important rule:

The model never directly executes business logic. Your application does.

This is the main safety boundary of the pattern.

## What To Learn

## 1. Tool interfaces are part prompt design and part software design

The tool definition teaches the model what exists, when to use it, and how arguments should be shaped.

Weak tool definitions usually create:

- wrong tool choice
- missing arguments
- vague queries
- invalid parameters
- extra repair logic in your application

Strong tool definitions reduce ambiguity before execution starts.

## 2. A tool description is not metadata fluff

For real systems, the tool description should explain:

- what the tool does
- when the tool should be used
- when it should not be used
- what each parameter means
- important limits and failure conditions

This is one of the highest-leverage parts of tool performance.

## 3. Validation is mandatory

Never assume the model's requested arguments are safe or complete.

Validate:

- required fields
- field types
- numeric ranges
- enum-like values
- permission boundaries
- execution preconditions

A tool loop without validation is just prompt-shaped trust.

## 4. Hosted tools and client tools solve different problems

Hosted tools are useful when you want:

- less implementation work
- platform-native retrieval or search
- provider-managed execution for supported capabilities

Client tools are useful when you want:

- exact control over data access
- domain-specific logic
- custom safety rules
- deterministic behavior around internal systems

Expert-level thinking means choosing intentionally, not assuming one category is always better.

## 5. Tool traces are a first-class debugging asset

You need to be able to inspect:

- which tool was selected
- why it was selected
- what arguments were requested
- what validation changed or rejected
- what output was returned
- how the final answer used the result

Without traceability, tool-enabled systems become difficult to improve honestly.

## 6. Multiple tools do not automatically mean "agent"

Many tasks only need:

- a small tool set
- an explicit loop
- sequential execution
- readable traces

You should be able to build strong tool systems before adding extra orchestration layers.

## Best Learning Sequence For This Week

1. understand the tool loop
2. design strong schemas
3. add validation and safety checks
4. compare provider payload formats
5. build a multi-tool assistant
6. inspect traces and failure cases

## Recommended Daily Breakdown

### Day 1: Tool-call fundamentals

Focus:

- the model/application boundary
- tool calls versus plain text answers
- why tool outputs should be deterministic when possible

### Day 2: Schema design

Focus:

- names, descriptions, and input fields
- strong versus weak parameter definitions
- limiting tool scope on purpose

### Day 3: Validation layer

Focus:

- required arguments
- type checks
- business limits
- safe failures

### Day 4: Provider literacy

Focus:

- OpenAI function tools in the Responses API
- Anthropic client tools and tool results
- hosted tools versus local tools

### Day 5: Build the assistant loop

Focus:

- planner or model output
- validation
- execution
- result composition

### Day 6: Failure analysis and traces

Focus:

- invalid calls
- ambiguous requests
- unnecessary tool use
- understanding the trace file

### Day 7: Review and explain

Focus:

- explain the architecture in your own words
- describe at least three failure modes
- document when tool use is appropriate and when it is overkill

## Hands-On Workspace Structure

```text
week-13-tool-use-and-function-calling/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- provider-payloads/
|   |-- schema-design/
|   |-- tool-loop-mental-model/
|   `-- validation-and-safety/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-tool-design-checklist.md
|   `-- 03-provider-differences.md
`-- projects/
    `-- operations-assistant-lab/
```

## Exercises

The exercises are designed to make the mechanics visible before the larger project hides them behind abstractions.

You will practice:

- reading function-call shaped outputs
- deciding whether a call should execute
- comparing strong and weak tool definitions
- validating arguments and limits
- generating OpenAI and Anthropic compatible tool payloads

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [operations-assistant-lab](projects/operations-assistant-lab/README.md)

This project is a local, inspectable tool-enabled operations assistant. It includes:

- multiple tool schemas
- a planner that proposes tool calls
- validation before execution
- local tool implementations
- trace logging
- provider payload examples for OpenAI and Anthropic

Available tools:

- `lookup_ticket`
- `search_policy_docs`
- `calculate_refund`
- `get_weather_snapshot`

This is intentionally local-first. You should understand the loop before depending on live provider behavior.

## Build Plan

Build and study one assistant that can:

- inspect support tickets from local data
- search internal policy notes
- run deterministic refund calculations
- fetch weather snapshots from local mock data
- explain what it did through traceable output

Required qualities:

- readable schemas
- validation layer
- clear separation between planning and execution
- failure-aware responses
- provider payload literacy

## Suggested Study Order Inside This Week

1. read this README fully
2. work through `exercises/`
3. study the project `README.md`
4. run sample queries in the assistant
5. inspect the trace output
6. read the notes after you have seen the code once

## Deliverables

By the end of Week 13, you should have:

- completed the exercises
- run the local tool-enabled assistant
- inspected at least one valid multi-tool run
- inspected at least one rejected or invalid tool call
- compared OpenAI and Anthropic tool definitions side by side
- written your own short explanation of the tool loop

## Exit Criteria

You should not leave Week 13 until you can do all of the following without hand-waving:

- explain the difference between the model choosing a tool and the application executing it
- describe why tool descriptions matter
- show where validation happens in the code
- explain at least one failure prevented by validation
- compare OpenAI function tools and Anthropic client tools at a high level
- inspect a trace and explain what happened step by step

## Common Mistakes To Avoid

- defining tools with vague descriptions
- letting the model pass unchecked arguments into real code
- overloading one tool with too many responsibilities
- treating tool use as magical reasoning instead of explicit system design
- skipping traces and then guessing why a result looked wrong
- calling everything an agent before the core loop is solid

## Expert Notes That Matter Early

### Good tool design reduces prompt burden

If tools are well-scoped and well-described, your prompt does less cleanup work.

### Deterministic tools are often more valuable than "smart" tools

If a calculator or lookup can produce a reliable result, use it. Do not ask the model to imitate determinism.

### Tool choice should be earned

Not every workflow should let the model dynamically choose everything. Sometimes explicit routing is better.

### Traces create real learning

When you can inspect plan, validation, execution, and final answer, you stop guessing about system behavior.

## Final Standard For This Week

The correct outcome of Week 13 is not:

"I made the model call a function once."

The correct outcome is:

"I can design safe, inspectable tool interfaces and build a working tool-result loop that I understand end to end."
