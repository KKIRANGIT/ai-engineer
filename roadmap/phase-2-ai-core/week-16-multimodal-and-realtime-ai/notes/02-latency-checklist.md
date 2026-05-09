# Latency Checklist

Back to [Week 16 README](../README.md)

Use this checklist when designing multimodal or realtime systems.

## Input Path

- Is audio transcribed before model reasoning?
- Are images resized or preprocessed?
- Is there any avoidable delay before the model can start?

## Session Flow

- Does the user know when the system is listening or processing?
- Are partial responses shown early enough?
- Can the user interrupt or correct the flow?

## Output Path

- Is output streamed or delayed until full completion?
- Does the system expose meaningful progress?
- Is the slowest part text generation, audio generation, or tool work?

## Practical Design Question

- Does the current latency profile justify a realtime architecture, or is a chained pipeline easier and good enough?
