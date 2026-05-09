# Week 09: LLM Fundamentals and API Literacy

Back to [Phase 2](../README.md)

## Goal

Understand large language models as configurable systems with interfaces, costs, latency, limits, and behavioral tradeoffs, not as black boxes that "just answer."

This week should give you the provider and runtime fluency needed to build every later week properly.

## Why This Week Matters

A huge amount of weak AI engineering comes from skipping this layer.

If you do not understand:

- the API shape
- context construction
- token costs
- model family tradeoffs
- statefulness and multi-turn handling
- tool-call response structure

then everything later becomes fragile, because you are building on top of an unclear foundation.

Week 09 is where you stop thinking "I am using an AI model" and start thinking "I am operating a model-backed system through explicit interfaces."

## Week 09 Outcomes

By the end of this week, you should be able to:

- explain tokens, context windows, latency, and cost at a practical level
- distinguish instructions from user content and know why that boundary matters
- compare model families by task, not hype
- call both OpenAI and Anthropic APIs directly
- understand the current OpenAI Responses API shape
- understand the current Anthropic Messages API shape
- build basic reusable wrappers instead of only one-off calls
- debug a failed model request by inspecting payload, response structure, and model settings

## What To Learn

## 1. Model-as-system mental model

An LLM request is not just "text in, text out." It is:

- an input construction problem
- a cost problem
- a latency problem
- a format-control problem
- sometimes a tool orchestration problem

The earlier you understand that, the stronger every later design decision becomes.

## 2. Tokens, context, and cost

You should understand:

- tokens are the approximate unit of text processing
- both prompt size and output size affect cost
- large context can improve quality for some tasks but can also increase latency and cost
- retrieval and summarization often exist partly to manage context efficiently

Expert beginner rule:

Never ask only "can the model do this?" Also ask:

- what is the context cost
- what is the latency cost
- what is the reliability cost

## 3. Instructions, user content, and boundaries

In modern APIs, instruction layers matter.

You should understand:

- system or developer instructions define the intended behavioral contract
- user input provides task-specific content
- external documents, retrieval results, and tool outputs are separate context layers

This matters because many model failures are really context-construction failures.

## 4. Model families and use-case fit

You should develop early judgment around:

- larger vs smaller models
- reasoning-focused vs lower-latency options
- text-first vs multimodal capabilities
- cost-sensitive vs quality-sensitive paths

Do not learn model choice as a static table. Learn it as a tradeoff exercise:

- task complexity
- response format needs
- latency tolerance
- budget

## 5. OpenAI Responses API

This is the current default OpenAI integration direction for new work.

You should learn:

- `input` shape
- response `output` items
- `output_text` helper
- stateful chaining via `previous_response_id`
- tool-aware response structure
- why Responses is preferred over Chat Completions for new builds

Important current guidance:

- Chat Completions is still supported
- Responses is recommended for new projects

## 6. Anthropic Messages API

You should learn:

- message structure
- system prompting model
- content blocks
- tool definitions and tool results
- how Claude responses differ structurally from OpenAI responses

Important mindset:

- do not treat provider APIs as interchangeable blobs
- treat each API as a distinct interface with its own strengths and response model

## 7. Multi-turn state and conversation handling

You need to understand:

- what should stay in context
- what should be summarized or externalized
- when carrying full conversation state becomes expensive or noisy

This becomes critical later for assistants, tools, and agent workflows.

## 8. Debugging and instrumentation at the API layer

Start building a logging habit now.

Track:

- model used
- instructions used
- prompt size
- latency
- output length
- error responses

This is the seed of later observability.

## Best Learning Sequence For This Week

1. model-system mental model
2. tokens and cost
3. context and instructions
4. OpenAI Responses API
5. Anthropic Messages API
6. wrapper design
7. basic instrumentation

## Recommended Daily Breakdown

### Day 1: Model concepts and cost model

Focus:

- tokens
- context windows
- latency
- cost thinking

### Day 2: OpenAI Responses API

Focus:

- request shape
- output items
- state handling

Build:

- tiny CLI chat wrapper

### Day 3: Anthropic Messages API

Focus:

- message format
- system prompts
- content structure

Build:

- equivalent CLI wrapper

### Day 4: Prompt comparisons and parameter literacy

Focus:

- compare outputs across providers or models
- inspect how instruction changes affect behavior

### Day 5: Wrapper cleanup

Focus:

- reusable functions
- cleaner request construction
- shared logging

### Day 6: Debugging and analysis

Focus:

- inspect failures
- compare latency and output style

### Day 7: Document tradeoffs

Focus:

- summarize what each provider felt better or worse at
- document costs and constraints

## Build Plan

Build two direct-provider CLI apps:

- one using OpenAI Responses
- one using Anthropic Messages

Then build one comparison notebook or markdown note covering:

- output style
- instruction following
- latency
- ergonomics of the API
- cost implications

## Deliverables

- one OpenAI CLI chat wrapper
- one Anthropic CLI chat wrapper
- one comparison note
- one simple usage logger or trace note

## Exit Criteria

- you can call both providers directly without confusion
- you understand the major structural differences in their APIs
- you can discuss cost and context tradeoffs in practical terms
- you can explain why Responses is the OpenAI default for new builds

## Common Mistakes To Avoid

- copying sample code without understanding the request or response shape
- ignoring tokens and latency because the example is small
- treating system instructions as optional decoration
- assuming a single provider mental model applies everywhere

## Expert Notes That Matter Early

### Provider fluency is leverage

If you understand providers directly, frameworks become optional rather than necessary.

### API literacy reduces superstition

Many people attribute failures to "bad models" when the real issue is bad context or poor request construction.

### Logging should begin before complexity

The best time to start tracing behavior is before the system becomes hard to inspect.

## Suggested Official References

- OpenAI Responses migration guide
- Anthropic Messages API docs
- OpenAI structured outputs guide for upcoming Week 10 context

## Final Standard For This Week

The correct outcome of Week 09 is not "I called two model APIs."

The correct outcome is:

"I understand the current provider interfaces well enough to build, inspect, compare, and reason about model-backed systems directly."
