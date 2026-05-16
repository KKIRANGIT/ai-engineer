export function suggestedRate(rateCard, options) {
  let rate = rateCard.baseRate;

  if (options.complex) {
    rate *= rateCard.complexityMultiplier;
  }

  if (options.urgent) {
    rate *= rateCard.urgencyMultiplier;
  }

  return rate;
}
