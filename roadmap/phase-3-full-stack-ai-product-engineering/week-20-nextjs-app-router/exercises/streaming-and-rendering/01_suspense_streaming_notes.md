# Exercise: Suspense And Streaming Notes

## Goal

Understand what streaming is doing for the user.

## Core Idea

With App Router, some content can arrive later without blocking the whole page shell.

That means:

- the layout can render quickly
- critical context can appear first
- slower sections can fill in afterward

## When This Helps

- AI summaries
- analytics panels
- slow server-generated insights
- content that is useful but not required for first interaction

## Week 20 Example

In the main project, the dashboard shows a streamed insight panel with an intentional server delay.

That is not because delays are good.

It is there to teach this product behavior:

- the page shell should stay useful even when one section is slower
