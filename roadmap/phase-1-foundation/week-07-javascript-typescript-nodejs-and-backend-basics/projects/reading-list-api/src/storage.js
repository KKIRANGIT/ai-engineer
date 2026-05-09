import { copyFile, mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const currentFilePath = fileURLToPath(import.meta.url);
const currentDirectory = path.dirname(currentFilePath);
const dataDirectory = path.join(currentDirectory, "..", "data");
const seedFilePath = path.join(dataDirectory, "seed-reading-list.json");
const databaseFilePath = path.join(dataDirectory, "reading-list.json");

async function ensureDataFileExists() {
  await mkdir(dataDirectory, { recursive: true });

  try {
    await readFile(databaseFilePath, "utf-8");
  } catch {
    await copyFile(seedFilePath, databaseFilePath);
  }
}

export async function loadBooks() {
  await ensureDataFileExists();
  const rawText = await readFile(databaseFilePath, "utf-8");
  return JSON.parse(rawText);
}

export async function saveBooks(books) {
  await ensureDataFileExists();
  await writeFile(databaseFilePath, JSON.stringify(books, null, 2));
}

export function getDatabaseFilePath() {
  return databaseFilePath;
}
