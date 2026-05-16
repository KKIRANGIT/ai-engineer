export function chooseBestChannel(channels) {
  const ranked = [...channels].sort((left, right) => {
    const leftScore = left.userFit * 2 + left.feedbackQuality - left.effort;
    const rightScore = right.userFit * 2 + right.feedbackQuality - right.effort;
    return rightScore - leftScore;
  });

  return ranked[0];
}
