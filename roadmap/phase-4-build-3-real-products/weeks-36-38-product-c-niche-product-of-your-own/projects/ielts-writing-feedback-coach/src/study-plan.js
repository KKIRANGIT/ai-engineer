export function buildNextStepPlan(feedback) {
  return {
    primaryFocus: feedback.priorities[0],
    nextPractice: [
      "Rewrite one body paragraph with stronger examples.",
      "Review the rubric dimension linked to the weakest score.",
      "Submit one more essay within two days to check improvement.",
    ],
  };
}
