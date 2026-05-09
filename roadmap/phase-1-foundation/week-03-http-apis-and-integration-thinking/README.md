# Week 03: HTTP, APIs, and Integration Thinking

Back to [Phase 1](../README.md)

## Goal

Understand how software communicates over the network and learn to work with external APIs as an engineer rather than as a copy-paste consumer.

Week 03 is where Python stops being only local scripting and starts becoming integration tooling.

By the end of this week, you should be able to:

- explain the request-response model clearly
- distinguish methods such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`
- inspect status codes, headers, and response bodies during debugging
- parse JSON responses into Python data structures
- send HTTP requests safely with explicit timeout thinking
- understand auth headers and API key handling
- design a small reusable wrapper around one real API

This week is the bridge between local programming and service integration.

## What This Week Is Actually Training

At surface level, Week 03 looks like "learn HTTP and call a few APIs."

The real training target is deeper:

- learning to reason about systems outside your own code
- understanding the data contract between client and server
- treating failures as a normal part of integration work
- separating transport details from business logic
- designing wrappers so your application code stays clean

This is why Week 03 matters so much for the rest of the roadmap. Later AI engineering work is full of API integrations:

- OpenAI
- Anthropic
- Stripe
- Supabase
- email providers
- analytics providers
- internal service calls

If HTTP feels fuzzy, every one of those systems feels harder than it should.

## Scope Boundaries

Study deeply this week:

- request and response structure
- status codes
- headers and auth
- JSON payloads and response shapes
- query parameters
- pagination concepts
- timeouts
- retries and backoff thinking
- small wrapper design
- debugging integration failures

Do not go deep on these yet:

- OAuth implementation details
- advanced HTTP caching
- websocket protocols
- async HTTP clients
- production observability stacks
- API schema generation
- distributed tracing

The goal is strong integration fundamentals, not protocol specialization.

## Week 03 Outcomes

You are successful this week if you can do most of the following with confidence:

- describe what a request contains
- describe what a response contains
- use status codes to narrow down failures quickly
- send query parameters and headers intentionally
- parse only the fields you actually need from a JSON response
- explain why timeouts and retries matter
- build one small client wrapper instead of scattering raw HTTP calls everywhere

## How Week 03 Builds On Week 02

Week 02 taught you how to organize a small Python project into:

- modules
- validation boundaries
- storage layers
- tests

Week 03 applies those same habits to integrations.

Instead of asking:

- how do I structure local Python logic

you now also ask:

- how do I structure communication with an external system

That means Week 03 is not a separate topic. It is Week 02 engineering discipline applied to networked software.

## Core Integration Concepts To Master

## 1. HTTP Mental Model

The first thing to learn is not a library. It is the protocol shape.

You must understand:

- a client sends a request
- a server returns a response
- the request has method, URL, headers, and sometimes a body
- the response has status code, headers, and body

Important idea:

HTTP is a contract. Your code is simply one client participating in that contract.

## 2. Methods and Intent

You should know the meaning of:

- `GET`: read or fetch data
- `POST`: create or submit data
- `PUT`: replace a resource
- `PATCH`: partially update a resource
- `DELETE`: remove a resource

Expert beginner rule:

Do not learn methods as trivia. Always connect them to an application behavior.

## 3. Status Codes

You must understand the broad families:

- `2xx`: success
- `3xx`: redirection
- `4xx`: client-side issue
- `5xx`: server-side issue

Important codes:

- `200 OK`
- `201 Created`
- `204 No Content`
- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `429 Too Many Requests`
- `500 Internal Server Error`

Important debugging rule:

Do not treat a failing API call as "the internet is broken." Start with the status code and let it narrow the problem.

## 4. Headers and Authentication

You need to understand:

- what headers are
- how `Authorization` is used
- why `Accept` matters
- why `Content-Type` matters
- why API secrets should live outside source code

Early habit:

- never hardcode secrets into committed files
- use environment variables or a documented config pattern

## 5. JSON and Response Shape

Most beginner API mistakes are not about sending the request. They are about misunderstanding the response.

You should be able to:

- inspect a JSON response
- identify the top-level type
- find the exact fields you need
- validate whether the shape matches your expectation

Expert beginner rule:

Good API work means extracting the 3-5 fields you need, not dumping a 500-line JSON blob and calling it done.

## 6. Query Parameters and Pagination

You need to understand:

- query parameters for filtering and search
- page-based pagination
- cursor-based pagination at a concept level
- that many APIs return partial result sets

This matters because real integrations almost never end at the first page.

## 7. Timeouts, Retries, and Rate Limits

This is where toy scripts become engineering code.

You should know:

- timeouts should be explicit
- not every failure should be retried
- `429` means the API is asking you to slow down
- backoff is a strategy for spacing retries

The project this week uses simple retry-aware thinking, not a heavy retry framework. That is the right level here.

## 8. Wrapper Design

The engineering upgrade of the week is learning not to scatter raw HTTP calls.

A small wrapper should:

- accept clean Python parameters
- build the URL and headers
- send the request
- validate or interpret the response
- return useful Python data

This pattern transfers directly into every later AI provider client you will build.

## Best Learning Sequence For This Week

Use this order:

1. request-response model
2. methods and status codes
3. headers and auth
4. JSON response shape
5. query parameters
6. timeouts and retries
7. reusable wrappers
8. project-level API client design

## A No-Doubt Execution Plan For The Week

### Day 1: HTTP fundamentals

Study:

- requests and responses
- methods
- status code families

Practice:

- run the HTTP basics exercise
- inspect the exploration scripts before running them

Checkpoint:

- can you explain what the client sends and what the server sends back

### Day 2: JSON and headers

Study:

- response bodies
- headers
- JSON shape extraction

Practice:

- run the JSON response exercise
- edit the scripts so they print only selected fields

Checkpoint:

- can you explain the exact fields you need from a response instead of printing everything

### Day 3: Query parameters and URL building

Study:

- URL encoding
- query parameters
- filtered requests

Practice:

- run the query-parameter exercise
- inspect how the GitHub client builds URLs

Checkpoint:

- can you build a URL with query parameters without guessing

### Day 4: Timeouts, retries, and failure thinking

Study:

- timeout
- retry
- backoff
- rate limits

Practice:

- run the resilience exercise
- read the debugging checklist note

Checkpoint:

- can you explain when retrying is reasonable and when it is not

### Day 5: API wrapper design

Study:

- helper functions
- low-level transport code
- response parsing
- data models

Practice:

- run the wrapper-design exercise
- inspect the GitHub client package

Checkpoint:

- can you explain why wrapper code is better than scattered request calls

### Day 6: Real project work

Build:

- run the exploration scripts
- run the GitHub API client example
- inspect the CLI and data models

Checkpoint:

- can you explain how the project separates config, HTTP utilities, parsing, and application usage

### Day 7: Review and synthesis

Review:

- reread the week README
- walk through the debugging checklist
- review the project tests

Checkpoint:

- can you debug a broken call methodically
- can you explain why this week makes later AI API work easier

## Week 03 Workspace Standard

This week now includes a real hands-on workspace.

Actual structure:

```text
week-03-http-apis-and-integration-thinking/
|-- exercises/
|   |-- http-basics/
|   |-- json-and-responses/
|   |-- query-params/
|   |-- resilience/
|   |-- wrappers/
|   `-- README.md
|-- projects/
|   |-- api-exploration-scripts/
|   `-- github-api-client/
|       |-- github_api/
|       |-- tests/
|       |-- examples/
|       |-- data/
|       |-- .env.example
|       `-- README.md
|-- notes/
`-- README.md
```

## Main Build Goals

This week has two build layers.

### Layer 1: Exploration scripts

You should explore several public APIs through small scripts so you see different response shapes and usage patterns.

This workspace includes:

- GitHub API exploration
- JSONPlaceholder exploration
- httpbin request/echo exploration

### Layer 2: One reusable API wrapper

The main project is a small GitHub API client.

It includes:

- config handling
- URL building
- explicit timeout use
- header handling
- JSON parsing
- dataclass-based response modeling
- CLI usage
- unit tests for parsing and helper logic

## Deliverables

By the end of the week, you should have:

- completed the local exercises
- explored at least three API patterns
- understood one reusable GitHub client package
- run the example script or CLI successfully in a network-enabled environment
- reviewed the local tests
- written a short note about at least one failure pattern you now understand better

## Best Sources For Week 03

Use sources in this order.

### Tier 1: Protocol and Standard Reference

1. MDN HTTP overview
   Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview

2. MDN HTTP methods
   Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

3. MDN HTTP status codes
   Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

### Tier 2: Python Client Reference

1. Python `urllib` documentation
   Link: https://docs.python.org/3/library/urllib.request.html

2. Python `urllib.parse` documentation
   Link: https://docs.python.org/3/library/urllib.parse.html

3. `requests` quickstart
   Link: https://requests.readthedocs.io/en/latest/user/quickstart/

4. `httpx` quickstart
   Link: https://www.python-httpx.org/quickstart/

Important note:

This workspace project uses Python's standard library so it stays runnable without extra dependencies, but you should still recognize the `requests` and `httpx` ecosystems because they are common in real-world code.

### Tier 3: Provider-Specific Reference

1. GitHub REST API getting started
   Link: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api

2. GitHub rate limits
   Link: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api

3. JSONPlaceholder guide
   Link: https://jsonplaceholder.typicode.com/guide/

4. httpbin
   Link: https://httpbin.org/

## Source Strategy That Avoids Confusion

For Week 03, use this source stack:

1. MDN for protocol understanding
2. Python `urllib` docs for first-principles mechanics
3. `requests` or `httpx` docs for ecosystem awareness
4. provider docs for the exact API you are touching
5. this local workspace for actual learning-through-code

That stack is enough.

## Exact Study Path Through The Sources

If you want the least ambiguity, use this sequence:

1. read the MDN HTTP overview
2. run the HTTP basics exercise
3. read methods and status code references
4. run the JSON and query-parameter exercises
5. read the `urllib` docs selectively
6. inspect the GitHub API client utilities
7. run the exploration scripts
8. read the GitHub REST API getting-started docs
9. run the project example or CLI
10. review the tests and notes

## Exit Criteria

You are ready for Week 04 only if most of these are true:

- you can explain what an HTTP request and response contain
- you can interpret common status codes quickly
- you can send query parameters and headers intentionally
- you can parse useful fields from a JSON response
- you understand why timeouts and retries matter
- you can explain one reusable client wrapper from this workspace
- you can debug a broken integration in a methodical order

If these are not true, repeat the exploration and wrapper review before moving on.

## Common Mistakes That Create Confusion Later

- printing entire responses without understanding structure
- ignoring status codes and assuming success
- hardcoding secrets into source files
- writing raw request logic repeatedly
- forgetting explicit timeouts
- retrying blindly without thinking about cause
- assuming every response is JSON

## Expert Notes

### Integration code should be boring

Good API integration code is explicit, predictable, and easy to inspect.

### Response shape matters more than response size

What matters is not how much data came back. What matters is whether you know which fields your application actually needs.

### Failure handling is part of the design

A network call that only works in perfect conditions is incomplete.

## How Week 03 Connects To Week 04

Week 04 focuses on Git, GitHub, terminal workflow, and developer operations habits.

That week becomes easier if Week 03 is strong, because integration work quickly leads to:

- managing project files
- documenting setup
- thinking about environment variables
- working with external tools and remote systems

HTTP work is one of the first places where engineering workflow starts feeling real.

## Final Standard For This Week

The correct outcome is not:

"I can hit an endpoint."

The correct outcome is:

"I understand HTTP well enough to integrate external APIs cleanly, inspect response structure intelligently, debug failures methodically, and build small reusable client wrappers."
