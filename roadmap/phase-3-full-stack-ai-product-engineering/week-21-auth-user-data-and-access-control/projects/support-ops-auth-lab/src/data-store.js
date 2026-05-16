export const users = [
  { id: "u-alice", name: "Alice", workspaceId: "w-acme", role: "admin" },
  { id: "u-bob", name: "Bob", workspaceId: "w-acme", role: "member" },
  { id: "u-cora", name: "Cora", workspaceId: "w-bravo", role: "admin" },
];

export const tickets = [
  {
    id: "t-101",
    workspaceId: "w-acme",
    title: "Broken billing export",
    assigneeUserId: "u-bob",
    createdByUserId: "u-alice",
    status: "open",
  },
  {
    id: "t-102",
    workspaceId: "w-acme",
    title: "Urgent access review",
    assigneeUserId: "u-alice",
    createdByUserId: "u-bob",
    status: "triage",
  },
  {
    id: "t-201",
    workspaceId: "w-bravo",
    title: "EU workspace latency spike",
    assigneeUserId: "u-cora",
    createdByUserId: "u-cora",
    status: "open",
  },
];
