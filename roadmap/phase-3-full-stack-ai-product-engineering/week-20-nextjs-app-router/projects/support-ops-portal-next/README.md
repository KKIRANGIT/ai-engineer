# Support Ops Portal Next

Back to [Week 20 README](../../README.md)

## Purpose

This project is the practical centerpiece of Week 20.

It teaches App Router through one realistic product shell instead of disconnected route examples. The app models a small support operations portal where a user can:

- view a dashboard
- inspect queue health
- filter tickets using the URL
- open a ticket detail page
- submit an intake draft for a server-side preview

## Why This Project Exists

A Next.js fundamentals project should make architecture decisions visible.

This app was chosen because it naturally requires:

- a shared layout
- nested routes
- server-rendered pages
- narrow client components
- route handlers
- search params
- dynamic routes
- one streaming-friendly section

That is enough to learn App Router well without immediately dragging in auth, databases, or billing.

This workspace stays JavaScript-first on purpose. The goal this week is to isolate App Router thinking before layering in the heavier platform concerns that arrive in later Phase 3 weeks.

## Learning Targets

By studying this project, you should understand:

- why most of the app stays server-rendered
- why the filter form becomes a client component
- why route handlers own request logic
- how URL state shapes the tickets page
- how a Suspense boundary can improve the dashboard experience

## Project Structure

```text
support-ops-portal-next/
|-- README.md
|-- app/
|   |-- api/
|   |   |-- intake-preview/
|   |   |   `-- route.js
|   |   `-- tickets/
|   |       |-- route.js
|   |       `-- [ticketId]/
|   |           `-- route.js
|   |-- compose/
|   |   `-- page.js
|   |-- tickets/
|   |   |-- [ticketId]/
|   |   |   `-- page.js
|   |   |-- loading.js
|   |   `-- page.js
|   |-- globals.css
|   |-- layout.js
|   |-- loading.js
|   |-- not-found.js
|   `-- page.js
|-- components/
|   |-- IntakePreviewForm.jsx
|   |-- QueueSearchForm.jsx
|   |-- QueueStatsPanel.jsx
|   |-- RouteCardGrid.jsx
|   |-- StreamedInsightsPanel.jsx
|   |-- TicketListTable.jsx
|   `-- TopNav.jsx
|-- lib/
|   |-- data.js
|   |-- delay.js
|   `-- intake.js
|-- next.config.mjs
|-- package.json
`-- tests/
    `-- data-utils.test.mjs
```

## How To Run Later

When you want to run the browser app locally:

1. install dependencies with `npm install`
2. start the dev server with `npm run dev`

For the logic tests that do not require the Next runtime:

1. run `node --test`

## Key Files To Study First

### `app/layout.js`

Study this to understand:

- shared shell structure
- layout-level product chrome
- navigation wrapping child routes

### `app/tickets/page.js`

Study this to understand:

- server-side route rendering
- `searchParams`
- URL-driven filtering

### `components/QueueSearchForm.jsx`

Study this to understand:

- the narrow client island pattern
- router updates from the browser
- why the rest of the route can stay server-rendered

### `app/api/intake-preview/route.js`

Study this to understand:

- server-side request logic
- JSON request validation
- predictable response shape

### `components/StreamedInsightsPanel.jsx`

Study this to understand:

- async server component behavior
- product-friendly progressive rendering

## Design Standard For This Project

The real quality bar is architectural clarity:

- explicit route structure
- clear server/client boundaries
- narrow client code
- request logic on the server
- readable utility functions
- comments only where they clarify intent

## What To Notice As You Read

- pages stay mostly server-rendered
- interactivity is isolated to specific components
- route handlers are application endpoints, not random utility buckets
- pure helper functions remain testable without the framework runtime

## Suggested Study Order

1. `lib/data.js`
2. `app/layout.js`
3. `app/page.js`
4. `app/tickets/page.js`
5. `components/QueueSearchForm.jsx`
6. `app/tickets/[ticketId]/page.js`
7. `app/api/intake-preview/route.js`
8. `components/IntakePreviewForm.jsx`

## Final Learning Check

After studying the project, you should be able to answer:

- which routes are server-rendered
- which components are client components and why
- why the filters live in the URL
- what the route handlers are responsible for
- how the streaming-friendly dashboard section improves the product feel
