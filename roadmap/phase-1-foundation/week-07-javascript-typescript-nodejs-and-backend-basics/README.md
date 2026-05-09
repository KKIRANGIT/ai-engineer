# Week 07: JavaScript, TypeScript, Node.js, and Backend Basics

Back to [Phase 1](../README.md)

## Goal

Build enough real fluency in JavaScript, TypeScript, and Node.js that the web-facing half of the roadmap stops feeling separate from the Python half.

This week is not about mastering the entire frontend ecosystem. It is about crossing the language boundary cleanly, understanding the runtime model, and learning how to build a small backend service with readable structure and basic type discipline.

## Why This Week Matters

AI engineers rarely stay inside one language forever.

Even when most model-facing work is done in Python, product work often requires:

- JavaScript or TypeScript for web interfaces
- Node.js for tooling, scripting, server-side handlers, and API layers
- JSON-based contracts between services
- typed request and response thinking

If you skip this fluency layer, later phases become slower:

- Next.js and React will feel harder than necessary
- API route logic will look unfamiliar
- frontend-backend data contracts will remain fuzzy
- TypeScript errors will feel like random obstacles instead of useful feedback

Week 07 exists to remove that friction early.

## What This Week Is Really Training

At a deeper level, this week trains five important instincts:

### 1. Cross-language translation

You should learn to map ideas, not just syntax.

Examples:

- Python dictionaries vs JavaScript objects
- Python lists vs JavaScript arrays
- Python exceptions vs JavaScript `throw` and `try` / `catch`
- Python module structure vs ES module imports and exports

### 2. Event-loop awareness

Node.js backend work requires a practical mental model of asynchronous execution. You do not need runtime internals at compiler depth, but you do need to understand why I/O-heavy code is structured around callbacks, promises, and `async` / `await`.

### 3. Contract thinking

TypeScript matters because it forces you to describe shapes and expectations more explicitly. That becomes important later in APIs, frontend props, tool schemas, and agent orchestration.

### 4. Boundary validation

All backend code lives at boundaries:

- HTTP request boundaries
- JSON parsing boundaries
- environment variable boundaries
- file-system boundaries

This week teaches you that external input is never trusted by default.

### 5. Minimal backend architecture

A small Node service should still separate concerns:

- server bootstrapping
- request parsing
- validation
- business logic
- persistence
- response shaping

That structure matters far more than framework hype at this stage.

## Scope Boundary

This week is not for:

- advanced frontend state management
- React component architecture
- advanced TypeScript generics
- ORMs
- authentication systems
- deployment platforms
- production-scale observability

Those come later.

This week is for:

- modern JavaScript fluency
- practical TypeScript basics
- Node runtime familiarity
- backend request/response thinking
- small API design with clean fundamentals

## Week 07 Outcomes

By the end of this week, you should be able to:

- read and write modern JavaScript without constant translation back into Python
- explain the difference between browser JavaScript and Node.js
- use `const`, `let`, objects, arrays, template literals, destructuring, and modules comfortably
- write and reason about `async` / `await`
- explain how TypeScript improves contracts and refactoring safety
- write small TypeScript functions with object types, unions, and return types
- build and run a small Node API locally
- validate JSON input and return consistent error responses
- explain how a simple Node backend is structured

## Workspace Structure

This week now includes a hands-on workspace:

```text
week-07-javascript-typescript-nodejs-and-backend-basics/
|-- README.md
|-- package.json
|-- exercises/
|   |-- README.md
|   |-- javascript-basics/
|   |-- async-and-node/
|   |-- typescript-basics/
|   |-- backend-thinking/
|   `-- validation-and-errors/
|-- projects/
|   `-- reading-list-api/
|       |-- README.md
|       |-- package.json
|       |-- src/
|       |-- tests/
|       |-- data/
|       `-- typescript-reference/
`-- notes/
    |-- 01-week-plan.md
    |-- 02-python-vs-javascript.md
    `-- 03-node-backend-checklist.md
