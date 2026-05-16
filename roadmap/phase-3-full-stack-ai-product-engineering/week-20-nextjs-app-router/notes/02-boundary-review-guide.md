# Boundary Review Guide

Use this when reviewing any App Router feature.

## Server Component Review

Ask:

- can this be rendered from server data without browser state?
- does this code need access to secrets or server-only logic?
- would moving this to the client increase bundle cost for no real benefit?

## Client Component Review

Ask:

- does this need local state, browser APIs, or router hooks?
- can the client logic be isolated to a smaller child component?

## Route Handler Review

Ask:

- is there real request/response logic here?
- should this behavior stay inside the application boundary?
- does the payload shape stay predictable?

## URL State Review

Ask:

- should this view be shareable?
- should refresh preserve the current state?
- should the server be able to read the same state?

If yes, the URL probably deserves to own that state.

## Final Review Question

If you deleted the client code from a route, would the server-rendered shell still make sense?

If the answer is no, the route may be too client-heavy for the current need.
