# Current Tech Notes

Back to [Roadmap Index](../README.md)

## Why This File Exists

A roadmap becomes stale when it mixes timeless principles with unstable version assumptions.

This file is the versioning and stack-policy layer for the roadmap. Its purpose is not to make you obsess over versions. Its purpose is to stop you from learning against outdated defaults or making fragile tooling choices.

## Current Assumptions

These assumptions were validated against official documentation as of May 9, 2026.

- Python `3.14` is the latest feature release series. Python.org shows `3.14.x` as the latest feature line and `3.14.4` as a current release in that series.
- Node.js `v24` is the `Active LTS` line and is the best default for production-style learning projects. Node.js `v25` is `Current`, but LTS should be the default unless you need a Current-only feature.
- React `19` is stable, and React `19.2` is already part of the active ecosystem.
- Next.js `16` is the current major release line.
- OpenAI recommends the Responses API for new projects instead of defaulting to Chat Completions.
- Anthropic's modern tool-use guidance centers on the Messages API with explicit tool definitions and versioned tool types.
- Supabase recommends `HNSW` as the general default index choice for most `pgvector` use cases.

## Versioning Policy For This Roadmap

Use this policy throughout the roadmap.

### Rule 1: Learn against the modern major workflow

Examples:

- OpenAI Responses API instead of designing new projects around Chat Completions
- Next.js App Router instead of older Pages Router-first learning
- React 19 async and UX patterns instead of older "everything is useEffect and callbacks" habits

### Rule 2: Build on the newest stable version your dependencies actually support

This is the real-world engineering rule.

Do not blindly use the newest release if:

- your dependencies lag support
- your hosting or templates are not ready
- the ecosystem is still shaking out compatibility issues

Use the latest stable version that keeps your project smooth, debuggable, and well-documented.

### Rule 3: Prefer LTS lines for production-style learning

That mainly applies to runtimes like Node.js.

Reason:

- better ecosystem support
- fewer incompatibility surprises
- more representative of production setups

### Rule 4: Separate learning experiments from portfolio builds

It is fine to test bleeding-edge features in an experiment repo.

It is usually not wise to anchor your main milestone portfolio project to unstable tooling unless the point of the project is specifically to demonstrate that tooling.

## Practical Version Recommendations

### Python

Recommended use:

- learn the `3.14` feature set
- use `3.14` when your dependencies support it cleanly
- if a library stack lags, stepping down one supported version for a production-style project is acceptable

Do not:

- freeze yourself on very old Python because a tutorial used it
- treat every new runtime feature as mandatory for every project

### Node.js

Recommended use:

- default to `v24` LTS for app work
- only adopt `Current` if you have a clear reason and understand the support tradeoff

Do not:

- optimize for novelty over stability in your main learning projects

### React and Next.js

Recommended use:

- learn React 19 mental models directly
- learn Next.js 16 App Router directly
- understand modern caching and server/client boundaries early

Important mindset:

- do not learn React as a bundle of outdated workarounds
- do not build App Router apps with Pages Router mental models

### OpenAI

Recommended use:

- default to the Responses API for new work
- use structured outputs when downstream code depends on schema validity
- use provider tools or custom functions intentionally rather than as demo decorations

Important mindset:

- use the provider’s current primary API shape
- avoid building new systems on legacy defaults just because older tutorials still dominate search results

### Anthropic

Recommended use:

- learn the Messages API directly
- learn the difference between client tools and server tools
- be aware that Anthropic-defined tools use versioned types

Important mindset:

- tool use is part of system design, not just a feature flag

### Retrieval and Vectors

Recommended use:

- learn `pgvector`
- use `HNSW` as the default index recommendation unless you have a specific reason otherwise
- compare hosted retrieval against self-managed retrieval to understand tradeoffs

Important mindset:

- vector storage is only one part of retrieval quality
- chunking, filtering, reranking, and evals often matter more than the storage layer brand

## Environment Strategy

Use two environments:

### Stable build environment

This is for:

- milestone projects
- portfolio work
- demos you want others to run

Choose:

- LTS runtimes
- well-supported package versions
- minimal experimental flags

### Exploration environment

This is for:

- trying new features
- testing provider updates
- benchmarking small experiments

Choose:

- isolated repos
- easy rollback
- short-lived experiments

This separation prevents your main roadmap output from being derailed by ecosystem churn.

## How To Think About "Latest"

"Latest" does not automatically mean "best default."

Use this decision order:

1. Is it current enough to reflect modern practices?
2. Is it stable enough for your intended project?
3. Is the documentation mature enough to support fast learning?
4. Is the ecosystem support good enough to avoid time waste?

If all four are true, use it.

## Current High-Confidence Defaults

If you want one conservative but modern baseline:

- Python `3.14`
- Node.js `v24` LTS
- React `19`
- Next.js `16`
- PostgreSQL / Supabase
- OpenAI Responses API
- Anthropic Messages API
- `pgvector` with `HNSW`

For the reasoning behind these defaults, see [2026 Stack Update](03-2026-stack-update.md). For official links, see [Official Reference Links](../90-reference/12-official-reference-links.md).
