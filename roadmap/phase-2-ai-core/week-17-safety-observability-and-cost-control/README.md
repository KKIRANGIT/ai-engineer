# Week 17: Safety, Observability, and Cost Control

Back to [Phase 2](../README.md)

## Goal

Learn the production concerns that separate real AI systems from persuasive demos: safety boundaries, traces, failure handling, and cost visibility.

This week is where the system stops being judged only by output quality and starts being judged by whether it is inspectable, constrained, and economically sane.

## Why This Week Matters

An AI app is not production-ready just because it produces good answers on happy-path examples.

Production-worthy AI systems need:

- safer behavior around untrusted input
- visibility into what happened during each request
- clear error and retry paths
- rough unit economics
- budget boundaries

This week matters because many later failures are not about model intelligence. They are about engineering blind spots.

## What This Week Is Actually Training

Week 17 is training five deeper skills:

1. identifying trust boundaries across user input, retrieved content, tools, and system prompts
2. designing simple guardrails against injection-like or unsafe behavior
3. instrumenting traces, latency, and failures
4. simulating retries, fallbacks, and degraded behavior
5. estimating per-request cost and enforcing budget controls

The real outcome is not "I know safety matters." The real outcome is "I can harden an AI workflow enough to reason about operating it."

## Scope Boundary For This Week

This week focuses on:

- trust boundaries
- prompt injection awareness
- tool-risk boundaries
- observability and traces
- retries and timeouts
- token and cost accounting

This week does not require:

- a full red-team program
- production-grade security infrastructure
- external monitoring stacks
- real provider billing integration

The correct first goal is not "solve AI safety in general." The correct first goal is "add practical controls and visibility to one concrete workflow."

## Week 17 Outcomes

By the end of this week, you should be able to:

- explain prompt-injection and tool-risk basics
- identify the trust boundaries in an AI workflow
- log key events and traces for debugging
- estimate cost per request and cost per user at a basic level
- design retry and timeout behavior intentionally
- create a failure-mode checklist for an AI application

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 17 workspace
2. official provider docs for safety, tracing, and data controls
3. your own trace logs and failure-mode notes

Do not turn this week into vague philosophy. Keep it grounded in one inspectable workflow.

## Recommended Official References

Primary sources:

- OpenAI Usage policies: <https://platform.openai.com/docs/usage-guidelines>
- OpenAI Trace grading: <https://platform.openai.com/docs/guides/trace-grading>
- OpenAI Agents SDK overview: <https://platform.openai.com/docs/guides/agents-sdk/>
- OpenAI Safety in building agents: <https://platform.openai.com/docs/guides/agent-builder-safety>
- OpenAI Data controls: <https://platform.openai.com/docs/guides/your-data>
- Anthropic prompt leak guidance: <https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak>

These references were chosen because safety, tracing, and data-control guidance changes over time and should be read from primary sources.

## Core Mental Models

## 1. Trust boundaries come first

AI systems often combine:

- trusted instructions
- user input
- retrieved content
- tool results
- application state

These sources do not all deserve the same trust.

The first safety skill is learning to ask:

- what content is trusted
- what content is untrusted
- what content can influence tool behavior

## 2. Prompt injection is a boundary problem

Once models consume external content, prompt injection becomes relevant.

You should understand the basic risk:

- retrieved or user-provided content may attempt to manipulate the model
- tool-enabled systems can amplify the impact

You do not need a full security program this week, but you do need engineering awareness and simple guardrail patterns.

## 3. Tools raise the stakes

Tools create higher stakes than plain chat.

You should think about:

- read-only vs write-capable tools
- approval boundaries
- parameter validation
- least privilege

If a model can trigger side effects, the application must constrain what success even means.

## 4. Observability is part of reliability

AI systems are hard to debug without traces.

Track:

- request inputs at a safe abstraction level
- model or variant choice
- token usage estimates
- latency
- retrieval results
- tool calls
- guardrail outcomes
- errors and fallback behavior

Good observability lets you answer:

- what happened
- where it failed
- what it cost

## 5. Cost is a system property

