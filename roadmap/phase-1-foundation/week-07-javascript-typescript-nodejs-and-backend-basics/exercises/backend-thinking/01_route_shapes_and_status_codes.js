/**
 * This exercise is about mental models rather than networking. It shows how
 * different route outcomes should map to status codes and response shapes.
 */

function buildResponse(statusCode, payload) {
  return {
    statusCode,
    body: payload,
  };
}

function getBookByIdResponse(book) {
  if (!book) {
    return buildResponse(404, {
      error: "Not Found",
      message: "The requested book does not exist.",
    });
  }

  return buildResponse(200, {
    data: book,
  });
}

function main() {
  console.log(
    "Success response:",
    getBookByIdResponse({ id: "book-1", title: "Clean Architecture" }),
  );
  console.log("Not found response:", getBookByIdResponse(null));
}

main();
