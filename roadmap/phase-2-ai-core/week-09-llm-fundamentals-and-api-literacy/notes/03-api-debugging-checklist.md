# API Debugging Checklist

Back to [Week 09](../README.md)

Use this checklist when a model call fails or behaves unexpectedly.

## Request Construction

- Did the code send the correct provider endpoint?
- Did it include the required authentication header?
- Did it build the payload in the format the provider expects?
- Did it separate instructions from user content correctly?

## Model and Cost Thinking

- Was the selected model appropriate for the task?
- Was the context much larger than needed?
- Did the request send unnecessary history?

## Response Inspection

- Did the provider return an explicit error body?
- Did the model stop for a reason you did not expect?
- Was the text in a different response field than your code assumed?
- Did usage metrics come back, and if so what do they suggest?

## Logging Quality

- Did you record provider, model, latency, and prompt details?
- Can you replay the same request easily?
- If the issue came from a live call, can you compare it against a mock run?

## Final Question

Are you sure the problem is "the model," or is the real problem the payload, the boundary design, or the missing observability?
