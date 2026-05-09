# Week 14: Agents and Workflow Orchestration

Back to [Phase 2](../README.md)

## Goal

Understand when multi-step agent patterns actually help, and learn how to orchestrate them with enough discipline to keep them inspectable and reliable.

This week is not about blindly building "multi-agent systems." It is about architectural judgment.

## Why This Week Matters

Agent systems are often overbuilt. Many tasks that people label as "agentic" are better solved by:

- retrieval plus structured output
- explicit workflow code
- one or two tool calls with deterministic control

At the same time, some tasks do benefit from more flexible orchestration, especially when they involve:

- multiple intermediate steps
- tool iteration
- uncertain paths
- human review checkpoints
- long-running stateful execution

This week teaches you to recognize the difference.

## Week 14 Outcomes

By the end of this week, you should be able to:

- distinguish workflows from agents clearly
- explain ReAct-style loops
- understand planner-executor style decomposition
- justify when LangChain or LangGraph adds value
- reason about durable execution and state
- build one multi-step workflow directly and one through a framework abstraction

## What To Learn

## 1. Workflow vs agent

A workflow is usually:

- predetermined
- explicit
- easy to inspect

An agent is usually:

- more flexible in path selection
- more dynamic in tool use
- more complex to debug

The crucial skill is knowing when you need flexibility badly enough to justify complexity.

## 2. ReAct-style loops

Learn the thought-action-observation pattern at a systems level:

- reason about what to do
- act with a tool
- observe the result
- decide what to do next

You do not need hidden chain-of-thought outputs to understand the architecture. You need to understand the loop structure.

## 3. Planner-executor patterns

Many complex tasks benefit from splitting:

- planning
- execution
- synthesis

This can reduce chaos and improve observability.

Important rule:

Do not assume every task needs a planner. Sometimes the plan can be implicit in your deterministic workflow.

## 4. State and memory

Once workflows become multi-step, state matters.

You should think about:

- current working context
- tool results so far
- user constraints
- what should persist between steps

This is part of why orchestration frameworks exist.

## 5. LangChain vs LangGraph

Current practical view:

- LangChain is a higher-level framework and integration layer that can get you started quickly with models, tools, and common agent loops.
- LangGraph is the lower-level orchestration runtime focused on durable execution, stateful flows, human-in-the-loop patterns, and complex agent control.

Important lesson:

- start simple
- reach for LangGraph when you genuinely need orchestration control, persistence, interrupts, or complex state transitions

## 6. Durable execution and human-in-the-loop

This is where serious agent systems differ from toy loops.

You should understand:

- retries and resumability
- approval checkpoints
- long-running steps
- traceability

Agent systems often need more operational scaffolding than people expect.

## Best Learning Sequence For This Week

1. workflow vs agent distinction
2. ReAct-style loops
3. planner-executor design
4. framework positioning
5. durable execution mindset
6. human review points

## Recommended Daily Breakdown

### Day 1: Architectural distinctions

Focus:

- workflow vs agent
- deterministic vs dynamic control

### Day 2: ReAct loop implementation

Focus:

- simple tool-using reasoning loop

### Day 3: Planner-executor pattern

Focus:

- splitting tasks into phases

### Day 4: Direct-code orchestration

Focus:

- implement a multi-step pipeline without heavy abstractions

### Day 5: Framework implementation

Focus:

- rebuild the same or similar flow using LangChain or LangGraph

### Day 6: Trace and compare

Focus:

- inspect how abstraction changed visibility and complexity

### Day 7: Judgment write-up

Focus:

- explain when the framework helped
- explain when it felt unnecessary

## Build Plan

Build one multi-step assistant or pipeline twice:

### Version 1: direct implementation

Use plain code and explicit steps.

### Version 2: framework-assisted implementation

Use LangChain or LangGraph where appropriate.

Suggested workflow ideas:

- research then summarize
- classify then retrieve then answer
- gather inputs then draft output then validate format

## Deliverables

- one direct-code multi-step workflow
- one framework-based workflow
- comparison note on abstraction costs and benefits
- trace notes or diagrams showing the step flow

## Exit Criteria

- you can explain when an agent is justified
- you can distinguish orchestration from prompting
- you understand what LangGraph is for compared with LangChain
- you can discuss state, persistence, and human review intelligently

## Common Mistakes To Avoid

- building an agent because it sounds more advanced
- using a framework before you understand the underlying loop
- failing to log intermediate steps
- confusing flexibility with quality

## Expert Notes That Matter Early

### Complexity should earn its place

Every new orchestration layer should solve a real problem.

### Deterministic workflows are underrated

If you know the process already, explicit code is often better than agentic freedom.

### State design is part of reliability

Most multi-step failures are really failures of state handling, tool boundaries, or observability.

## Suggested Official References

- LangChain overview
- LangGraph overview
- provider tool-use docs from prior weeks

## Final Standard For This Week

The correct outcome of Week 14 is not "I built an agent."

The correct outcome is:

"I can distinguish where agentic flexibility is useful, where deterministic workflows are better, and how orchestration choices affect reliability and complexity."
