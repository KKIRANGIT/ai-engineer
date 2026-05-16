# Exercise: URL State For Filters

## Goal

Understand when filters belong in the URL instead of local component state.

## Good Reasons To Use URL State

- the current view should be shareable
- the current view should survive refreshes
- the server should be able to read the same state
- the route itself represents the product view

## Week 20 Example

For the tickets route, these filters belong in the URL:

- `q`
- `status`
- `priority`

This is better than keeping them only in client state because:

- the server page can filter correctly
- a teammate can share the exact filtered view
- navigation history becomes meaningful

## Warning

Not every bit of UI state belongs in the URL.

Examples of state that can stay local:

- whether a help tooltip is open
- whether a local panel is collapsed
