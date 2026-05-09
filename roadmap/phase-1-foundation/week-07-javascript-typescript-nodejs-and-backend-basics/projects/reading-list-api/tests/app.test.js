import test from "node:test";
import assert from "node:assert/strict";
import http from "node:http";
import { createApp } from "../src/app.js";

function createMemoryBookService() {
  const books = [
    {
      id: "book-1",
      title: "Clean Code",
      author: "Robert C. Martin",
      tags: ["clean-code"],
      isRead: false,
    },
  ];

  return {
    async listBooks() {
      return books;
    },
    async getBookById(id) {
      return books.find((book) => book.id === id) ?? null;
    },
    async createBook(input) {
      const newBook = {
        id: `book-${books.length + 1}`,
        title: input.title,
        author: input.author,
        tags: input.tags ?? [],
        isRead: false,
      };

      books.push(newBook);
      return newBook;
    },
    async markBookAsRead(id) {
      const book = books.find((item) => item.id === id);

      if (!book) {
        return null;
      }

      book.isRead = true;
      return book;
    },
  };
}

function makeRequest(server, method, path, body) {
  return new Promise((resolve, reject) => {
    const address = server.address();

    const request = http.request(
      {
        hostname: "127.0.0.1",
        port: address.port,
        path,
        method,
        headers: body
          ? {
              "Content-Type": "application/json",
            }
          : {},
      },
      (response) => {
        let responseBody = "";

        response.on("data", (chunk) => {
          responseBody += chunk.toString();
        });

        response.on("end", () => {
          resolve({
            statusCode: response.statusCode,
            body: responseBody ? JSON.parse(responseBody) : null,
          });
        });
      },
    );

    request.on("error", reject);

    if (body) {
      request.write(JSON.stringify(body));
    }

    request.end();
  });
}

test("GET /health returns service status", async () => {
  const app = createApp({ bookService: createMemoryBookService() });
  const server = http.createServer(app);

  await new Promise((resolve) => server.listen(0, resolve));

  try {
    const response = await makeRequest(server, "GET", "/health");

    assert.equal(response.statusCode, 200);
    assert.equal(response.body.status, "ok");
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
});

test("POST /books validates payloads", async () => {
  const app = createApp({ bookService: createMemoryBookService() });
  const server = http.createServer(app);

  await new Promise((resolve) => server.listen(0, resolve));

  try {
    const response = await makeRequest(server, "POST", "/books", {
      title: "",
      author: "",
    });

    assert.equal(response.statusCode, 400);
    assert.equal(response.body.message, "Invalid book payload.");
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
});

test("POST /books creates a new book when the payload is valid", async () => {
  const app = createApp({ bookService: createMemoryBookService() });
  const server = http.createServer(app);

  await new Promise((resolve) => server.listen(0, resolve));

  try {
    const response = await makeRequest(server, "POST", "/books", {
      title: "Practical Node",
      author: "Asha Singh",
      tags: ["node", "backend"],
    });

    assert.equal(response.statusCode, 201);
    assert.equal(response.body.data.title, "Practical Node");
    assert.equal(response.body.data.isRead, false);
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
});
