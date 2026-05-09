# AI Engineer Roadmap to $10K+/Month

**12 Months. 5 Phases. Your Path to Freedom.**

This Markdown version preserves the original roadmap content and reorganizes it for readability in Markdown preview.

## Snapshot

- Starting point: Some coding skills
- Target identity: AI Engineer + Product Builder
- End goal: $10K+/month

| Phase | Focus | Weeks | Income Target |
| --- | --- | --- | --- |
| Phase 1 | Foundation | 1-8 | $0/month |
| Phase 2 | AI Core | 9-18 | $0/month |
| Phase 3 | Full-Stack | 19-28 | $0-500/month |
| Phase 4 | Build | 29-38 | $500-3K/month |
| Phase 5 | Earn | 39-48 | $10K+/month |

## How To Use This Roadmap

- Treat each week as a build week, not just a study week.
- Do not move on without shipping the milestone project or exercise for that stage.
- Keep every meaningful project public, documented, and live.
- If you are learning part-time, stretch each "week" into 2-3 weeks rather than skipping milestones.
- If a named tool changes over time, keep the same skill goal and swap in a modern equivalent.

## Phase 1: Foundation

**Weeks:** 1-8  
**Goal:** Build the base that every AI product sits on.

### Week 1: Python Deep Dive

- Syntax, data types, loops, functions
- OOP (classes, objects, inheritance)
- File I/O, error handling
- Do: 100 exercises on exercism.io
- Build: CLI todo app
- Push everything to GitHub

### Week 2: APIs and HTTP

- REST APIs, HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- Python `requests` library
- JSON parsing and handling
- Auth tokens and API keys
- Do: Consume 3 public APIs (weather, GitHub, news)
- Build: Python API wrapper script

### Week 3: Git + Linux + DevOps Basics

- Git (branch, merge, rebase, cherry-pick)
- GitHub (PRs, issues, actions)
- Linux CLI (navigate, SSH, permissions)
- Environment variables (`.env` files)
- Do: Set up a VPS (DigitalOcean $5/mo)
- Result: Active GitHub profile starts building

### Week 4: Databases and SQL

- SQL basics (`SELECT`, `JOIN`, `GROUP BY`, `INDEX`)
- PostgreSQL setup and usage
- Supabase (free tier, hosted Postgres)
- Data modeling (tables, relations, foreign keys)
- Do: 30 SQL query exercises
- Build: CRUD app with Supabase backend

### Week 5: Python Advanced + Data

- Async / await (`asyncio`)
- Decorators and generators
- Pandas (dataframes, filtering, grouping)
- Numpy basics
- Do: Build an async API scraper
- Build: Data pipeline that processes CSV

### Week 6: Cloud and Deployment

- Vercel (deploy frontend free)
- Railway (deploy backend free)
- Docker (build + run containers)
- AWS S3 (file storage)
- Do: Deploy 2 projects with live URLs
- Result: Everything you build is now live

### Week 7: JavaScript + Node.js

- ES6+ (arrow functions, destructuring, spread, modules)
- Async JS (promises, `async`/`await`, `fetch`)
- Node.js + npm ecosystem
- Express.js (build REST APIs)
- Do: Build a REST API with Express + PostgreSQL
- Build: API with auth endpoint

### Week 8: Foundation Project (Milestone)

- Plan: Simple full-stack app idea
- Build: Frontend + backend + database
- Deploy: Live URL on Vercel/Railway
- Document: Write clean README on GitHub
- Portfolio Project #1 complete
- Example: Expense tracker / Link shortener

### Phase 1 Outcome

- You can build and deploy full-stack apps
- You have an active GitHub
- You understand APIs, databases, cloud
- You are ready for AI

## Phase 2: AI Core

**Weeks:** 9-18  
**Goal:** Master the skills clients actually pay for.

### Week 9: LLM Fundamentals

- How LLMs work (tokens, context, temperature)
- System prompts vs user prompts
- Claude API (Anthropic): read all docs
- OpenAI API: read all docs
- Do: Call Claude API with 20 different prompts
- Understand every single parameter

### Week 10: Prompt Engineering (Pro Level)

- Chain-of-thought prompting
- Few-shot and zero-shot techniques
- XML tags for structured output
- Role prompting and persona setting
- Output format control (JSON, Markdown)
- Do: Read `docs.anthropic.com/prompt-engineering`
- Build: Reusable prompt template library

### Week 11: Vector Databases and Embeddings

- What are embeddings? (text -> numbers)
- Cosine similarity (how semantic search works)
- Pinecone (hosted vector DB)
- Supabase pgvector (free, built-in)
- Do: Index 1000 documents in Pinecone
- Build: Semantic search engine

