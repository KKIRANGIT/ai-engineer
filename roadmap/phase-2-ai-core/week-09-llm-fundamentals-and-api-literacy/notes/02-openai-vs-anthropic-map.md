# OpenAI vs Anthropic Map

Back to [Week 09](../README.md)

## Why This Comparison Matters

A weak Week 09 outcome is:

"These APIs are basically the same."

That is too vague to be useful.

The stronger outcome is:

"These APIs solve similar problems, but they structure requests, state, and outputs differently, and I can adapt to those differences intentionally."

## Practical Differences

### OpenAI Responses

Useful concepts:

- `instructions`
- `input`
- `output`
- `output_text`
- `previous_response_id`
- tool-capable response items

This interface encourages thinking in terms of response objects and stateful chaining options.

### Anthropic Messages

Useful concepts:

- `system`
- `messages`
- `content` blocks
- `stop_reason`
- stateless multi-turn conversations

This interface encourages thinking in terms of explicitly sent conversational history and content blocks.

## Shared Similarities

Both providers require you to think about:

- model choice
- prompt or instruction quality
- token usage
- output inspection
- error handling
- tool or extension boundaries

## Good Engineering Attitude

Do not try to collapse both providers into a fake identical abstraction too early.

A better approach is:

1. understand each provider natively
2. normalize only the pieces your application truly needs
3. keep provider-specific details visible where they matter
