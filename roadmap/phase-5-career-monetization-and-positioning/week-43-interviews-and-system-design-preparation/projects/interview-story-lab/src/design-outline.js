export function buildDesignOutline(story) {
  return {
    requirements: [story.problem, story.result],
    components: story.architecture.split(", "),
    tradeoff: story.tradeoff
  };
}
