import { getPathSegments } from "./request-utils.js";

export function matchRoute(method, pathname) {
  const segments = getPathSegments(pathname);

  if (method === "GET" && pathname === "/health") {
    return { name: "health" };
  }

  if (method === "GET" && pathname === "/books") {
    return { name: "listBooks" };
  }

  if (method === "POST" && pathname === "/books") {
    return { name: "createBook" };
  }

  if (method === "GET" && segments.length === 2 && segments[0] === "books") {
    return { name: "getBookById", params: { id: segments[1] } };
  }

  if (
    method === "PATCH" &&
    segments.length === 3 &&
    segments[0] === "books" &&
    segments[2] === "read"
  ) {
    return { name: "markBookAsRead", params: { id: segments[1] } };
  }

  return null;
}
