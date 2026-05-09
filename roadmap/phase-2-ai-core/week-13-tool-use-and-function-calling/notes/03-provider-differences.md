# Provider Differences

Back to [Week 13 README](../README.md)

## Why This Note Exists

Beginners often get stuck because two providers can support the same concept while using different message shapes and terminology.

The goal is to separate the stable idea from the changing wire format.

## Stable Idea

Across providers, the durable concept is:

1. you define tools
2. the model requests a tool
3. your application executes it
4. you return the result
5. the model continues

That application pattern matters more than the exact JSON wrapper.

## OpenAI

In the modern OpenAI flow for new builds:

- the Responses API is the recommended default for new projects
- custom function tools are defined in the `tools` array
- function tools use JSON Schema-like parameter definitions
- the application reads `function_call` output items and sends back `function_call_output`

This is a strong fit when you want:

- modern OpenAI primitives
- one interface for tool-enabled responses
- compatibility with built-in tools and related platform features

## Anthropic

In Anthropic's tool-use flow:

- tools are sent with names, descriptions, and `input_schema`
- client tools are executed on your side
- Claude returns `tool_use` content blocks
- your application responds with `tool_result` blocks

This is a strong fit when you want:

- Claude-based applications
- detailed client-tool descriptions
- a clear content-block-based tool protocol

## Practical Advice

- learn the shared loop first
- then learn each provider's message shape
- keep your internal tool registry separate from provider-specific payload builders

That last point is important. If you design your internal tool model well, moving between providers becomes much easier.
