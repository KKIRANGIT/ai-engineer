# Deployment And Config Notes

## What This Week Should Teach

You do not need a production deployment pipeline this week, but you should understand the shape of deployment concerns.

## Core Ideas

- server-side code stays on the server
- route handlers run on the server
- environment variables should not be exposed accidentally to client components
- build output and runtime behavior matter more once real data and auth arrive

## Local Project Notes

The Week 20 project uses local data and pure helper modules so the App Router patterns are easy to inspect.

That means:

- no database setup is required
- no external API keys are required
- route handlers remain deterministic and readable

## What Changes In Later Weeks

In Week 21 and beyond, the same structure will need to accommodate:

- authentication
- user-specific data
- protected routes
- real persistence
- billing-aware behavior

That is why Week 20 focuses so heavily on boundaries now.
