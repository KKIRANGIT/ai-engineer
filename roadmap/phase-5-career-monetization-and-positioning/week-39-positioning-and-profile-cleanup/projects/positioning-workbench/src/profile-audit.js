function normalizeToken(token) {
  const cleaned = token.toLowerCase().replace(/[^a-z0-9]/g, "");
  return cleaned.endsWith("s") ? cleaned.slice(0, -1) : cleaned;
}

function tokenizeSignals(signals) {
  return signals
    .flatMap((signal) => signal.split(/\s+/))
    .map(normalizeToken)
    .filter((token) => token.length > 2);
}

function overlapCount(leftSignals, rightSignals) {
  const rightSet = new Set(tokenizeSignals(rightSignals));
  return tokenizeSignals(leftSignals).filter((token) => rightSet.has(token)).length;
}

export function auditProfileConsistency(profile) {
  const headlineSummaryOverlap = overlapCount(profile.headlineSignals, profile.summarySignals);
  const summaryGithubOverlap = overlapCount(profile.summarySignals, profile.githubSignals);

  return {
    headlineSummaryOverlap,
    summaryGithubOverlap,
    consistent: headlineSummaryOverlap >= 1 && summaryGithubOverlap >= 1,
  };
}
