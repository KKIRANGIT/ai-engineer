import test from "node:test";
import assert from "node:assert/strict";
import { validateNewBookInput } from "../src/validation.js";

test("validateNewBookInput accepts a valid payload", () => {
  const result = validateNewBookInput({
    title: "Clean Architecture",
    author: "Robert C. Martin",
    tags: ["architecture", "clean-code"],
  });

  assert.equal(result.isValid, true);
  assert.deepEqual(result.errors, []);
});

test("validateNewBookInput returns helpful errors for bad input", () => {
  const result = validateNewBookInput({
    title: "",
    author: 10,
    tags: "backend",
  });

  assert.equal(result.isValid, false);
  assert.deepEqual(result.errors, [
    "title must be a non-empty string",
    "author must be a non-empty string",
    "tags must be an array of non-empty strings when provided",
  ]);
});
