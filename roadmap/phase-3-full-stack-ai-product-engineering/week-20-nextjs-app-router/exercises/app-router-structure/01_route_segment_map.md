# Exercise: Route Segment Map

## Goal

Practice thinking in App Router segments instead of one large UI tree.

## Scenario

You are building a support operations portal with:

- a dashboard
- a tickets list
- a ticket detail page
- an intake preview page
- three internal API routes

## Task

Sketch the route structure before coding.

Strong answer:

```text
app/
|-- layout.js
|-- page.js
|-- loading.js
|-- not-found.js
|-- compose/
|   `-- page.js
|-- tickets/
|   |-- loading.js
|   |-- page.js
|   `-- [ticketId]/
|       `-- page.js
`-- api/
    |-- intake-preview/
    |   `-- route.js
    `-- tickets/
        |-- route.js
        `-- [ticketId]/
            `-- route.js
```

## What You Should Notice

- UI routes live under `app/`
- route handlers also live under `app/api/`
- layouts wrap nested routes
- dynamic detail routes are explicit
- loading and not-found behavior belong to route structure, not random components
