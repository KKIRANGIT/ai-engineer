import test from "node:test";
import assert from "node:assert/strict";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { buildGroundedAnswer } from "../src/answer.js";
import { chunkDocuments } from "../src/chunk-documents.js";
import { runEvalSet, loadEvalQuestions } from "../src/evals.js";
import { loadDocuments } from "../src/load-documents.js";
import { createQueryLogEntry } from "../src/query-log.js";
import { retrieveTopChunks } from "../src/retrieve.js";

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const documentsDir = path.join(currentDir, "..", "data", "documents");
const evalPath = path.join(currentDir, "..", "data", "evals", "questions.json");

const documents = loadDocuments(documentsDir);
const chunks = chunkDocuments(documents);

test("document loader parses frontmatter and body", () => {
  const securityDoc = documents.find((document) => document.id === "security-access-policy");

  assert.equal(securityDoc.category, "security");
  assert.match(securityDoc.body, /quarter/);
});

test("chunking keeps section-level metadata", () => {
  const chunk = chunks.find((entry) => entry.chunkId === "travel-expense-policy::1");

  assert.equal(chunk.heading, "Receipt Rules");
  assert.equal(chunk.category, "finance");
});

test("retrieval surfaces the expected policy chunk", () => {
  const topChunks = retrieveTopChunks(
    "When do managers review privileged access?",
    chunks,
    { category: "security" }
  );

  assert.equal(topChunks[0].documentId, "security-access-policy");
  assert.match(topChunks[0].text, /quarter/);
});

test("grounded answers expose citations", () => {
  const topChunks = retrieveTopChunks("Do I need receipts over seventy-five dollars?", chunks);
  const answer = buildGroundedAnswer("Do I need receipts over seventy-five dollars?", topChunks);

  assert.equal(answer.supported, true);
  assert.ok(answer.citations.length >= 1);
  assert.equal(answer.citations[0].documentId, "travel-expense-policy");
});

test("eval set passes for the bundled representative questions", () => {
  const evalQuestions = loadEvalQuestions(evalPath);
  const results = runEvalSet(chunks, evalQuestions);

  assert.ok(results.every((result) => result.passed));
});

test("query logs preserve retrieved chunk ids", () => {
  const topChunks = retrieveTopChunks("Can a new employee work remotely in the first month?", chunks);
  const logEntry = createQueryLogEntry({
    query: "Can a new employee work remotely in the first month?",
    filters: { audience: "employees" },
    topChunks,
    supported: true,
  });

  assert.ok(logEntry.chunkIds.length >= 1);
  assert.equal(logEntry.filters.audience, "employees");
});
