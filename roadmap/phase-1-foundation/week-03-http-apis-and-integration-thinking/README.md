# Week 03: HTTP, APIs, and Integration Thinking

Back to [Phase 1](../README.md)

## Goal

Understand how software communicates over the network and learn to work with external APIs as an engineer rather than as a copy-paste consumer.

This week is about building a strong mental model of request-response systems, structured data exchange, and integration reliability.

## Why This Week Matters

Most modern engineering work involves integration:

- frontend to backend
- backend to third-party services
- one internal service to another
- product logic to AI providers

If you do not understand HTTP well, later topics become much harder:

- model APIs feel magical instead of predictable
- auth problems become confusing
- debugging becomes slow
- retry, timeout, and pagination issues become painful

Week 03 is the foundation for everything later involving OpenAI, Anthropic, Supabase, Stripe, or any other external system.

## Week 03 Outcomes

By the end of this week, you should be able to:

- explain the request-response model clearly
- use `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` correctly at a beginner-professional level
- inspect status codes, headers, and response bodies when debugging
- parse JSON responses into Python data structures
- call public APIs using `requests` or `httpx`
- handle auth headers and API keys safely
- design a small wrapper around an external API

## What To Learn

## 1. HTTP Mental Model

Start with the system model, not the library syntax.

You need to understand:

- a client sends a request
- a server returns a response
- the request has method, URL, headers, and sometimes a body
- the response has status code, headers, and body

Important idea:

HTTP is not "Python calling the internet." It is a protocol with rules and predictable structure.

## 2. Methods and Their Meaning

You should know the intent of:

- `GET`: read data
- `POST`: create or submit data
- `PUT`: replace data
- `PATCH`: partially update data
- `DELETE`: remove data

Expert beginner rule:

Do not memorize methods abstractly. Tie each method to an application behavior.

## 3. Status Codes

You should understand the broad categories:

- `2xx`: success
- `3xx`: redirection
- `4xx`: client-side problem
- `5xx`: server-side problem

Important codes to know:

- `200 OK`
- `201 Created`
- `204 No Content`
- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `429 Too Many Requests`
- `500 Internal Server Error`

Expert rule:

When an API call fails, always inspect:

- status code
- response body
- request headers you sent

## 4. Headers, Tokens, and Auth

You need to understand:

- what headers are
- why `Authorization` matters
- API keys vs bearer tokens
- content negotiation basics
- `Content-Type` and `Accept`

Important habit:

- never hardcode secrets into shared code
- use environment variables

## 5. JSON as the Language of APIs

You already touched JSON in Week 02. This week uses it in network communication.

You should be comfortable with:

- sending JSON payloads
- reading JSON responses
- knowing when the response is not JSON
- thinking about the expected response shape

Expert note:

Good API integration starts by understanding the response schema, not just printing the full result blob.

## 6. Query Parameters and Pagination

Many APIs use query parameters for:

- filtering
- sorting
- searching
- page navigation

You should understand:

- URL parameters
- page-based pagination
- cursor-based pagination at a concept level

Why this matters:

- real APIs often return partial results
- you need to know how to fetch more than the first page

## 7. Timeouts, Retries, and Rate Limits

This is one of the biggest differences between toy code and engineering thinking.

You need to know:

- network calls can fail temporarily
- not every failure should be retried
- timeouts should be explicit
- rate limits exist and must be respected

Focus on the concepts:

- timeout
- retry
- backoff
- `429` handling

Even if your first implementations are simple, your mindset should already include these concerns.

## 8. Using `requests` or `httpx`

You can start with either library.

Learn:

- basic request call
- query parameters
- headers
- JSON body
- response parsing
- response validation

Practical rule:

- write small wrapper functions
- do not scatter raw HTTP calls all over your code

## 9. API Wrapper Design

This is the engineering upgrade of the week.

Instead of writing one-off scripts only, learn to build a small API client abstraction.

A small wrapper should:

- accept parameters cleanly
- send the request
- validate success or failure
- return useful Python data
- hide low-level details from the rest of your code

This skill transfers directly into later AI provider work.

## 10. Debugging Integrations

When an API call is failing, debug in this order:

1. Check the URL.
2. Check the method.
3. Check headers.
4. Check payload shape.
5. Check response status code.
6. Check response body.
7. Check whether auth or rate limits are involved.

This debugging order will save you a lot of time later.

## Best Learning Sequence For This Week

Use this order:

1. request-response model
2. methods and status codes
3. headers and auth
4. JSON payloads and responses
5. query params and pagination
6. retries and timeouts
7. Python HTTP client usage
8. API wrapper design

## Recommended Daily Breakdown

### Day 1: HTTP fundamentals

Focus:

- request-response structure
- methods
- status code families

Build:

- inspect a few public APIs manually

### Day 2: JSON and headers

Focus:

- request headers
- response bodies
- JSON parsing

Build:

- script that fetches and prints selected fields only

### Day 3: Auth and environment variables

Focus:

- API key handling
- auth headers
- `.env` usage

Build:

- authenticated call to one safe external API if available

### Day 4: Pagination and filtering

Focus:

- query parameters
- paginated responses

Build:

- collect multiple pages of data from one API

### Day 5: Error handling and retries

Focus:

- failure modes
- timeout setting
- simple retry strategy

Build:

- resilient wrapper function

### Day 6: API wrapper module

Focus:

- clean function design
- reusable client shape

Build:

- small SDK-style wrapper for one chosen API

### Day 7: Example scripts and documentation

Focus:

- show real usage
- polish README
- document known limits and assumptions

## Build Plan

You should complete two layers of build work this week.

### Layer 1: Exploration scripts

Consume at least three public APIs.

Suggested examples:

- weather API
- GitHub API
- public placeholder or testing API

The point is not the brand. The point is seeing different response shapes and integration patterns.

### Layer 2: One small wrapper library

Choose one API and build a small client around it.

Good wrapper features:

- base request helper
- explicit timeout
- header handling
- query parameter support
- status validation
- JSON parsing
- example usage script

## Deliverables

By the end of this week, you should have:

- scripts for at least three API integrations
- one small API wrapper module or package
- example scripts showing common usage
- one README explaining auth, setup, and sample outputs
- one short note describing how you debugged at least one failed request

## Exit Criteria

You are ready to move on only if:

- you can explain what an HTTP request and response contain
- you can use status codes to guide debugging
- you can send headers and parse JSON confidently
- you can work with query parameters and basic pagination
- you can build one small reusable API wrapper instead of only one-off scripts
- you can debug a broken API call methodically

## Common Mistakes To Avoid

- printing entire responses without understanding the data shape
- ignoring status codes and assuming success
- hardcoding secrets into source files
- writing raw request logic repeatedly instead of wrapping it
- retrying everything blindly
- forgetting timeouts

## Expert Notes That Matter Early

### Integration code should be boring

Good integration code is predictable, explicit, and easy to debug.

### Response shape matters more than response size

The most important skill is knowing which fields you actually need.

### Failure handling is part of the design

A network call that only works in perfect conditions is incomplete.

## Suggested References

- HTTP overview resources
- `requests` or `httpx` documentation
- provider-specific API docs for the APIs you use
- JSON documentation and examples

## Final Standard For This Week

The correct outcome of Week 03 is not "I can hit an endpoint."

The correct outcome is:

"I understand HTTP well enough to integrate external APIs cleanly, debug failures methodically, and build small reusable client wrappers."
