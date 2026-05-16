export async function* streamSummary(text) {
  const chunks = text.split(" ");

  for (const chunk of chunks) {
    yield chunk;
  }
}

export async function collectStream(generator) {
  const parts = [];

  for await (const chunk of generator) {
    parts.push(chunk);
  }

  return parts;
}
