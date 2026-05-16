# Week 20 Plan

Back to [Week 20 README](../README.md)

## Objective

Finish this week with one small Next.js App Router product shell whose structure and boundaries you can explain clearly.

## Suggested Flow

### Step 1

Read:

- the Week 20 README
- the exercises README
- the official Next.js docs on layouts, server/client components, and route handlers

### Step 2

Do the structure and boundary exercises first.

You should be able to answer:

- which routes exist
- which components stay on the server
- which components become client islands

### Step 3

Read the project README and inspect:

- `app/layout.js`
- `app/page.js`
- `app/tickets/page.js`
- `app/api/tickets/route.js`
- `components/QueueSearchForm.jsx`

### Step 4

Explain the app in writing:

- how the layout wraps the routes
- how search params drive the tickets page
- how route handlers fit the app
- why the intake preview form is client-side

### Step 5

Run the Node tests for the pure utility logic.

This will not verify the full browser app, but it will verify the filter, stats, and intake-preview logic that the app depends on.

## What Success Looks Like

You are not done because the folder names look correct.

You are done when you can explain:

- why the boundary decisions were made
- where request logic lives
- where streaming helps the product
- what would need to change once authentication is introduced next week
