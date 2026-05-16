export function summarizePipeline(opportunities) {
  return opportunities.reduce(
    (summary, opportunity) => {
      summary.byStage[opportunity.stage] = (summary.byStage[opportunity.stage] || 0) + 1;
      summary.byChannel[opportunity.channel] =
        (summary.byChannel[opportunity.channel] || 0) + 1;
      return summary;
    },
    { byStage: {}, byChannel: {} }
  );
}

export function chooseFocusChannel(opportunities) {
  const ranked = [...opportunities].sort((left, right) => {
    const score = { high: 2, medium: 1, low: 0 };
    return score[right.relevance] - score[left.relevance];
  });

  return ranked[0].channel;
}
