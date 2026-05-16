export const topology = [
  { component: "web-app", owns: ["ui", "navigation", "streamed views"] },
  { component: "app-server", owns: ["route handlers", "policy checks"] },
  { component: "worker", owns: ["slow analysis jobs", "retries"] },
  { component: "database", owns: ["tickets", "usage", "billing state"] },
];
