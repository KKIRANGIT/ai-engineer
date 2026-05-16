import { readFileSync } from "node:fs";

import { buildGroundedAnswer } from "./answer.js";
import { retrieveTopChunks } from "./retrieve.js";

export function loadEvalQuestions(evalPath) {
  return JSON.parse(readFileSync(evalPath, "utf8"));
}

export function runEvalSet(chunks, evalQuestions) {
  return evalQuestions.map((item) => {
    const topChunks = retrieveTopChunks(item.query, chunks);
    const answer = buildGroundedAnswer(item.query, topChunks);
    const topDocumentId = topChunks[0]?.documentId ?? null;

    return {
      query: item.query,
      expectedDocumentId: item.expectedDocumentId,
      topDocumentId,
      passed: topDocumentId === item.expectedDocumentId && answer.supported,
    };
  });
}
