/**
 * Node.js gives JavaScript access to the file system. This example reads a
 * local JSON file and turns it into normal JavaScript objects.
 */

import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const currentFilePath = fileURLToPath(import.meta.url);
const currentDirectory = path.dirname(currentFilePath);
const sampleFilePath = path.join(currentDirectory, "sample-course-data.json");

async function loadCourseData() {
  const rawText = await readFile(sampleFilePath, "utf-8");
  return JSON.parse(rawText);
}

async function main() {
  try {
    const data = await loadCourseData();
    console.log("Course name:", data.courseName);
    console.log("Modules:", data.modules);
  } catch (error) {
    console.error("Could not load the sample JSON file:", error.message);
  }
}

main();
