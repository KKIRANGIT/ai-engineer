# Week 09: LLM Fundamentals and API Literacy

Back to [Phase 2](../README.md)

## Goal

Understand large language models as configurable systems with interfaces, costs, latency, limits, and behavioral tradeoffs, not as black boxes that "just answer."

This week should give you enough provider and runtime fluency to build every later Phase 2 system on top of real understanding rather than copied examples.

## Why This Week Matters

A large percentage of weak AI engineering starts here:

- the request shape is copied without being understood
- prompt and instruction layers are mixed together carelessly
- output structure is not inspected
- token usage is ignored
- provider differences are flattened into one vague mental model

That creates fragility later. If you do not understand:

- API shape
- context construction
- token usage
- model family tradeoffs
- multi-turn state handling
- output and tool-call structure

then every later week becomes weaker because it is built on unclear assumptions.

Week 09 is where you stop thinking:

"I am using an AI model."

and start thinking:

"I am operating a model-backed system through explicit APIs with observable tradeoffs."

## What This Week Is Really Training

At a deeper level, Week 09 is training six important habits.

### 1. Model-as-system thinking

An LLM call is not just "text in, text out." It is:

- a context construction problem
- a cost and token problem
- a latency problem
- a format-control problem
- an observability problem

### 2. Interface literacy

You must be able to read provider requests and responses directly. Frameworks are useful later, but API literacy is the foundation that makes frameworks optional rather than magical.

### 3. Comparative thinking

Different provider APIs are not interchangeable blobs. They have different request models, response shapes, conversation models, and ergonomics.

### 4. Logging and inspection

You should build a habit of recording:

- provider
- model
- request structure
- latency
- usage
- errors

This becomes the seed of later production observability.

### 5. Cost awareness

Strong AI engineering includes asking:

- how much context is this using?
- what does that imply for latency?
- what does that imply for cost?
- what is the smallest model that can do the job well enough?

### 6. Boundary control

You must understand the difference between:

- instructions
- user content
- tool results
- retrieved context
- model output

Many "model failures" are actually boundary failures.

## Scope Boundary

This week is not for:

- full agent frameworks
- production retrieval systems
- advanced prompt optimization
- structured JSON enforcement
- tool execution loops
- fine-tuning decisions

Those come next.

This week is for:

- direct API understanding
- multi-provider request/response literacy
- basic wrapper design
- usage and latency inspection
- context and conversation-state reasoning

## Week 09 Outcomes

By the end of this week, you should be able to:

- explain tokens, latency, and cost at a practical level
- explain the difference between instructions and user content
- compare model families by task instead of hype
- call OpenAI Responses and Anthropic Messages directly
- recognize the major structural differences in those APIs
- build small reusable wrappers around provider APIs
- normalize provider responses into one internal shape
- inspect and log request/response metadata
- debug a failed model call by looking at the payload and returned error

## Workspace Structure

This week now includes a full hands-on workspace:

```text
week-09-llm-fundamentals-and-api-literacy/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- concepts/
|   |   |-- 01_context_layers.py
|   |   `-- 02_tokens_latency_and_cost.py
|   |-- payloads/
|   |   |-- 01_openai_response_shape.py
|   |   `-- 02_anthropic_message_shape.py
|   `-- state-and-debugging/
|       |-- 01_conversation_state_planning.py
|       `-- 02_failure_analysis.py
|-- projects/
|   `-- llm-api-playground/
|       |-- README.md
|       |-- .env.example
|       |-- data/
|       |   `-- .gitkeep
|       |-- logs/
|       |   `-- .gitkeep
|       |-- src/
|       |   |-- __init__.py
|       |   |-- clients.py
|       |   |-- config.py
|       |   |-- cost_utils.py
|       |   |-- http_utils.py
|       |   |-- logger.py
|       |   |-- main.py
|       |   |-- models.py
|       |   |-- prompts.py
|       |   `-- sample_data.py
|       `-- tests/
|           |-- test_clients.py
|           |-- test_cost_utils.py
|           `-- test_logger.py
`-- notes/
    |-- 01-week-plan.md
    |-- 02-openai-vs-anthropic-map.md
    `-- 03-api-debugging-checklist.md
```

## What To Learn

## 1. Model-as-system mental model

A model request is not "one prompt." It is a configuration envelope around a task.

That envelope usually includes:

- model choice
- instruction layer
- user input
- optional conversation state
- optional tools
- output constraints
- logging or tracing metadata

Once you start seeing the full envelope, later architecture decisions become clearer.

## 2. Tokens, context, and cost

You should understand:

- tokens are the rough unit of model input and output accounting
- more context usually means more cost and often more latency
- large context is not free quality
- retrieval, summarization, and pruning often exist partly to control cost and noise

Practical rule:

Never ask only:

- can the model answer this?

Also ask:

- how much context does this require?
- what is the likely token bill?
- what does this do to latency?
- is the task even using the right model size?

## 3. Instructions, user content, and boundary layers

You should understand the difference between:

- instructions that define intended behavior
- user content that defines the current task
- retrieved content that grounds the answer
- tool results that add external facts
- model output that must be inspected, not blindly trusted

This week's exercises make these layers explicit so you stop treating prompt design as one undifferentiated text blob.

## 4. Model families and use-case fit

You should build beginner judgment around:

- larger versus smaller models
- lower-latency versus higher-reasoning options
- cheap iteration versus higher-quality completion
- when to use one provider over another

Do not memorize model choice as a static chart. Learn it as a decision problem:

- task difficulty
- format control needs
- latency tolerance
- budget sensitivity

## 5. OpenAI Responses API

The OpenAI side of this week is built around the current Responses API direction for new work.

You should understand:

