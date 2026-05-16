export const jobModel = {
  supportsDurableExecution: true,
  states: ["queued", "running", "completed", "failed"],
  completionSignal: "email-and-dashboard-status",
};
