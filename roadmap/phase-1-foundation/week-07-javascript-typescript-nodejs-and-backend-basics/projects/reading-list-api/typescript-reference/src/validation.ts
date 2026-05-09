import type { CreateBookInput } from "./models";

export interface ValidationResult {
  isValid: boolean;
  errors: string[];
}

export function validateCreateBookInput(input: Partial<CreateBookInput>): ValidationResult {
  const errors: string[] = [];

  if (typeof input.title !== "string" || input.title.trim() === "") {
    errors.push("title must be a non-empty string");
  }

  if (typeof input.author !== "string" || input.author.trim() === "") {
    errors.push("author must be a non-empty string");
  }

  if (
    input.tags !== undefined &&
    (!Array.isArray(input.tags) || input.tags.some((tag) => tag.trim() === ""))
  ) {
    errors.push("tags must be an array of non-empty strings when provided");
  }

  return {
    isValid: errors.length === 0,
    errors,
  };
}
