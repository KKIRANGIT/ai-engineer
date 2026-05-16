export function groupError(error) {
  if (error.code === "AI_TIMEOUT") {
    return "provider-latency";
  }

  if (error.code === "AUTH_SCOPE_FAILURE") {
    return "access-control";
  }

  return "unknown";
}
