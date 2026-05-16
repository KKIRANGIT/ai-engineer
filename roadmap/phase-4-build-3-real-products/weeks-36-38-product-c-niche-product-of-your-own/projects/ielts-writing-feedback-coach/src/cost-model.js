export function estimateSessionCost({ tokensPerEssay, costPerThousandTokens = 0.003 }) {
  return Number(((tokensPerEssay / 1000) * costPerThousandTokens).toFixed(4));
}

export function estimateContributionMargin({ pricePerMonth, essaysPerMonth, sessionCost }) {
  const monthlyCost = essaysPerMonth * sessionCost;
  return Number((pricePerMonth - monthlyCost).toFixed(2));
}
