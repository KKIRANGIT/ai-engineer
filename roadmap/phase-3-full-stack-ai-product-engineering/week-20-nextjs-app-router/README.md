# Week 20: Next.js App Router

Back to [Phase 3](../README.md)

## Goal

Learn the default modern architecture for AI product web apps using Next.js App Router, server/client boundaries, route handlers, and streaming-friendly full-stack patterns.

## Why This Week Matters

If React teaches you component thinking, Next.js teaches you product-system thinking for the web.

This week matters because product engineering decisions now include:

- what runs on the server
- what runs on the client
- what should be streamed
- where data fetching belongs
- how route handlers fit the app

Weak understanding here leads to:

- unnecessary client complexity
- poor data-loading patterns
- confused rendering boundaries
- harder deployment and performance tuning

## Week 20 Outcomes

By the end of this week, you should be able to:

- explain the App Router mental model
- distinguish server and client components
- use route handlers for backend logic where appropriate
- understand rendering and caching decisions at a practical level
- stream a useful AI interaction or loading path
- deploy a small Next.js app cleanly

## What To Learn

## 1. App Router mental model

You should understand:

- file-system routing
- layouts
- pages
- route handlers
- server-first architecture

Important mindset:

Do not import old Pages Router assumptions into App Router design.

## 2. Server vs client components

This is one of the central concepts of the week.

Learn:

- server components for data and non-interactive composition
- client components for interactivity, local state, and browser APIs
- how the boundary affects bundle size and architecture

Good question to ask:

- does this logic truly need to run in the browser

## 3. Data flow and route handlers

You should understand when to:

- fetch on the server
- use route handlers
- separate product routes from standalone backend services

Important rule:

Keep the architecture as simple as the product allows.

## 4. Rendering, caching, and freshness

At a practical level, learn:

- static vs dynamic behavior
- where caching helps
- when AI-backed routes should avoid stale assumptions

You do not need to master every caching edge case this week, but you do need a working model of why rendering strategy matters.

## 5. Streaming patterns

AI product UX often benefits from:

- streamed text output
- progressive UI states
- partial rendering

Next.js is a strong environment for learning how streamed experiences affect the app shell.

## 6. Deployment model

You should understand:

- build step
- environment variables
- production route behavior
- why some code belongs server-side only

## Best Learning Sequence For This Week

1. App Router structure
2. server/client boundary
3. route handlers
4. rendering and caching
5. streaming interaction
6. deployment

## Recommended Daily Breakdown

### Day 1: App Router basics

Focus:

- layouts
- pages
- route structure

### Day 2: Server and client components

Focus:

- interaction boundaries
- state boundaries

### Day 3: Route handlers and data flow

Focus:

- internal API path
- request-response design inside the app

### Day 4: Streaming pattern

Focus:

- loading and partial output
- AI interaction shell

### Day 5: Rendering and caching decisions

Focus:

- freshness vs performance

### Day 6: Build the full app shell

### Day 7: Deploy and document boundaries

## Build Plan

Build one small Next.js app with:

- layout shell
- server-rendered sections
- at least one client-interactive section
- one route handler
- one AI-related or streamed interaction path

## Deliverables

- deployed Next.js app
- one note explaining server vs client boundaries
- one note explaining route-handler usage

## Exit Criteria

- you can explain App Router architecture clearly
- you know what should stay server-side vs client-side
- you can add a route handler without confusion
- you can build one streaming-friendly interaction path

## Common Mistakes To Avoid

- marking too much of the tree as client components
- treating route handlers as a substitute for architectural thinking
- importing server-only assumptions into client code
- building streaming UX without clear loading states

## Expert Notes That Matter Early

### Server-first thinking reduces complexity

Not every piece of app logic needs to live in the browser.

### Boundaries shape maintainability

Clear server/client boundaries make AI product code easier to reason about.

### Streaming is a product behavior, not just a transport feature

Users feel the difference when information arrives progressively and clearly.

## Final Standard For This Week

The correct outcome of Week 20 is not "I made a Next.js app."

The correct outcome is:

"I understand how to structure a modern Next.js product so that rendering, routing, streaming, and server/client boundaries support a real AI application."
