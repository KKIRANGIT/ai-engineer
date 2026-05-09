# Orchestration Checklist

Back to [Week 14 README](../README.md)

Use this checklist when deciding whether a system should be a workflow, a graph, or an agent loop.

## Control

- Is the step order mostly known in advance?
- Can routing be expressed as simple conditions?
- Is dynamic tool choice actually necessary?

## State

- What information must survive between steps?
- Do retries need counters or checkpoints?
- Should the system pause and resume later?

## Reliability

- Where can the system fail?
- What should happen after a low-confidence result?
- Is human review required for weak evidence or risky action?

## Observability

- Can you inspect every intermediate step?
- Are transitions explicit?
- Will a trace explain why the path changed?

## Complexity

- Would plain code be clearer than a framework here?
- Is a graph runtime solving a real branching or durability problem?
- Is the word "agent" being used because it is accurate or because it sounds advanced?
