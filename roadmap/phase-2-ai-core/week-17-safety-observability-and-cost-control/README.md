# Week 17: Safety, Observability, and Cost Control

Back to [Phase 2](../README.md)

## Goal

Learn the production concerns that separate real AI systems from persuasive demos: safety boundaries, traces, failure handling, and cost visibility.

## Why This Week Matters

An AI app is not production-ready just because it produces good answers on happy-path examples.

Production-worthy AI systems need:

- safer behavior around untrusted input
- visibility into what happened during each request
- clear error and retry paths
- rough unit economics

This week matters because many later failures are not about model intelligence. They are about engineering blind spots.

## Week 17 Outcomes

By the end of this week, you should be able to:

- explain prompt-injection and tool-risk basics
- identify the trust boundaries in an AI workflow
- log key events and traces for debugging
- estimate cost per request and cost per user at a basic level
- design retry and timeout behavior intentionally
- create a failure-mode checklist for an AI application

## What To Learn

## 1. Trust boundaries

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

## 2. Prompt injection basics

Once models consume external content, prompt injection becomes relevant.

You should understand the basic risk:

- retrieved or user-provided content may attempt to manipulate the model
- tool-enabled systems can amplify the impact

You do not need a full security program this week, but you do need engineering awareness.

## 3. Tool abuse and action risk

Tools create higher stakes than plain chat.

You should think about:

- read-only vs write-capable tools
- approval boundaries
- parameter validation
- least privilege

If a model can trigger side effects, the application must constrain what "success" even means.

## 4. Observability and traces

AI systems are hard to debug without traces.

Track:

- request inputs at a safe abstraction level
- model choice
- token usage
- latency
- retrieval results
- tool calls
- errors

Good observability lets you answer:

- what happened
- where it failed
- what it cost

## 5. Retries, timeouts, and degraded behavior

Learn to think about operational failure modes:

- provider timeout
- malformed model output
- tool failure
- retrieval miss
- rate limits

Ask:

- should this be retried
- should the user see partial results
- should the app fall back to a safer mode

## 6. Cost accounting

Current AI systems can become expensive in hidden ways.

Track:

- input token cost
- output token cost
- retrieval or file-search costs where relevant
- tool-related costs
- cost per user task

This is one of the biggest differentiators in client and product conversations.

## 7. Failure-mode inventory

Create a structured list of:

- bad user input cases
- grounding failures
- schema failures
- tool misfires
- rate-limit conditions
- latency spikes

This list becomes the seed of real production hardening.

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

### Day 2: Tool and action risk review

Focus:

- read-only vs side-effecting operations
- approval points

### Day 3: Add instrumentation

Focus:

- log requests, latency, and outputs

### Day 4: Add failure handling

Focus:

- retries
- timeouts
- clearer user-visible errors

### Day 5: Add cost tracking

Focus:

- per-request cost notes
- simple per-user estimate

### Day 6: Failure-mode checklist

Focus:

- list predictable weak points

### Day 7: Review and tighten

Focus:

- what is still unsafe or invisible

## Build Plan

Take one AI project from Weeks 12-16 and improve it with:

- request logging or trace capture
- token and cost tracking
- retry/timeout handling
- documented guardrails
- failure-mode checklist

## Deliverables

- instrumented AI app
- cost estimate worksheet
- failure-mode checklist
- short note on trust boundaries and remaining risks

## Exit Criteria

- you can explain what a request costs at a rough level
- you can identify key failure and trust boundaries
- you can observe the system with useful logs or traces
- you can describe what happens when major subsystems fail

## Common Mistakes To Avoid

- assuming prompt quality alone makes the system safe
- giving tools more authority than necessary
- treating logs as optional
- waiting too long to think about cost

## Expert Notes That Matter Early

### Safety begins with boundaries

The safest system is often the one with clearer scope, not just stronger wording.

### Observability is part of reliability

If you cannot inspect the system, you cannot improve it responsibly.

### Cost awareness is product awareness

Economic viability is part of engineering quality for AI systems.

## Suggested Official References

- provider docs on tool use and hosted tools
- provider docs on token or usage measurement
- eval and tracing guidance where available

## Final Standard For This Week

The correct outcome of Week 17 is not "I know AI apps can be risky."

The correct outcome is:

"I can identify trust boundaries, instrument an AI system, reason about its failures, and estimate whether its behavior is operationally and economically sane."
