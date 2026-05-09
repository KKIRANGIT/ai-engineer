# Week 13 Exercises

Back to [Week 13 README](../README.md)

## Purpose

These exercises isolate the core mechanics of tool use before you study the larger project.

The point is not to memorize provider syntax. The point is to become fluent in:

- reading tool-call shaped outputs
- designing clear schemas
- validating arguments before execution
- comparing provider payload styles

## Exercise Order

Work through these folders in order:

1. `tool-loop-mental-model/`
2. `schema-design/`
3. `validation-and-safety/`
4. `provider-payloads/`

## Folder Guide

### `tool-loop-mental-model/`

Use these files to understand the difference between:

- a model requesting a tool
- the application deciding whether to execute it
- the application returning results

### `schema-design/`

Use these files to compare weak and strong tool definitions.

Focus on:

- tool descriptions
- parameter shape
- required fields
- when tool scope is too broad

### `validation-and-safety/`

Use these files to study why model arguments must still be treated as untrusted input.

Focus on:

- type checks
- range checks
- authorization-like boundaries
- safe failure patterns

### `provider-payloads/`

Use these files to compare how the same tool ideas are expressed for:

- OpenAI function tools
- Anthropic client tools

## How To Use The Exercises Properly

For each file:

1. run it
2. read the output
3. explain what the code is teaching
4. change one small thing and observe what breaks or improves

Do not rush to the project before the loop and validation logic feel obvious.

## What Success Looks Like

You are ready for the main project when you can:

- explain why a call should or should not execute
- describe the parts of a good tool schema
- show how validation protects the system
- compare provider payload shapes without confusion
