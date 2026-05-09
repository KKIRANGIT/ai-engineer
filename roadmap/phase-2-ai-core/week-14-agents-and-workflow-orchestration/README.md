# Week 14: Agents and Workflow Orchestration

Back to [Phase 2](../README.md)

## Goal

Understand when multi-step agent patterns actually help, and learn how to orchestrate them with enough discipline to keep them inspectable and reliable.

This week is not about blindly building a "multi-agent system." It is about architectural judgment, state design, and operational control.

## Why This Week Matters

The AI ecosystem often rewards the word "agent" more than the engineering reality behind it.

Many tasks that people label as agentic are better solved by:

- retrieval plus structured output
- explicit workflow code
- one or two tool calls with deterministic control

At the same time, some tasks do benefit from more flexible orchestration, especially when they involve:

- multiple intermediate steps
- iterative search or tool use
- uncertain execution paths
- human review checkpoints
- long-running or resumable state

This week teaches you to recognize the difference and to build systems that make the tradeoff visible.

## What This Week Is Actually Training

Week 14 is training five deeper skills:

1. separating deterministic workflows from flexible agent loops
2. designing state that survives multi-step execution
3. deciding where routing should be explicit versus model-driven
4. adding retry, review, and trace points without losing clarity
5. understanding what orchestration frameworks are really buying you

If Week 13 was about one tool loop, Week 14 is about sequencing and governing many steps over time.

## Scope Boundary For This Week

This week focuses on:

- workflow vs agent distinction
- ReAct-style and planner-executor patterns
- stateful orchestration
- retry and review boundaries
- graph-style execution thinking
- framework positioning

This week does not require:

- production deployment infrastructure
- real background queues
- real browser agents
- actual distributed multi-agent systems

The correct first goal is not "make an autonomous system." The correct first goal is "make orchestration choices understandable."

## Week 14 Outcomes

By the end of this week, you should be able to:

- distinguish workflows from agents clearly
- explain ReAct-style loops in application terms
- implement planner-executor style decomposition
- reason about state, retries, and human review checkpoints
- justify when LangChain adds convenience and when LangGraph adds orchestration control
- build one problem in at least two orchestration styles and compare the tradeoffs

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 14 workspace
2. official provider and framework docs for current terminology
3. your own traces and architecture notes

Do not start from broad "agent" articles. They usually blur together planning, tools, memory, and orchestration without enough precision.

## Recommended Official References

Primary sources:

- OpenAI tools guide: <https://platform.openai.com/docs/guides/tools?api-mode=responses>
- OpenAI remote MCP guide: <https://platform.openai.com/docs/guides/tools-remote-mcp?lang=python>
- OpenAI Agents guide: <https://platform.openai.com/docs/guides/agents/agent-builder%20rel%3D>
- Anthropic tool use overview: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview>
- Anthropic tool-use implementation guide: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use>
- LangChain overview: <https://docs.langchain.com/oss/python/langchain/overview>
- LangGraph overview: <https://docs.langchain.com/oss/javascript/langgraph>

These references were chosen because orchestration guidance is time-sensitive and framework positioning changes quickly.

## Core Mental Models

## 1. Workflow vs agent

A workflow is usually:

- predetermined
- explicit
- easy to inspect

An agent is usually:

- more flexible in path selection
- more dynamic in tool use
- more complex to debug

The important skill is not memorizing the labels. The important skill is deciding whether flexibility earns its cost.

## 2. ReAct-style loops

At the architecture level, ReAct means:

1. reason about what to do next
2. act with a tool or sub-step
3. observe the result
4. decide whether more action is needed

You do not need hidden chain-of-thought output to understand this. You need a visible action loop and traceable observations.

## 3. Planner-executor patterns

Many harder tasks benefit from splitting:

- planning
- execution
- synthesis

This can improve observability and reduce chaos, but it is not free. If the task is already deterministic, an explicit workflow may be simpler and better.

## 4. State is the real backbone

Multi-step systems live or die by state design.

State may include:

- user query
- intermediate decisions
- retrieved evidence
- retry counts
- review flags
- final output draft

Frameworks often look impressive because they formalize state transitions. That is the actual value.

## 5. Durable execution and human review

Serious agent systems are rarely just "call model in a loop."

