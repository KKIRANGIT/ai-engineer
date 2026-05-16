import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";

export function loadSubmissions(submissionsDir) {
  const filenames = readdirSync(submissionsDir).filter((name) => name.endsWith(".json"));

  return filenames.map((filename) => {
    const fullPath = path.join(submissionsDir, filename);
    return JSON.parse(readFileSync(fullPath, "utf8"));
  });
}
