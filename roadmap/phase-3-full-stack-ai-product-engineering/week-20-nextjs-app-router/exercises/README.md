# Week 20 Exercises

Back to [Week 20 README](../README.md)

## Purpose

These exercises are designed to teach App Router as an application-structure system, not as a list of file conventions.

The order matters. Start with route structure, then boundaries, then route handlers, then streaming and rendering decisions.

## Exercise Groups

### 1. App Router structure

Files:

- [01_route_segment_map.md](app-router-structure/01_route_segment_map.md)
- [02_layout_loading_not_found_notes.md](app-router-structure/02_layout_loading_not_found_notes.md)

Focus:

- thinking in route segments
- understanding where layouts, pages, loading UIs, and not-found screens fit

### 2. Server and client boundaries

Files:

- [01_choose_server_or_client.md](server-client-boundaries/01_choose_server_or_client.md)
- [02_boundary_example.jsx](server-client-boundaries/02_boundary_example.jsx)

Focus:

- deciding which logic belongs on the server
- keeping client islands narrow

### 3. Route handlers and data flow

Files:

- [01_route_handler_contract.js](route-handlers-and-data-flow/01_route_handler_contract.js)
- [02_search_params_url_state.md](route-handlers-and-data-flow/02_search_params_url_state.md)

Focus:

- request and response shape
- URL-driven filtering state
- server-side logic behind interactive flows

### 4. Streaming and rendering

Files:

- [01_suspense_streaming_notes.md](streaming-and-rendering/01_suspense_streaming_notes.md)
- [02_freshness_decisions_checklist.md](streaming-and-rendering/02_freshness_decisions_checklist.md)

Focus:

- progressive delivery
- loading states
- freshness vs simplicity

## How To Use These Exercises

For each file:

1. read the explanation
2. explain the decision in your own words
3. compare it to the main project
4. identify what architectural instinct the exercise is training

These exercises exist to reduce framework confusion before you study the project itself.
