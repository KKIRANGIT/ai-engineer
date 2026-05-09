import { readJsonBody } from "./request-utils.js";
import { sendError, sendJson } from "./response-utils.js";
import { matchRoute } from "./router.js";
import { validateNewBookInput } from "./validation.js";

export function createApp({ bookService }) {
  return async function app(request, response) {
    const url = new URL(request.url, "http://localhost");
    const route = matchRoute(request.method, url.pathname);

    if (!route) {
      sendError(response, 404, "Route not found.");
      return;
    }

    try {
      if (route.name === "health") {
        sendJson(response, 200, {
          status: "ok",
          service: "reading-list-api",
        });
        return;
      }

      if (route.name === "listBooks") {
        const books = await bookService.listBooks();
        sendJson(response, 200, { data: books });
        return;
      }

      if (route.name === "getBookById") {
        const book = await bookService.getBookById(route.params.id);

        if (!book) {
          sendError(response, 404, "Book not found.");
          return;
        }

        sendJson(response, 200, { data: book });
        return;
      }

      if (route.name === "createBook") {
        const input = await readJsonBody(request);
        const validation = validateNewBookInput(input);

        if (!validation.isValid) {
          sendError(response, 400, "Invalid book payload.", validation.errors);
          return;
        }

        const newBook = await bookService.createBook(input);
        sendJson(response, 201, { data: newBook });
        return;
      }

      if (route.name === "markBookAsRead") {
        const updatedBook = await bookService.markBookAsRead(route.params.id);

        if (!updatedBook) {
          sendError(response, 404, "Book not found.");
          return;
        }

        sendJson(response, 200, { data: updatedBook });
      }
    } catch (error) {
      sendError(response, 500, error.message || "Unexpected server error.");
    }
  };
}
