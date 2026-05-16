# Exercise: Freshness Decisions Checklist

## Goal

Build a basic rendering and freshness instinct.

## Ask These Questions

1. Does this view need the newest possible data every time?
2. Would a slightly older version be acceptable for a short period?
3. Is the content user-specific or shared?
4. Is the route mostly static, mostly dynamic, or mixed?
5. Is the complexity of advanced caching worth it this week?

## Week 20 Standard

This week is not about mastering every cache mode.

This week is about being able to say:

- this section is server-rendered
- this section is interactive
- this route reads URL state
- this slower section can stream
- this request logic belongs in a route handler

That is already a strong foundation.
