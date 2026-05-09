# Framework Positioning

Back to [Week 14 README](../README.md)

## Why This Note Exists

Beginners often ask whether they should learn LangChain, LangGraph, or "build agents from scratch" first.

The answer depends on the orchestration problem.

## Practical Positioning

### Plain code

Use plain code when:

- the flow is small
- step order is mostly fixed
- you want maximum clarity
- you are still learning the mechanics

### LangChain

Use LangChain when:

- you want model and tool integrations quickly
- you need a higher-level agent abstraction
- you do not need full low-level orchestration control

### LangGraph

Use LangGraph when:

- stateful control really matters
- workflows branch and rejoin
- you need durable execution
- you need interrupts or human-in-the-loop checkpoints
- you want stronger control over transitions

## The Local Project Strategy

This Week 14 project stays dependency-light on purpose.

It teaches:

- direct workflow control
- graph-style orchestration ideas
- a lightweight agent loop

That makes the underlying architecture visible before a framework hides it behind convenience APIs.
