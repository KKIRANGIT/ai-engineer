import { users } from "./data-store.js";

export function createSession(userId) {
  const user = users.find((entry) => entry.id === userId);

  if (!user) {
    throw new Error(`Unknown user: ${userId}`);
  }

  return {
    token: `session:${user.id}`,
    userId: user.id,
    workspaceId: user.workspaceId,
    role: user.role,
  };
}

export function getSessionFromToken(token) {
  if (!token || !token.startsWith("session:")) {
    return null;
  }

  const userId = token.replace("session:", "");

  try {
    return createSession(userId);
  } catch {
    return null;
  }
}
