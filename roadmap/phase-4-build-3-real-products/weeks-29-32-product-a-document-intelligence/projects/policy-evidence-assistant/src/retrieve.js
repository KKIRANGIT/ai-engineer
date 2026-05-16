function tokenize(value) {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, " ")
    .split(/\s+/)
    .filter(Boolean);
}

export function scoreChunk(query, chunk, filters = {}) {
  if (filters.category && filters.category !== chunk.category) {
    return -1;
  }

  if (filters.audience && filters.audience !== chunk.audience) {
    return -1;
  }

  const queryTokens = tokenize(query);
  const chunkTokens = new Set(tokenize(`${chunk.title} ${chunk.heading} ${chunk.text}`));

  return queryTokens.reduce((score, token) => score + (chunkTokens.has(token) ? 1 : 0), 0);
}

export function retrieveTopChunks(query, chunks, filters = {}, limit = 3) {
  return chunks
    .map((chunk) => ({
      ...chunk,
      score: scoreChunk(query, chunk, filters),
    }))
    .filter((chunk) => chunk.score > 0)
    .sort((left, right) => right.score - left.score)
    .slice(0, limit);
}
