# Week 14 Study Plan

Back to [Week 14 README](../README.md)

## Main Objective

By the end of this week, you should understand orchestration as a systems-design choice, not a fashionable label.

## Suggested Flow

### Day 1

- read the Week 14 README
- run the workflow-vs-agent exercises
- write your own short rule for when a workflow is enough

### Day 2

- run the ReAct and planner exercises
- explain where the control loop lives

### Day 3

- run the state-and-retries exercises
- describe what state must persist between steps

### Day 4

- run the direct workflow mode in the main project
- inspect the trace

### Day 5

- run the graph workflow mode
- compare the transition logic with the direct workflow

### Day 6

- run the lightweight agent mode
- compare flexibility against debuggability

### Day 7

- read the notes
- write a one-page comparison:
  - direct workflow
  - graph orchestration
  - agent loop

## Review Questions

- What does the system know after each step?
- Where would a retry happen and why?
- When should a human review interrupt the flow?
- What does a framework add beyond plain Python code?
