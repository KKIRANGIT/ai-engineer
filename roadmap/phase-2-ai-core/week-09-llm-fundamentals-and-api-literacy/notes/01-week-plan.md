# Week 09 Study Plan

Back to [Week 09](../README.md)

## Objective

Use this week to become operationally comfortable with provider APIs before moving into prompt optimization, structured outputs, retrieval, and tools.

The main success condition is not "I got one answer." It is:

- you understand the request shape
- you understand the response shape
- you understand how to inspect, compare, and debug both

## Suggested Order

### Day 1

- read the Week 09 README
- complete the concept exercises
- explain tokens, latency, and cost in your own words

### Day 2

- complete the OpenAI payload exercise
- inspect the OpenAI request/response shape carefully
- run the project in mock OpenAI mode

### Day 3

- complete the Anthropic payload exercise
- inspect the Anthropic request/response shape carefully
- run the project in mock Anthropic mode

### Day 4

- inspect the shared request model and normalized response model
- understand why provider-specific parsing is separated from application-facing output

### Day 5

- inspect the logger and cost helpers
- run a few prompts and read the trace logs

### Day 6

- review the debugging checklist
- trace one failure path in your head from bad config to surfaced error

### Day 7

- read the provider comparison note
- write your own short summary of which interface feels more natural and why

## Minimum Success Definition

You should not leave this week saying:

"I can call a model."

You should leave saying:

"I understand how provider request and response interfaces work, how to compare them, and how to build small wrappers around them responsibly."
