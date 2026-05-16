import { readFileSync } from "node:fs";

export function loadTasks(tasksPath) {
  return JSON.parse(readFileSync(tasksPath, "utf8"));
}
