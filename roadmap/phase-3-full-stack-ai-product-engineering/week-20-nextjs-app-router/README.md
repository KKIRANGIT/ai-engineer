# Week 20: Next.js App Router

Back to [Phase 3](../README.md)

## Goal

Learn the default modern architecture for AI product web apps using Next.js App Router, server/client boundaries, layouts, route handlers, and streaming-friendly rendering patterns.

This week is about product structure, not just framework syntax.

## Why This Week Matters

If Week 19 taught you component thinking, Week 20 teaches you application-boundary thinking.

This week matters because product engineering now includes questions such as:

- what should render on the server
- what actually needs to run in the browser
- where URL state should live
- how route handlers fit the app
- how loading and streaming behavior affect UX
- where sensitive logic should stay server-side

Weak understanding here leads to:

- too much client-side code
- confused data-loading patterns
- accidental exposure of server concerns to the browser
- route-handler sprawl
- poor streaming and loading behavior

Week 20 should give you a working mental model for building a real product shell in modern Next.js.

## What This Week Is Actually Training

Week 20 is training six deeper skills:

1. thinking in route segments instead of single-page trees
2. distinguishing server composition from client interactivity
3. using layouts and nested routes to shape product structure
4. using route handlers as application endpoints without overcomplicating the architecture
5. using URL search params as product state where appropriate
6. designing loading and streaming behavior intentionally

The real outcome is not "I made a Next.js app." The real outcome is "I understand how a modern product should be structured in App Router."

## Scope Boundary For This Week

This week focuses on:

- App Router structure
- layouts and nested routes
- server and client component boundaries
- route handlers
- URL-based filtering state
- loading and streaming-friendly UI
- server-safe data and request logic

This week does not require:

- authentication providers
- database integration
- production billing
- advanced cache invalidation
- edge runtime specialization
- full deployment automation

The correct goal is not to cover every Next.js feature. The correct goal is to understand the App Router model well enough that later SaaS features have a solid home.

## Week 20 Outcomes

By the end of this week, you should be able to:

- explain the App Router mental model clearly
- distinguish server and client components with confidence
- use layouts, pages, and dynamic segments correctly
- build a route handler that performs server-side request logic
- use URL search params as a clean source of truth for filters
- design one streaming-friendly path without confusing the user

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 20 workspace
2. official Next.js App Router documentation
3. your own boundary notes on server vs client decisions

Do not learn this week by mixing old Pages Router tutorials with modern App Router docs. That creates avoidable confusion.

## Recommended Official References

Use these official sources as the primary external reference stack:

- Next.js App Router overview: <https://nextjs.org/docs/app>
- Installation and project structure: <https://nextjs.org/docs/app/getting-started/installation>
- Layouts and pages: <https://nextjs.org/docs/app/getting-started/layouts-and-pages>
- Linking and navigating: <https://nextjs.org/docs/app/getting-started/linking-and-navigating>
- Server and Client Components: <https://nextjs.org/docs/app/getting-started/server-and-client-components>
- Route handlers: <https://nextjs.org/docs/app/getting-started/route-handlers>
- Fetching data: <https://nextjs.org/docs/app/getting-started/fetching-data>
- `loading.js` and streaming: <https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming>
- `useSearchParams`: <https://nextjs.org/docs/app/api-reference/functions/use-search-params>
- `notFound`: <https://nextjs.org/docs/app/api-reference/functions/not-found>
- Next.js 16 release: <https://nextjs.org/blog/next-16>

These were chosen because this week depends on current App Router behavior, not older framework assumptions.

## Recommended Project Direction For This Workspace

This workspace uses one realistic but manageable product shell:

- a support operations portal built with App Router

Why this direction was chosen:

- it naturally benefits from nested routes
- it needs both server-rendered and client-interactive sections
- it gives route handlers a clear purpose
- it supports URL-based filters well
- it provides a realistic place to demonstrate streaming-friendly UI

## Project Capabilities This Week Includes

The Week 20 project includes:

