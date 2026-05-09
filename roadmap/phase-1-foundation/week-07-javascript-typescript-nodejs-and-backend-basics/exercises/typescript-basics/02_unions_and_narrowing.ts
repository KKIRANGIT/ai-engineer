/**
 * Union types let a value be one of several allowed shapes. Narrowing is the
 * process of determining which specific shape you currently have.
 */

type StatusMessage = string | number;

function formatStatus(value: StatusMessage): string {
  if (typeof value === "number") {
    return `Numeric status code: ${value}`;
  }

  return `Text status message: ${value.toUpperCase()}`;
}

console.log(formatStatus(200));
console.log(formatStatus("created"));
