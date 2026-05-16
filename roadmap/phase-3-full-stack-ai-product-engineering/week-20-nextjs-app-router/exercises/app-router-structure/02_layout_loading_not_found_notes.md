# Exercise: Layout, Loading, and Not Found

## Goal

Understand the job of each App Router file instead of treating them as interchangeable.

## Layout

Use a layout when multiple routes should share:

- navigation
- shell structure
- global styling
- repeated product chrome

## Loading

Use `loading.js` when a route segment should show an immediate placeholder while server work is still resolving.

This is useful when:

- the user navigates between routes
- server-rendered content may take noticeable time
- you want the product to feel responsive instead of frozen

## Not Found

Use `notFound()` when a route parameter does not map to a real resource.

That is stronger and clearer than rendering a vague empty screen.

## Week 20 Connection

In the main project:

- the shared shell belongs in `layout.js`
- ticket loading belongs in `tickets/loading.js`
- missing ticket ids should trigger `notFound()`
