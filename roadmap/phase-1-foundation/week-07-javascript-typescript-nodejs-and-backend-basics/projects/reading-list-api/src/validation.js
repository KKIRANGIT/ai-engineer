function isNonEmptyString(value) {
  return typeof value === "string" && value.trim() !== "";
}

function areStringTags(tags) {
  return Array.isArray(tags) && tags.every((tag) => typeof tag === "string" && tag.trim() !== "");
}

export function validateNewBookInput(input) {
  const errors = [];

  if (!isNonEmptyString(input.title)) {
    errors.push("title must be a non-empty string");
  }

  if (!isNonEmptyString(input.author)) {
    errors.push("author must be a non-empty string");
  }

  if (input.tags !== undefined && !areStringTags(input.tags)) {
    errors.push("tags must be an array of non-empty strings when provided");
  }

  return {
    isValid: errors.length === 0,
    errors,
  };
}