- `input`
- `instructions`
- `previous_response_id`
- `output`
- `output_text`
- `usage`
- provider error handling

The project wrapper intentionally exposes the raw payload and then normalizes the returned data so you can compare "provider-native shape" and "application shape."

## 6. Anthropic Messages API

You should understand:

- `system`
- `messages`
- `content` blocks
- `max_tokens`
- `usage`
- `stop_reason`

You should also understand one major conceptual difference:

- Anthropic Messages is stateless by default, so you typically send the conversation history you want used
- OpenAI Responses supports stateful chaining through response IDs and conversation primitives

That difference matters architecturally.

## 7. Multi-turn state and history decisions

You need to understand:

- when to keep full history
- when to summarize history
- when to store application state separately from conversation text
- when carrying too much history increases cost or degrades answer quality

This week introduces those questions before retrieval and agent orchestration make them more complex.

## 8. Debugging and instrumentation

You should start logging at this stage, not after the system becomes complicated.

Track:

- provider
- model
- prompt or message size estimates
- latency
- usage metrics
- errors

The project includes a small JSONL logger so this habit becomes operational instead of theoretical.

## Best Learning Sequence For This Week

Use this order:

1. model-system mental model
2. tokens, cost, and latency
3. context layer boundaries
4. OpenAI Responses request/response literacy
5. Anthropic Messages request/response literacy
6. response normalization and wrapper design
7. logging and failure inspection

## Recommended Daily Breakdown

### Day 1: System mental model and token economics

Focus:

- tokens
- latency
- cost
- context layers

Do:

- complete the concept exercises
- explain one request as a structured system instead of a "prompt"

### Day 2: OpenAI Responses API

Focus:

- request body shape
- response output items
- usage
- stateful chaining concept

Do:

- read the OpenAI sample payload exercise
- run the playground in mock mode and inspect the normalized output

### Day 3: Anthropic Messages API

Focus:

- message list structure
- system instructions
- content blocks
- stateless multi-turn model

Do:

- read the Anthropic sample payload exercise
- run the playground in mock mode for Anthropic and compare the normalized output

### Day 4: Wrapper design and comparison

Focus:

- shared internal request model
- provider-specific payload builders
- response normalization

Do:

- inspect `clients.py`
- explain why one internal response shape helps later application code

### Day 5: Logging and debugging

Focus:

- latency logging
- usage logging
- error recording
- failed request reasoning

Do:

- read the debugging note
- inspect generated logs from mock runs

### Day 6: Live-call readiness

Focus:

- environment variables
- provider headers
- request safety
- cost awareness before using real keys

Do:

- read the project README carefully
- understand how to switch from mock mode to live mode

### Day 7: Synthesis and comparison note

Focus:

- OpenAI vs Anthropic ergonomics
- state handling differences
- output structure differences
- what felt easier or harder

Do:

- read the comparison note
- write your own short provider comparison summary

## Main Project

The core project for this week is:

- [projects/llm-api-playground](projects/llm-api-playground/README.md)

This project is intentionally built to be usable in two modes:

- `mock` mode for offline learning and testing
- live provider mode for real API calls when keys are available

That design choice matters because the goal of Week 09 is understanding request/response structure and application discipline, not just getting one live completion to work.

The project teaches:

- provider request construction
- provider-specific response parsing
- normalization into one internal response type
- trace logging
- cost estimation helpers
- CLI usage with reusable abstractions

## Build Quality Standard

For this week, "I got one API response" is not enough.

Minimum quality bar:

- provider payloads are understandable
- responses are parsed intentionally
- mock mode makes the project runnable without live dependencies
- logging exists
- usage and cost thinking are visible
- the README explains how to move from offline mode to live mode safely

## Deliverables

By the end of this week, you should have:

- concept and payload exercises
- one provider-aware CLI playground
- one internal normalized response model
- one request logger
- one comparison note
- one debugging checklist

## Exit Criteria

You are ready to move on only if:

- you can explain the difference between OpenAI Responses and Anthropic Messages at a practical level
- you can explain how instructions and user messages are represented in each
- you can inspect a response body and extract the useful content intentionally
- you can explain why logging usage and latency matters
- you can run the playground in mock mode and understand how to switch it to live mode

## Common Mistakes To Avoid

- copying example code without understanding the payload shape
- ignoring token and latency implications because the examples are small
- treating instructions as optional decoration
- flattening provider differences into one vague generic API model
- assuming a successful answer means the integration was well designed

## Expert Notes That Matter Early

### Provider fluency is leverage

If you understand providers directly, frameworks and SDKs become tools instead of crutches.

### API literacy reduces superstition

Many teams blame "the model" when the real issue is weak request construction or missing observability.

### A normalized internal shape is an architectural advantage

Applications often benefit from adapting provider-specific responses into one internal format. This makes later comparison, logging, and testing simpler.

## Suggested Official References

Prioritize these official sources:

1. OpenAI Responses API reference  
   https://platform.openai.com/docs/api-reference/responses
2. OpenAI migration guide to Responses  
   https://developers.openai.com/api/docs/guides/migrate-to-responses
3. Anthropic Messages API reference  
   https://platform.claude.com/docs/en/build-with-claude/working-with-messages
4. Anthropic API overview  
   https://platform.claude.com/docs/en/api/overview
5. Anthropic token counting  
   https://platform.claude.com/docs/en/api/messages/count_tokens

Use the official docs for correctness, but use this workspace as the place where those interfaces become understandable.

## Final Standard For This Week

The correct outcome of Week 09 is not:

"I called two model APIs."

The correct outcome is:

"I understand the current provider interfaces well enough to build, inspect, compare, and reason about model-backed systems directly, with real awareness of request shape, response shape, state handling, cost, and observability."
