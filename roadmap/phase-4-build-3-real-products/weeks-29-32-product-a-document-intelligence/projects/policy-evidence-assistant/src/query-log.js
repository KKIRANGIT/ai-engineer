export function createQueryLogEntry({ query, filters, topChunks, supported }) {
  return {
    query,
    filters,
    supported,
    chunkIds: topChunks.map((chunk) => chunk.chunkId),
    timestamp: "sample-log-entry",
  };
}
