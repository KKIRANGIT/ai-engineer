# Week 18: AI Milestone Product

Back to [Phase 2](../README.md)

## Goal

Ship one serious AI-powered application that demonstrates you can combine prompting, structured outputs, retrieval, tools, evaluation, and product judgment into a credible engineering artifact.

This is the capstone of the AI Core phase.

## Why This Week Matters

Without a serious milestone project, Phase 2 remains a set of isolated techniques.

Week 18 should prove that you can combine:

- provider-style model workflow thinking
- prompt and output-structure discipline
- retrieval or tool use
- evaluation
- safety and observability
- cost awareness

This project should be strong enough to discuss in:

- interviews
- client calls
- portfolio case studies

## What This Week Is Actually Training

Week 18 is training six deeper skills:

1. choosing the right AI pattern for a real problem
2. integrating multiple Phase 2 techniques into one coherent workflow
3. keeping the architecture as simple as the problem allows
4. making quality visible through traces, sources, and evals
5. explaining the tradeoffs like an engineer instead of a demo presenter
6. turning a build into a believable case-study artifact

The real outcome is not "I used many AI features." The real outcome is "I built one system whose design choices make sense."

## Scope Boundary For This Week

This week focuses on:

- one coherent product workflow
- retrieval and/or tool use where justified
- structured output
- visible source support
- logging and basic safety controls
- small but real evaluation discipline

This week does not require:

- a production deployment pipeline
- multiple providers
- every Phase 2 technique in one app
- a perfect frontend

The correct goal is not maximal complexity. The correct goal is architectural fit.

## What This Project Should Prove

By the end of this week, the project should prove that you can:

- choose the right AI pattern for a real task
- design a meaningful user workflow
- connect models to context or tools safely
- generate reliable outputs
- evaluate performance with more than anecdotal impressions
- explain the architecture and tradeoffs clearly

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 18 workspace
2. official references from Weeks 10-17 that match the chosen pattern
3. your own eval notes, architecture notes, and trace evidence

This week is where source discipline matters. Do not turn the capstone into a pile of disconnected patterns.

## Recommended Official References

Primary sources most relevant to this milestone:

- OpenAI Structured Outputs: <https://platform.openai.com/docs/guides/structured-outputs?lang=javascript>
- OpenAI Retrieval: <https://platform.openai.com/docs/guides/retrieval>
- OpenAI Tools guide: <https://platform.openai.com/docs/guides/tools?api-mode=responses>
- OpenAI Agent Evals: <https://platform.openai.com/docs/guides/agent-evals>
- OpenAI Usage guidelines: <https://platform.openai.com/docs/usage-guidelines>
- Anthropic tool use overview: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview>
- Anthropic Vision guide if your chosen product uses image input: <https://docs.anthropic.com/en/docs/build-with-claude/vision>

These references were chosen because the milestone product should stand on current primary-source guidance rather than random tutorials.

## Recommended Project Direction For This Workspace

This workspace uses one serious use case:

- a support operations copilot

Why this direction was chosen:

- it supports retrieval cleanly
- it benefits from structured output
- it can use deterministic tools
- it is easy to evaluate
- it naturally benefits from traces, guardrails, and cost awareness

## Project Capabilities This Week Includes

The milestone product in this workspace includes:

- clear user problem
- retrieval over local support policies
- structured analysis output
- deterministic tool support for SLA and escalation logic
- source visibility
- basic guardrails
- trace logging
- cost estimation
- a small evaluation set
- clean README and demo flow

## Planning Before Building

Before building or extending a milestone product, write:

- what the app does
- who it is for
- which AI pattern it uses
- what "good" output means
- what the major failure modes are
- what you will deliberately not build this week

Scope control matters even more here than in Phase 1, because AI features expand quickly if left vague.

## AI Pattern Selection Guidance

Ask first:

- Is this mainly prompting plus structured output?
- Does it need retrieval?
- Does it need tool use?
- Does it need an agent loop, or is a workflow enough?

Do not build the most complex architecture by default. Build the minimum architecture that matches the real problem.

For this workspace, the answer is:

- structured output: yes
- retrieval: yes
- deterministic tools: yes
- agent loop: no

That is an intentional design choice. Architectural restraint is part of the milestone.

## Recommended Build Sequence

1. define the use case clearly
2. choose the architecture pattern
3. build the core AI-style analysis flow
4. add retrieval and tool support
5. add validation, logging, and cost visibility
6. build a small eval set
7. refine documentation and case-study language

## Recommended Daily Breakdown

### Day 1: Scope and architecture

Focus:

- problem definition
- pattern selection
- failure boundaries

### Day 2: Core analysis flow

Focus:

- structured output contract
- response generation path

### Day 3: Retrieval and tools

Focus:

- policy retrieval
- citations
- deterministic SLA and escalation helpers

### Day 4: UX and application structure

Focus:

- output readability
- source presentation
- debug visibility

### Day 5: Observability and guardrails

Focus:

- logging
- validation
- usage and request boundaries

### Day 6: Eval set and improvement cycle

Focus:

- representative ticket cases
- inspect and fix obvious failures

### Day 7: Documentation and case study prep

Focus:

- README
- architecture note
- tradeoff summary
- case-study framing

## Hands-On Workspace Structure

```text
week-18-ai-milestone-product/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- evaluation-and-quality-review/
|   |-- observability-and-case-study-thinking/
|   |-- project-scope-and-pattern-selection/
|   `-- retrieval-and-structured-output-design/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-architecture-and-scope-notes.md
|   `-- 03-case-study-checklist.md
`-- projects/
    `-- support-ops-copilot/
```

## Exercises

The exercises isolate the milestone thinking before the larger project combines everything.

You will practice:

- scoping a serious use case
- choosing the correct AI pattern
- designing structured outputs and retrieval shape
- reviewing eval and observability requirements
- thinking about the project as a case study while building it

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [support-ops-copilot](projects/support-ops-copilot/README.md)

This project is a local support operations copilot that:

- analyzes support tickets
- retrieves relevant policy support
- emits structured output
- calculates SLA and escalation decisions
- logs traces
- estimates request cost
- evaluates itself on a small case set

It stays local and deterministic on purpose so the integrated system design is easy to inspect.

## Deliverables

By the end of this week, you should have:

- one AI milestone product
- clearly runnable local demo
- README with setup and architecture explanation
- eval set
- architecture note
- short case-study-ready summary

## Exit Criteria

You are ready to leave Phase 2 only if:

- the project is more than a generic chatbot
- you can explain why the architecture fits the problem
- the system has at least minimal evaluation discipline
- the project exposes enough of its internal quality story to be believable
- you can explain where retrieval, structure, tools, and guardrails each matter

## Common Mistakes To Avoid

- adding every AI technique just because you learned it
- skipping evaluation because the demo looks impressive
- hiding retrieval or tool behavior so failures stay opaque
- choosing a vague use case with no clear success criteria
- overbuilding agent loops when a workflow is enough

## Expert Notes That Matter Early

### Architectural restraint is a strength

The strongest milestone is often not the most complicated one. It is the one whose design fits the problem well.

### Quality must be visible

If your app is grounded, show sources. If it is structured, show why. If it is evaluated, mention that clearly.

### Case-study thinking starts during the build

Do not wait until the end to figure out what story the project proves.

### Integration quality matters more than feature count

One coherent system is more impressive than five disconnected tricks.

## Final Standard For This Week

The correct outcome of Week 18 is not:

"I shipped an AI app."

The correct outcome is:

"I shipped one credible AI product that demonstrates system design judgment, measurable quality thinking, and enough implementation depth to discuss seriously."