They often need:

- retry boundaries
- checkpoints
- human approval
- resumability
- step-level trace logs

If you do not design these explicitly, the system may look autonomous while actually being fragile.

## Best Learning Sequence For This Week

1. workflow vs agent distinction
2. ReAct and planner-executor patterns
3. state and retries
4. graph-style orchestration
5. human review checkpoints
6. framework positioning

## Recommended Daily Breakdown

### Day 1: Architectural distinction

Focus:

- deterministic vs dynamic control
- workflow vs agent classification

### Day 2: ReAct-style loop

Focus:

- plan, act, observe, continue
- making the loop visible in code

### Day 3: Planner-executor decomposition

Focus:

- separate planning from action
- understand when this split helps

### Day 4: Direct workflow

Focus:

- explicit step ordering
- routing
- traceability

### Day 5: Graph-style orchestration

Focus:

- state transitions
- retry edges
- review checkpoints

### Day 6: Compare orchestration styles

Focus:

- direct workflow vs graph runtime vs lightweight agent loop
- where complexity rises

### Day 7: Judgment write-up

Focus:

- explain when flexibility helped
- explain when deterministic control was better

## Hands-On Workspace Structure

```text
week-14-agents-and-workflow-orchestration/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- framework-positioning/
|   |-- react-and-planner/
|   |-- state-and-retries/
|   `-- workflow-vs-agent/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-orchestration-checklist.md
|   `-- 03-framework-positioning.md
`-- projects/
    `-- research-brief-orchestrator/
```

## Exercises

The exercises isolate the core orchestration mechanics before the project combines them.

You will practice:

- classifying systems as workflow-like or agent-like
- understanding ReAct loops
- comparing planner-executor and fixed pipelines
- thinking about retries, state, and review boundaries
- positioning LangChain and LangGraph correctly

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [research-brief-orchestrator](projects/research-brief-orchestrator/README.md)

This project solves one problem in three orchestration styles:

- a direct deterministic workflow
- a graph-style state machine
- a lightweight agent loop

The shared task is generating a local research brief from internal documents. The point is not fancy output. The point is seeing how orchestration style changes visibility, control, and failure handling.

## Build Plan

Build and study one multi-step research assistant that can:

- classify a query into one or more topics
- retrieve relevant documents
- draft a concise brief
- run a quality gate
- request human review when evidence is weak

Required qualities:

- explicit state
- traceable step history
- direct workflow version
- graph-style orchestration version
- lightweight agent-loop version

## Suggested Study Order Inside This Week

1. read this README fully
2. complete the exercises
3. run the direct workflow version
4. run the graph workflow version
5. run the agent-loop version
6. compare traces and outputs
7. read the notes after you have seen the project behavior

## Deliverables

By the end of Week 14, you should have:

- completed the exercises
- run the project in at least two orchestration modes
- inspected at least one retry or review path
- written your own comparison of workflow vs agent tradeoffs
- explained how state moves through the system

## Exit Criteria

You should not leave Week 14 until you can:

- explain why a workflow is often better than an agent
- describe what a ReAct loop is doing structurally
- show where state lives in the code
- explain how retries or review checkpoints work
- compare direct orchestration with graph-style orchestration
- explain when LangChain or LangGraph would be justified in a real system

## Common Mistakes To Avoid

- building an agent because it sounds more advanced
- using a framework before understanding the underlying loop
- hiding state transitions inside vague abstractions
- failing to log intermediate decisions
- confusing flexibility with quality
- adding retries without clear stopping rules

## Expert Notes That Matter Early

### Complexity should earn its place

Every orchestration layer should solve a real problem in reliability, durability, or control.

### Deterministic workflows are underrated

If you already know the process, explicit code is often better than agentic freedom.

### State design is usually the real challenge

Many "agent" failures are actually failures of state handling, step boundaries, or missing review logic.

### Frameworks are multipliers, not substitutes

Frameworks help once you understand the orchestration problem clearly. They do not provide judgment for free.

## Final Standard For This Week

The correct outcome of Week 14 is not:

"I built an agent."

The correct outcome is:

"I can distinguish where agentic flexibility is useful, where deterministic workflows are better, and how orchestration choices affect reliability, state, and debugging."