AI systems can become expensive in hidden ways.

Track:

- estimated input token cost
- estimated output token cost
- retrieval or tool-related costs where relevant
- cost per request
- budget alarms or per-request thresholds

This is one of the clearest differences between a demo and a product-ready system.

## Best Learning Sequence For This Week

1. trust boundaries
2. prompt injection basics
3. tool safety
4. tracing and observability
5. retries and timeouts
6. cost accounting
7. failure-mode review

## Recommended Daily Breakdown

### Day 1: Threat and trust mapping

Focus:

- identify trusted vs untrusted context

### Day 2: Guardrails

Focus:

- prompt injection awareness
- read-only vs risky operations

### Day 3: Add instrumentation

Focus:

- log requests, latency, costs, and outputs

### Day 4: Add failure handling

Focus:

- retries
- timeouts
- clearer user-visible errors

### Day 5: Add cost tracking

Focus:

- per-request cost estimates
- simple per-user budget logic

### Day 6: Failure-mode checklist

Focus:

- list predictable weak points

### Day 7: Review and tighten

Focus:

- what is still unsafe or invisible

## Hands-On Workspace Structure

```text
week-17-safety-observability-and-cost-control/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- cost-and-budget-controls/
|   |-- observability-and-retries/
|   |-- prompt-injection-and-guardrails/
|   `-- trust-boundaries/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-failure-mode-checklist.md
|   `-- 03-safety-and-cost-design-notes.md
`-- projects/
    `-- guarded-support-assistant-lab/
```

## Exercises

The exercises isolate the main hardening concepts before the larger project combines them.

You will practice:

- mapping trust boundaries
- identifying prompt-injection risk
- thinking about retries and timeout behavior
- estimating request cost and budget pressure

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [guarded-support-assistant-lab](projects/guarded-support-assistant-lab/README.md)

This project is a local guarded support assistant that:

- classifies request trust boundaries
- screens for suspicious or injection-like text
- logs a full request trace
- simulates retries and fallbacks
- estimates token and request cost
- blocks or warns on budget thresholds

It stays local and deterministic on purpose so the hardening logic is easy to inspect.

## Build Plan

Build and study one guarded AI workflow that can:

- inspect user input and retrieved notes
- apply simple guardrails
- simulate a support response path
- log trace events and failure points
- estimate request cost
- warn or block when a request exceeds a budget rule

Required qualities:

- explicit trust boundaries
- readable trace logging
- retry and timeout simulation
- cost estimation
- failure-mode documentation

## Suggested Study Order Inside This Week

1. read this README fully
2. complete the exercises
3. read the project README
4. run a safe request
5. run a suspicious or risky request
6. inspect the trace and cost output
7. read the notes after you have seen the behavior

## Deliverables

By the end of Week 17, you should have:

- completed the exercises
- run the guarded workflow on multiple request types
- inspected the request trace
- reviewed per-request cost estimates
- written your own short failure-mode checklist

## Exit Criteria

You should not leave Week 17 until you can:

- identify the main trust boundaries in an AI workflow
- explain how a simple injection screen or output filter works
- inspect a trace and explain where a failure occurred
- explain roughly what a request costs
- describe what the system does when guardrails or budgets fail

## Common Mistakes To Avoid

- assuming prompt quality alone makes the system safe
- giving tools more authority than necessary
- treating logs as optional
- waiting too long to think about cost
- hiding failures instead of surfacing them clearly

## Expert Notes That Matter Early

### Safety begins with boundaries

The safest system is often the one with clearer scope, not just stronger wording.

### Observability is part of reliability

If you cannot inspect the system, you cannot improve it responsibly.

### Cost awareness is product awareness

Economic viability is part of engineering quality for AI systems.

### Simple guardrails still matter

Even lightweight screens, allowlists, and approval boundaries can prevent a large class of avoidable failures.

## Final Standard For This Week

The correct outcome of Week 17 is not:

"I know AI apps can be risky."

The correct outcome is:

"I can identify trust boundaries, instrument an AI system, reason about its failures, and estimate whether its behavior is operationally and economically sane."
