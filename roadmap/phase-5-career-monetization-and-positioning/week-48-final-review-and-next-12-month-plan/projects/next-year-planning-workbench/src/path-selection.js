export function choosePrimaryPath(review) {
  return review.strongestPath;
}

export function pathDecisionMemo(review) {
  return `Primary path: ${review.strongestPath}. This path matches the strongest signal around ${review.bestResponse}.`;
}
