export function buildChecklist(process) {
  return process.repeatedTasks.map((task) => `${task.name}: define a reusable review step`);
}
