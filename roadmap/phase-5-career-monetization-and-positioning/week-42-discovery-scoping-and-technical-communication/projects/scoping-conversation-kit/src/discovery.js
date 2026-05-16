export function buildDiscoveryQuestions(brief) {
  return [
    `How does ${brief.workflow} work today from start to finish?`,
    `What does success look like for ${brief.client}?`,
    `Which constraints are non-negotiable, especially around ${brief.constraints[0]}?`
  ];
}