### Week 12: RAG (Retrieval-Augmented Generation)

- What is RAG? (give AI access to your data)
- RAG pipeline:
  1. Upload document
  2. Chunk it into pieces
  3. Convert chunks to embeddings
  4. Store in vector DB
  5. User asks question
  6. Find relevant chunks
  7. Send chunks + question to LLM
- Chunking strategies (size, overlap)
- Reranking with Cohere
- LangChain basics
- Build: PDF Q&A chatbot (real product)

### Week 13: AI Agents Basics

- What is an agent? (AI that takes actions)
- Tool use / function calling
- Agent loop (think -> act -> observe -> repeat)
- Claude `tool_use` feature (read docs fully)
- Do: Build agent that searches web + answers
- Build: Simple ReAct agent

### Week 14: Advanced Agents + Orchestration

- Multi-agent systems (agents talking to agents)
- LangGraph (agent workflow graphs)
- CrewAI (role-based agent teams)
- Streaming responses (real-time output)
- Agent memory (short-term + long-term)
- Do: Build 2-agent pipeline
- Agent 1: Research -> Agent 2: Write
- Build: Automated content pipeline

### Week 15: Fine-Tuning and Evals

- When to use RAG vs fine-tuning
- OpenAI fine-tuning API
- Hugging Face (open source models)
- Evaluation pipelines (measure quality)
- Do: Fine-tune small model for specific task
- Build: Eval report for your AI app

### Week 16: Multimodal AI

- Speech-to-text (OpenAI Whisper)
- Claude Vision (analyze images with AI)
- Image generation (Replicate, Stability AI)
- Combining voice + vision in one pipeline
- Build: Voice meeting summarizer
- Flow: speak -> transcribe -> summarize -> email

### Week 17: AI Product Patterns (Study Real Products)

- Copilot pattern -> AI helps user do task faster
- Example: GitHub Copilot, Cursor
- Chatbot pattern -> conversational AI interface
- Example: Claude, ChatGPT
- Autonomous agent pattern -> AI does task alone
- Example: Devin, AutoGPT
- Data pipeline pattern -> AI processes bulk data
- Example: AI that reads 1000 emails/day
- Do: Study 10 real AI products deeply
- Output: 3 AI product ideas (your ideas)

### Week 18: AI Phase Project (Milestone)

- Pick one real problem to solve with AI
- Build a complete AI-powered product
- Option A: AI document analyzer
- Option B: AI email/outreach writer
- Option C: AI SEO content tool
- Deploy publicly with live URL
- Get at least 5 real people to use it
- Portfolio Project #2 complete

### Phase 2 Outcome

- You can build AI products from scratch
- You understand RAG, agents, fine-tuning
- You have a live AI app with real users
- You are now more skilled than 95% of devs

## Phase 3: Full-Stack

**Weeks:** 19-28  
**Goal:** Wrap AI in products people can actually buy and use.

### Week 19: React Fundamentals

- Components (reusable UI blocks)
- Hooks (`useState`, `useEffect`, `useContext`)
- Props and state management
- Tailwind CSS (utility-first styling)
- Build: React dashboard UI

### Week 20: Next.js (App Router)

- Next.js 14+ with App Router
- Server components vs client components
- API routes (backend inside Next.js)
- SSR vs SSG vs ISR
- Deploy on Vercel (1 click)
- Build: Full Next.js app deployed live

### Week 21: Auth and User Management

- Clerk (easiest auth for Next.js)
- Google / GitHub OAuth
- JWT tokens and sessions
- Protected routes (only logged-in users)
- Row-level security in Supabase
- Build: App with auth + user dashboard

### Week 22: Payments with Stripe

- Stripe subscriptions (recurring billing)
- Pricing tiers (Free / Pro / Business)
- Webhooks (Stripe tells your app what happened)
- Billing portal (users manage their plan)
- Free trials and usage-based billing
- Build: 3-tier subscription SaaS payment flow
- Note: This skill alone = $5K per project

### Week 23: UI/UX for Developers

- `shadcn/ui` (copy-paste component library)
- Tailwind CSS (spacing, colors, responsive)
- Framer Motion (smooth animations)
- Landing page design (hero, features, pricing)
- Do: Study 5 great SaaS landing pages
- Build: Redesign old project with polished UI

### Week 24: Email + Background Jobs

- Resend (send transactional emails)
- Upstash (Redis queues)
- Inngest (background job processing)
- Why needed: AI tasks take 30-60 seconds
- Background jobs prevent timeout
- Build: Email system + async AI job queue

### Week 25: Analytics and Monitoring

- PostHog (user behavior tracking)
- Sentry (error tracking in production)
- Axiom (log management)
- Feature flags (release features safely)
- Build: Fully monitored production app

