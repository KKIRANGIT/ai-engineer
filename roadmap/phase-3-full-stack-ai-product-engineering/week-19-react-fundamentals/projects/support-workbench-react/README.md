# Support Workbench React

Back to [Week 19 README](../../README.md)

## Purpose

This project is the practical centerpiece of Week 19.

It teaches React fundamentals through one realistic dashboard instead of disconnected examples. The app models a small support operations workbench where a user can:

- review queue health
- filter tickets
- create a new ticket
- select a ticket for details
- inspect a recent activity feed

## Why This Project Exists

A React fundamentals project should make state ownership visible.

This app was chosen because it naturally requires:

- shared state
- local draft state
- derived counts
- filtered lists
- selection state
- conditional rendering
- controlled forms
- one or two legitimate effects

That is enough to learn React well without immediately dragging in backend complexity.

This workspace stays JavaScript-first on purpose. The goal this week is to isolate React thinking before layering in the heavier full-stack and TypeScript concerns that arrive later in Phase 3.

## Learning Targets

By studying this project, you should understand:

- why `App` owns the main queue state
- why `TicketComposer` owns its temporary form draft
- how filters and stats are derived
- why `localStorage` persistence belongs in an effect
- how a dashboard shell can stay readable through component separation

## Project Structure

```text
support-workbench-react/
|-- README.md
|-- index.html
|-- package.json
|-- src/
|   |-- App.jsx
|   |-- main.jsx
|   |-- sampleData.js
|   |-- styles.css
|   |-- utils.js
|   `-- components/
|       |-- ActivityFeed.jsx
|       |-- DashboardShell.jsx
|       |-- QueueFilters.jsx
|       |-- SelectedTicketPanel.jsx
|       |-- StatsPanel.jsx
|       |-- TicketCard.jsx
|       |-- TicketComposer.jsx
|       `-- TicketList.jsx
`-- tests/
    `-- app-utils.test.mjs
```

## How To Run Later

This project is written as a standard React app.

When you want to run it locally with the browser UI:

1. install dependencies with `npm install`
2. start the dev server with `npm run dev`

For the logic tests that do not require React packages at runtime:

1. run `node --test`

## Key Files To Study First

### `src/App.jsx`

This is the state orchestration layer.

Study it to understand:

- shared state
- derived values
- effect boundaries
- how child components communicate upward

### `src/utils.js`

This file contains the pure data logic.

Study it to understand:

- validation
- filtering
- stats derivation
- activity feed derivation

### `src/components/TicketComposer.jsx`

Study this for:

- controlled form state
- local validation feedback
- clean submit handling

### `src/components/QueueFilters.jsx`

Study this for:

- filter controls driven by parent state
- controlled search and select inputs

## Design Standard For This Project

The UI should feel intentional, but the real quality bar is architectural clarity:

- explicit props
- clear state ownership
- minimal duplicated truth
- effects only where justified
- code readable enough for a beginner to follow

## What To Notice As You Read

- presentational components stay mostly dumb
- the top-level app composes the workflow
- the helper functions are testable without the UI
- CSS is used to create a coherent product feel without hiding the logic

## Suggested Study Order

1. `src/utils.js`
2. `src/App.jsx`
3. `src/components/TicketComposer.jsx`
4. `src/components/QueueFilters.jsx`
5. `src/components/TicketList.jsx`
6. `src/components/SelectedTicketPanel.jsx`
7. `src/styles.css`

## Final Learning Check

After studying the project, you should be able to answer:

- what the source of truth is
- which values are derived
- which effects are legitimate
- which component boundaries would still hold if the UI grew larger
