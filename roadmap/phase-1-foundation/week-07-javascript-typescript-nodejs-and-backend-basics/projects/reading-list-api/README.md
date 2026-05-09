# Reading List API

Back to [Week 07](../../README.md)

## Purpose

This project is a small Node.js backend that manages a reading list.

It is designed to teach:

- how a Node HTTP server is structured
- how routes are matched
- how JSON request bodies are parsed
- how validation protects the rest of the application
- how business logic can stay separate from persistence
- how TypeScript would describe the same shapes more explicitly

The project uses the built-in Node runtime instead of a framework so that the request/response flow stays visible.

## Project Structure

```text
reading-list-api/
|-- README.md
|-- package.json
|-- data/
|   `-- seed-reading-list.json
|-- src/
|   |-- app.js
|   |-- book-service.js
|   |-- request-utils.js
|   |-- response-utils.js
|   |-- router.js
|   |-- server.js
|   |-- storage.js
|   `-- validation.js
|-- tests/
|   |-- app.test.js
|   `-- validation.test.js
`-- typescript-reference/
    |-- README.md
    |-- tsconfig.json
    `-- src/
```

## Routes

### `GET /health`

Simple health endpoint.

### `GET /books`

Returns all books.

### `GET /books/:id`

Returns one book by ID.

### `POST /books`

Creates a new book.

Expected JSON body:

```json
{
  "title": "Practical Object-Oriented Design",
  "author": "Sandi Metz",
  "tags": ["design", "ruby"]
}
```

### `PATCH /books/:id/read`

Marks one book as read.

## How To Run

From this folder:

```powershell
node src/server.js
```

The API starts on `http://localhost:4000` by default.

You can change the port:

```powershell
$env:PORT=4500
node src/server.js
```

## How To Test

```powershell
node --test
```

## Architecture Notes

### `server.js`

Starts the Node HTTP server and wires the project together.

### `app.js`

Contains the main request handler so it can be tested without coupling everything to the startup file.

### `router.js`

Matches methods and paths to a route description.

### `request-utils.js`

Parses request bodies and extracts useful path information.

### `response-utils.js`

Keeps response formatting consistent.

### `validation.js`

Rejects invalid request data before business logic uses it.

### `book-service.js`

Contains the reading-list rules, such as creating a book or marking it as read.

### `storage.js`

Handles file-backed JSON persistence.

## Why There Is A TypeScript Reference Folder

The main project runs as plain JavaScript to keep local execution simple.

The `typescript-reference/` folder shows how the same ideas become clearer when you add:

- explicit object shapes
- typed service contracts
- typed route payloads

Use that folder as a bridge into the later TypeScript-heavy parts of the roadmap.