### Week 26: AI Streaming + Usage Tracking

- Stream AI responses (token by token)
- Rate limiting per user
- Track token usage per user
- Cost per user calculation
- Usage-based billing with Stripe
- Build: AI app with cost tracking per user

### Week 27: SaaS Architecture Patterns

- Multi-tenant architecture
- API design best practices
- Caching strategies (Redis)
- Scalability planning
- Document: Architecture for your SaaS idea

### Week 28: Full-Stack AI Project (Milestone)

- Build complete SaaS product
- Auth (Clerk)
- Database (Supabase)
- AI features (Claude/OpenAI)
- Payments (Stripe)
- Email (Resend)
- Analytics (PostHog)
- Deploy live on Vercel
- Portfolio Project #3 complete

### Phase 3 Outcome

- You can build complete SaaS products
- You know auth, payments, AI, email
- You have 3 live portfolio projects
- You are ready to get paid

## Phase 4: Build

**Weeks:** 29-38  
**Goal:** Build 3 real AI products with real users.

### Product A: AI Document Intelligence

**Window:** Weeks 29-32

- Problem: Businesses drown in PDFs, reports, contracts
- Solution: Upload doc -> AI reads -> answers questions
- User flow: Upload PDF -> Chunk -> Embed -> Store -> Ask -> Answer
- Tech stack:
  - Next.js (frontend)
  - Anthropic Claude (AI brain)
  - LangChain + RAG (document processing)
  - Supabase pgvector (storage)
  - Stripe (charge $29/month)
- Target: 10 paying beta users before Week 33
- Revenue: $290/month MRR

### Product B: AI Sales Outreach Writer

**Window:** Weeks 33-35

- Problem: Sales teams write 100 emails/day manually
- Solution: AI researches lead + writes personalized email
- User flow: Input ICP -> AI researches -> Writes email -> Sends via Gmail
- Tech stack:
  - Next.js (frontend)
  - Claude (email writing)
  - LangGraph (research + write agent)
  - Gmail API (send emails)
  - Stripe (charge $49/month)
- Target: 5 businesses using it
- Revenue: $245/month MRR

### Product C: Your Own Idea

**Window:** Weeks 36-38

- This one is yours. Pick a niche you understand.
- How to find your idea:
  - What problem do you face daily?
  - What does your family/friends complain about?
  - What does your local business struggle with?
  - Pick the most painful + most common problem
- Ideas by niche:
  - Healthcare -> AI medical report summarizer
  - Legal -> AI contract reviewer
  - Education -> AI tutor for specific subject
  - HR -> AI resume screener
  - Finance -> AI expense categorizer
- Target: $500 MRR before Phase 5 starts

### Phase 4 Outcome

- 3 live AI products in production
- Real users, real feedback, real money starting
- Your confidence is now unshakeable
- First $500-1000 MRR

## Phase 5: Earn

**Weeks:** 39-48  
**Goal:** Hit $10K+/month using 3 parallel streams.

### Stream 1: Freelancing

**Target:** $3K-6K/month

#### Week 39: Set Up Profiles

- Upwork (AI developer niche)
- Toptal (premium, harder to get in)
- LinkedIn (optimize for AI Engineer)

#### Week 40: Send First Proposals

- 10 proposals per day
- Niche down: "I build RAG chatbots"
- Show portfolio projects as proof

#### Week 41: Land First Client

- Start low ($30-50/hr) to get reviews
- Deliver exceptional work, get 5-star review

#### Weeks 42-48: Scale

- Raise rate -> $75/hr -> $100/hr -> $150/hr
- Work only with clients you choose
- $3K-6K/month realistic by month 10

### Stream 2: Agency Clients

**Target:** $5K-10K/month

#### Week 42: Start Cold Outreach

- Target: Small businesses (20-200 people)
- Message: "I build AI tools that save your team 10 hours/week"
- Send 20 outreach messages per week

#### Week 43: The AI Audit Offer

- Price: $500 flat (easy to say yes to)
- Deliverable: 5-page PDF showing where AI can help their business
- Convert: 60% buy a build project after

#### Week 44: Land First Project

- Price: $5,000 - $15,000 per project
- Timeline: 3-6 weeks to deliver
- Collect 50% upfront, 50% on delivery

#### Week 46: Hire Help

- Hire 1 junior dev (Upwork, $15-25/hr)
- You architect, they build
- Your margin: 60-70% profit per project

#### Stream Target

- 1-2 projects/month = $5K-15K/month

### Stream 3: Own SaaS (Passive)

**Target:** $1K-5K/month

#### Week 39: Pick Best Product From Phase 4

- The one with most user interest

