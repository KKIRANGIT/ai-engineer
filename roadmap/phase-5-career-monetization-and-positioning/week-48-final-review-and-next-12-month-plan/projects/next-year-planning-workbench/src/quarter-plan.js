export function buildQuarterPlan(review) {
  return {
    goal: review.nextQuarterGoal,
    actions: [
      "follow the strongest outreach channel weekly",
      "improve one proof asset each month",
      "close the highest-impact operating gap"
    ]
  };
}
