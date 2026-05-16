import { plans } from "./plans.js";

export function buildCheckoutSession(user, planKey) {
  const plan = plans[planKey];

  if (!plan || plan.monthlyPriceCents === 0) {
    throw new Error("Checkout requires a paid plan");
  }

  return {
    mode: "subscription",
    customerEmail: user.email,
    metadata: {
      userId: user.id,
      workspaceId: user.workspaceId,
      planKey,
    },
    successUrl: "https://example.test/billing/success",
    cancelUrl: "https://example.test/billing/cancel",
  };
}
