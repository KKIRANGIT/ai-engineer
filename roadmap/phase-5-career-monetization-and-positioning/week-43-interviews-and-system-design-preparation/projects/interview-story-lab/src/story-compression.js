export function buildIntro(story) {
  return `I build AI product systems for ${story.user}. One project I am proud of is ${story.name}, which improved ${story.result}.`;
}

export function buildWalkthrough(story) {
  return `The problem was ${story.problem}. The system used ${story.architecture}. The key tradeoff was that it ${story.tradeoff}.`;
}
