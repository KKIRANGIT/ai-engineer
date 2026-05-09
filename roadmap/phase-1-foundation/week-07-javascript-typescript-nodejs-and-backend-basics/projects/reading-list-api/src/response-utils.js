export function sendJson(response, statusCode, payload) {
  response.writeHead(statusCode, {
    "Content-Type": "application/json",
  });
  response.end(JSON.stringify(payload, null, 2));
}

export function sendError(response, statusCode, message, details = []) {
  sendJson(response, statusCode, {
    error: statusCode >= 500 ? "Server Error" : "Request Error",
    message,
    details,
  });
}
