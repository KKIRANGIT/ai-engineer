# TypeScript Reference Layer

Back to [Reading List API](../README.md)

## Purpose

This folder is not the main runtime entrypoint. It is a teaching layer.

The main API runs as plain JavaScript so the project stays easy to execute in a minimal environment. This folder shows how the same backend ideas can be described more explicitly in TypeScript.

## What To Notice

Read these files with one question in mind:

"What became clearer because the type information is explicit?"

Pay attention to:

- the `Book` shape
- the `CreateBookInput` contract
- the service method return types
- the union used for route results

That is the value TypeScript adds. It makes intent harder to misunderstand.