- a shared layout and navigation shell
- a server-rendered dashboard page
- a streamed server insight panel
- a searchable tickets page that uses URL search params
- a dynamic ticket detail route
- route handlers for listing tickets, looking up ticket details, and previewing intake triage
- a client-side intake form that calls a route handler
- global loading and not-found experiences
- pure utility modules with Node-based tests

The project stays dependency-light and data-local on purpose so the App Router concepts stay visible.

## Recommended Build Sequence

1. map the route structure
2. define the server/client boundary for each feature
3. build the shared layout and static navigation
4. add the tickets route with URL-driven filtering
5. add dynamic ticket detail routing
6. add route handlers for data and preview logic
7. add one streamed or delayed server-rendered insight panel

## Recommended Daily Breakdown

### Day 1: App Router structure

Focus:

- route segments
- pages
- layouts
- nested navigation

### Day 2: Server and client boundaries

Focus:

- what stays server-side
- what must become interactive
- why client components should stay narrow

### Day 3: URL state and route handlers

Focus:

- search params
- route handlers
- request/response boundaries

### Day 4: Dynamic routes and product detail pages

Focus:

- `[ticketId]`
- not-found behavior
- route-specific data lookup

### Day 5: Loading and streaming behavior

Focus:

- loading UI
- suspense boundaries
- progressive information delivery

### Day 6: Full app assembly

Focus:

- project structure
- UI shell consistency
- data and route flow

### Day 7: Boundary review and documentation

Focus:

- server/client decisions
- route-handler rationale
- what should change in Week 21 when auth arrives

## Hands-On Workspace Structure

```text
week-20-nextjs-app-router/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- app-router-structure/
|   |-- route-handlers-and-data-flow/
|   |-- server-client-boundaries/
|   `-- streaming-and-rendering/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-boundary-review-guide.md
|   `-- 03-deployment-and-config-notes.md
`-- projects/
    `-- support-ops-portal-next/
```

## Exercises

The exercises isolate the parts of Next.js that usually get blurred together by beginners.

You will practice:

- mapping route segments
- choosing server vs client components
- defining route-handler contracts
- using search params as product state
- understanding loading and streaming behavior

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [support-ops-portal-next](projects/support-ops-portal-next/README.md)

This project is a small support operations portal built with App Router. It teaches:

- layouts and page structure
- server-first rendering
- narrow client islands
- dynamic routes
- route handlers
- loading and streamed insight behavior

It is intentionally realistic enough to feel like product work, but small enough that the framework decisions stay understandable.

## Deliverables

By the end of this week, you should have:

- one complete Next.js App Router workspace
- one project with layouts, routes, and route handlers
- one note explaining server/client boundary decisions
- one note explaining URL state and route-handler usage
- one small set of tested pure helpers

## Exit Criteria

You are ready to move to Week 21 only if:

- you can explain the difference between a page, layout, and route handler
- you can justify why a component is server-side or client-side
- you can explain how filters flow through URL search params
- you can describe why sensitive request logic stays in route handlers
- you can explain how loading and streaming improve product behavior
- you can navigate the project structure without confusion

## Common Mistakes To Avoid

- turning large parts of the tree into client components by default
- treating route handlers as a replacement for all architecture decisions
- storing product state in local client state when the URL should own it
- mixing server-only logic into client components
- using streaming and loading UI without a clear user-facing purpose

## Expert Notes That Matter Early

### Server-first thinking reduces frontend complexity

If data lookup and composition can stay on the server, keep them there.

### Client components should be narrow and intentional

A client component is not a badge of sophistication. It is a cost. Use it only when the browser truly needs to own the interaction.

### URL state is product state

Filters, tabs, and views often belong in the URL because they should be shareable, reload-safe, and server-readable.

### Route handlers should have a job

Use them when the app needs request/response logic. Do not create them just because they exist.

### Loading behavior is part of the product

App Router is not only about routes. It is also about how the product feels while data is arriving.

## Final Standard For This Week

The correct outcome of Week 20 is not:

"I know the App Router folder names."

The correct outcome is:

"I can structure a modern Next.js product so that routing, rendering, request handling, and server/client boundaries support a real application cleanly."
