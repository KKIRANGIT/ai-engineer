# Exercise: Choose Server Or Client

## Goal

Practice boundary decisions before you code them.

## Questions

For each item below, decide whether it should usually be a server component or a client component in Week 20.

### 1. Dashboard stats derived from existing ticket data

Strong answer:

- server component

Reason:

- no browser interactivity is needed
- the server can prepare the view directly

### 2. Search form that updates URL filters while the user types

Strong answer:

- client component

Reason:

- it needs browser-side interaction and router updates

### 3. Ticket detail page resolved from a route parameter

Strong answer:

- server page

Reason:

- the server can read the route parameter and fetch the detail view directly

### 4. Intake preview form that submits data to a route handler

Strong answer:

- client component inside a server page

Reason:

- the page can stay server-rendered
- only the interactive form behavior needs the browser

## Rule Of Thumb

Default to server components.

Move to the client only when you need:

- local interactive state
- browser APIs
- event-driven UI behavior
- client-side navigation hooks
