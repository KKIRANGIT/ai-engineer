function countWords(text) {
  return text.split(/\s+/).filter(Boolean).length;
}

function countSentences(text) {
  return text.split(/[.!?]+/).map((part) => part.trim()).filter(Boolean).length;
}

export function scoreEssay(essay) {
  const words = countWords(essay);
  const sentences = countSentences(essay);
  const longEnough = words >= 220;
  const hasBalancedStructure = sentences >= 4;

  return {
    taskResponse: longEnough ? 6.5 : 5.5,
    coherenceAndCohesion: hasBalancedStructure ? 6.5 : 5.5,
    lexicalResource: words >= 180 ? 6 : 5.5,
    grammaticalRangeAndAccuracy: sentences >= 4 ? 6 : 5.5,
  };
}

export function estimateOverallBand(scores) {
  const values = Object.values(scores);
  const average = values.reduce((sum, value) => sum + value, 0) / values.length;

  return Number(average.toFixed(1));
}
