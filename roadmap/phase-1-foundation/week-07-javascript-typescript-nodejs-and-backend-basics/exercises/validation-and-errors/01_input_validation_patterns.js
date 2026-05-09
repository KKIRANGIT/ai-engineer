/**
 * Incoming data should be checked before the rest of the program relies on it.
 * This example uses a simple array of error messages instead of a framework.
 */

function validateNewBookInput(input) {
  const errors = [];

  if (typeof input.title !== "string" || input.title.trim() === "") {
    errors.push("title must be a non-empty string");
  }

  if (typeof input.author !== "string" || input.author.trim() === "") {
    errors.push("author must be a non-empty string");
  }

  if (input.tags !== undefined && !Array.isArray(input.tags)) {
    errors.push("tags must be an array when provided");
  }

  return {
    isValid: errors.length === 0,
    errors,
  };
}

function main() {
  const validBook = {
    title: "Patterns of Enterprise Application Architecture",
    author: "Martin Fowler",
    tags: ["architecture", "design"],
  };

  const invalidBook = {
    title: "",
    author: 42,
    tags: "architecture",
  };

  console.log("Valid book result:", validateNewBookInput(validBook));
  console.log("Invalid book result:", validateNewBookInput(invalidBook));
}

main();
