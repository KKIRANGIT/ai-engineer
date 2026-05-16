# System Overview

## Components

- Next.js web app for product UI
- auth provider for sessions and user identity
- application server and route handlers
- database for tickets, usage, and billing state
- background worker for slow analysis jobs
- AI provider for analysis and summarization
- monitoring and analytics services

## Primary Flows

1. User signs in and enters the workspace.
2. User uploads or selects a support dataset.
3. App creates an analysis request and may enqueue slow work.
4. Worker stores results and emits usage and monitoring signals.
5. Product UI shows the result and gates features by plan.