#### Week 40: Content Marketing

- LinkedIn: post 3x/week
- X (Twitter): post daily
- Topic: "what I built this week"

#### Week 42: Product Hunt Launch

- Prep: 2 weeks of teaser posts
- Launch: get 200+ upvotes
- Result: 500-2000 new visitors

#### Week 44: SEO + Inbound Funnel

- Write 4 SEO blog posts/month
- Target: "AI tool for [niche]" keywords
- Free trial -> convert to paid

#### Week 48: Target $1K-5K MRR

- Grows passively while you sleep

### Phase 5 Income Math

| Source | Monthly Range |
| --- | --- |
| Freelance | $3,000 - $6,000/month |
| Agency projects | $5,000 - $10,000/month |
| SaaS MRR | $1,000 - $5,000/month |
| Total | $9,000 - $21,000/month |

## Earnings Timeline

| Time | Income Target | Note |
| --- | --- | --- |
| Month 01-02 | $0 | Learning phase. Zero income. Normal. |
| Month 03-04 | $0-500 | First small gigs or beta users |
| Month 05-06 | $1K-3K | First real clients + MRR starting |
| Month 07-08 | $3K-6K | Freelance flowing + agency starts |
| Month 09-10 | $6K-10K | Agency + SaaS compound together |
| Month 11 | $8K-15K | Everything firing simultaneously |
| Month 12 | $10K-20K+ | Target hit. Scale from here. |

## Tech Stack Mindmap

### Full Stack

#### AI Layer

- Models: Claude (Anthropic), GPT-4, Gemini
- Framework: LangChain, LangGraph, CrewAI
- Vector DB: Pinecone, Supabase pgvector
- Speech/Vision: Whisper, Claude Vision, Replicate

#### Backend

- Python: FastAPI, asyncio, pandas
- Node.js: Express, REST APIs

#### Frontend

- Framework: Next.js 14 (App Router)
- Library: React, `shadcn/ui`
- Styling: Tailwind CSS

#### Database

- Primary: PostgreSQL (via Supabase)
- Cache: Redis (via Upstash)
- Files: AWS S3, Supabase Storage

#### Services

- Auth: Clerk
- Payments: Stripe
- Email: Resend
- Jobs: Inngest
- Analytics: PostHog, Sentry

#### Deploy

- Frontend: Vercel
- Backend: Railway
- Containers: Docker

## Resources Mindmap

### Free Learning

- Python -> `python.org` + `exercism.io`
- AI/Claude -> `docs.anthropic.com` <- read everything
- Prompt Engineering -> `docs.anthropic.com/prompt-engineering`
- React/Next.js -> `react.dev` + `nextjs.org/learn`
- SQL -> `sqlzoo.net` + `supabase.com/docs`
- Git -> `learngitbranching.js.org`
- LangChain -> `python.langchain.com/docs`
- Agents -> `docs.anthropic.com/tool-use`
- Stripe -> `stripe.com/docs`

### Earning Platforms

- Freelance -> Upwork, Toptal, Contra
- Cold outreach -> Apollo.io, LinkedIn Sales Nav
- SaaS launch -> Product Hunt, Hacker News
- Content -> LinkedIn, X (Twitter)
- Inspiration -> `ycombinator.com` (AI startups)

## Daily Schedule

| Time | Activity |
| --- | --- |
| 6:00 - 8:00 | Study (new concepts, docs, videos) |
| 8:00 - 12:00 | Code (build the thing) |
| 12:00 - 13:00 | Break |
| 13:00 - 16:00 | Project work (portfolio / client) |
| 16:00 - 17:00 | Post on LinkedIn or X about what you built |
| 17:00 - 19:00 | Freelance / client work (Phase 5 only) |
| 19:00 - 20:00 | Read / research / plan tomorrow |

## The 3 Rules That Determine Everything

### Rule 1: Build Every Single Day

- No code pushed = day wasted. No exceptions.

### Rule 2: Every Project Must Be Live

- Private repo = invisible portfolio = no clients.

### Rule 3: Talk About What You Build

- LinkedIn 3x/week. Your audience = your clients.

## The Only 3 Things That Matter This Week

- Today -> Read `python.org/docs` for 2 hours
- Tomorrow -> Write your first Python script
- This week -> Build a CLI app and push to GitHub

Everything else follows from this.

## Supplemental Notes

- This roadmap assumes aggressive execution. If your schedule is limited, reduce speed, not standards.
- For every milestone project, aim to keep 1 public repo, 1 live demo URL, and 1 short case study or README.
- The exact tools in AI change quickly, but the core capabilities in this roadmap are the real asset: APIs, prompting, RAG, agents, productization, distribution, and sales.
