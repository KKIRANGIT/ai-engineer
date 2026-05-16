export function buildGroundedAnswer(query, topChunks) {
  if (topChunks.length === 0) {
    return {
      query,
      answer:
        "I could not find enough support in the current document set to answer this confidently.",
      supported: false,
      citations: [],
    };
  }

  const leadChunk = topChunks[0];
  const supportingChunks = topChunks.map((chunk) => ({
    documentId: chunk.documentId,
    title: chunk.title,
    heading: chunk.heading,
    excerpt: chunk.text,
  }));

  return {
    query,
    answer: `${leadChunk.text} This answer is grounded in ${leadChunk.title}, section "${leadChunk.heading}".`,
    supported: true,
    citations: supportingChunks,
  };
}
