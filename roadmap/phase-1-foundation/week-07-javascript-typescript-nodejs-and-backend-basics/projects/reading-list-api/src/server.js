import http from "node:http";
import { createApp } from "./app.js";
import { BookService } from "./book-service.js";
import * as storage from "./storage.js";

const port = Number(process.env.PORT || 4000);
const bookService = new BookService(storage);
const app = createApp({ bookService });

const server = http.createServer(app);

server.listen(port, () => {
  console.log(`Reading List API is running on http://localhost:${port}`);
  console.log(`Data file: ${storage.getDatabaseFilePath()}`);
});