```

The week-level `package.json` marks the exercise files as ES modules so the Node examples can use modern `import` syntax directly.

## What To Learn

## 1. JavaScript Mental Model

Do not think of JavaScript as "Python with semicolons."

The important beginner truths are:

- `const` means the binding does not change, not that the object becomes immutable
- objects are flexible key-value containers, but they are not the same as Python classes
- arrays are powerful and come with built-in iteration helpers like `map`, `filter`, and `find`
- functions are first-class values and are passed around constantly
- block scope matters because `let` and `const` are scoped differently than older `var`

Key mindset:

- Python often reads like direct procedural logic
- JavaScript often mixes data transformation, callbacks, and object-based patterns

Learn the ideas, not just the punctuation.

## 2. Modern Syntax You Need

Be comfortable with:

- `const` and `let`
- object and array literals
- property shorthand
- destructuring
- template literals
- rest and spread syntax
- default function parameters
- optional chaining
- nullish coalescing at a basic level

These features appear everywhere in modern Node and frontend codebases. You do not need to memorize every corner case, but you must stop treating them as "advanced syntax."

## 3. Async Patterns in JavaScript

Understand three layers:

### Promise-producing work

Some APIs return promises because the result is not available immediately.

### `async` / `await`

This is the readable form of promise-based logic. It lets you write asynchronous code that still reads top to bottom.

### Error handling

Network calls, file reads, and JSON parsing can fail. You need clear `try` / `catch` habits and reasonable fallback behavior.

Important mental comparison with Python:

- the purpose of async is similar
- the runtime and ecosystem conventions are different
- JavaScript exposes async patterns much earlier in day-to-day code

## 4. Node.js Runtime Basics

You should understand Node.js at a practical level:

- it runs JavaScript outside the browser
- it provides access to files, environment variables, network sockets, and processes
- it is commonly used for APIs, scripts, CLIs, and build tooling
- modern Node projects usually use modules and `package.json`

You should also understand the difference between:

- language: JavaScript
- type system add-on: TypeScript
- runtime: Node.js
- framework: Express, Fastify, Next.js API routes, or similar

Beginners often confuse these layers. Do not.

## 5. TypeScript Basics

For this week, TypeScript should teach clarity, not fear.

Learn:

- primitive annotations
- arrays and object types
- type aliases
- interfaces
- union types
- optional properties
- function parameter and return annotations
- basic narrowing with `typeof` and property checks

What matters:

- you describe the shape of values
- you make invalid states harder to express
- you reduce ambiguity for future readers and tooling

## 6. REST API Design in Node

You should understand:

- how a request reaches a route
- how the server chooses a handler
- how query strings and path parameters differ
- how JSON request bodies are parsed
- how responses should be shaped consistently
- how to use status codes intentionally

Good beginner habits:

- keep routes small
- do validation before business logic
- separate persistence from handlers
- return stable JSON shapes
- keep error responses predictable

## 7. Validation and Error Thinking

The moment data crosses a boundary, you validate it.

Examples:

- request body fields may be missing
- a field may have the wrong type
- a URL parameter may not be in the format you expect
- a file may not exist
- environment configuration may be absent

Validation is not bureaucracy. It is how you keep small systems understandable.

## 8. Project Layout in Node

A beginner project still benefits from structure.

This week's project separates:

- `server.js` for bootstrapping
- `app.js` for the request handler
- `request-utils.js` and `response-utils.js` for boundary logic
- `validation.js` for input rules
- `book-service.js` for business logic
- `storage.js` for file persistence

That is enough structure to teach the right habits without becoming overengineered.

## Best Learning Sequence For This Week

Use this order:

1. modern JavaScript syntax and value types
2. arrays, objects, and functions
3. modules and runtime scripts in Node
4. promises and `async` / `await`
5. TypeScript basics
6. JSON request/response thinking
7. routing and validation
8. structured backend assembly

## Recommended Daily Breakdown

### Day 1: Modern JavaScript basics

Focus:

- `const` and `let`
- objects and arrays
- functions
- template literals
- destructuring

Do:

- complete the JavaScript basics exercises
- rewrite one small Python-style data manipulation problem in JavaScript

### Day 2: Modules and async workflow

Focus:

- imports and exports
- file reading in Node
- promises
- `async` / `await`

Do:

- complete the async exercises
- step through one script and explain the flow out loud

### Day 3: TypeScript foundations

Focus:

- type annotations
- interfaces
- type aliases
- union types

Do:

- complete the TypeScript exercises
- compare the untyped JavaScript version with the typed TypeScript version

### Day 4: Backend request and response flow

Focus:

- routing
- status codes
- JSON request bodies
- response shapes

Do:

- complete the backend-thinking exercise
- map one route from incoming request to final JSON response

### Day 5: Validation and service structure

Focus:

- input validation
- separating route code from business logic
- error handling

Do:

- complete the validation exercise
- inspect the project validation and service layers carefully

### Day 6: Build and inspect the full API

Focus:

- project structure
- file persistence
- API route behavior
- typed reference code

Do:

- run the reading-list API
- test the routes manually
- read the TypeScript reference folder and explain how types improve the design

### Day 7: Synthesis and comparison

Focus:

- Python vs JavaScript mental model
- Node vs Python backend differences
- when TypeScript is most helpful

Do:

- read the notes folder
- write your own summary of what still feels unfamiliar

## Build Plan

This week should produce three layers of proof:

### 1. Syntax and concept exercises

Purpose:

- remove surface-level confusion
- practice reading and writing modern JavaScript and beginner TypeScript

### 2. A runnable Node backend

Purpose:

- understand server bootstrapping, route flow, JSON boundaries, validation, and file-backed persistence

### 3. A typed reference layer

Purpose:

- see how TypeScript sharpens object shapes, service contracts, and route payload thinking

## Main Project

The primary project for this week is:

- [projects/reading-list-api](projects/reading-list-api/README.md)

It is intentionally simple:

- no external framework dependency is required to understand the backend flow
- the server uses the built-in Node HTTP runtime
- JSON is persisted to a file for clarity
- a TypeScript companion folder shows how the same ideas become more explicit with types

Routes included:

- `GET /health`
- `GET /books`
- `GET /books/:id`
- `POST /books`
- `PATCH /books/:id/read`

## Deliverables

By the end of this week, you should have:

- completed JavaScript, async, TypeScript, backend, and validation exercises
- one working Node API project
- one project README documenting routes and local usage
- one typed reference layer showing basic TypeScript contracts
- notes explaining Python vs JavaScript and Node backend thinking

## Exit Criteria

You are ready to move on only if:

- you can read common modern JavaScript syntax without getting lost
- you understand when to use `const`, arrays, objects, destructuring, and template literals
- you can explain what a promise is and how `async` / `await` changes readability
- you can write small typed TypeScript functions and object shapes
- you can explain how a Node HTTP request becomes a JSON response
- you can validate incoming request data before using it
- you can run and understand the reading-list API end to end

## Common Mistakes To Avoid

- translating every line mentally back into Python instead of learning JavaScript on its own terms
- using `let` everywhere instead of preferring `const`
- writing asynchronous code without understanding where failures can happen
- treating TypeScript as optional decoration instead of contract clarification
- packing routing, validation, persistence, and business logic into one file
- returning inconsistent error response shapes

## Expert Notes That Matter Early

### JavaScript fluency is strategic, not cosmetic

Later full-stack and product work becomes dramatically easier once JS and TS stop feeling alien.

### TypeScript is a design aid

A good type definition is not just for the compiler. It is a statement of intent.

### Node backend fundamentals matter more than framework branding

If you understand how a request is parsed, validated, routed, and answered, moving from one Node framework to another becomes far easier.

### Small systems teach architecture best

A tiny backend with clear files teaches more than a large copied template you do not understand.

## Suggested References

Prioritize these sources in this order:

1. MDN JavaScript Guide  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
2. MDN `async function` reference  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
3. TypeScript Handbook  
   https://www.typescriptlang.org/docs/handbook/intro.html
4. Node.js Learn documentation  
   https://nodejs.org/en/learn
5. Node.js HTTP module docs  
   https://nodejs.org/api/http.html
6. Node.js file-system docs  
   https://nodejs.org/api/fs.html
7. Optional Express reference for comparison later  
   https://expressjs.com/

Use the official docs first. Use this workspace as the proving ground where the ideas become real.

## Final Standard For This Week

The correct outcome of Week 07 is not:

"I touched JavaScript, TypeScript, and Node once."

The correct outcome is:

"I can move between Python and Node mental models, understand modern JavaScript syntax, write small typed TypeScript code, and build a simple backend that handles requests, validation, and JSON responses cleanly."
