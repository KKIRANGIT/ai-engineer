import { activationEvents, isKnownEvent } from "./event-taxonomy.js";

export function recordEvent(name, properties = {}) {
  if (!isKnownEvent(name)) {
    throw new Error(`Unknown event: ${name}`);
  }

  return {
    name,
    properties,
  };
}

export function summarizeActivationFunnel(events) {
  const seen = new Set(events.map((event) => event.name));

  return activationEvents.map((name) => ({
    name,
    completed: seen.has(name),
  }));
}
