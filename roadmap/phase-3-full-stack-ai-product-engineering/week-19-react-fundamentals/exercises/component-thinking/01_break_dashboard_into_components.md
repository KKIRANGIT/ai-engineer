# Exercise: Break A Dashboard Into Components

## Goal

Practice component decomposition before writing the full app.

## Scenario

You are building a support dashboard with:

- a header
- queue statistics
- queue filters
- a ticket list
- a selected ticket detail panel
- a ticket creation form
- a recent activity feed

## Task

Before coding, answer these questions:

1. Which parts of the page are reusable UI sections?
2. Which parts only display data?
3. Which parts need local interactive state?
4. Which state must be shared across multiple sections?
5. Which values can be derived instead of stored?

## Strong Answer Shape

A strong answer usually looks something like this:

- `App` owns the shared queue data, filters, and selected ticket id.
- `TicketComposer` owns its temporary draft input values.
- `StatsPanel` receives already-computed numbers as props.
- `QueueFilters` receives filter values and update handlers.
- `TicketList` receives visible tickets and selection handlers.
- `SelectedTicketPanel` receives the selected ticket object.
- `ActivityFeed` receives a derived activity list.

## What You Should Notice

The screen is not divided by visual boxes alone. It is divided by:

- state ownership
- data flow
- interaction responsibility

That is the React mental model you need this week.
