export function createAttemptRegistry() {
  return new Set();
}

export function shouldProcessAttempt(registry, attemptKey) {
  if (registry.has(attemptKey)) {
    return false;
  }

  registry.add(attemptKey);
  return true;
}
