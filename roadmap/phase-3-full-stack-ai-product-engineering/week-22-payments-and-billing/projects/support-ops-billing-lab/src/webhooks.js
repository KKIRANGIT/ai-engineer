export function reduceBillingState(currentState, event) {
  switch (event.type) {
    case "checkout.session.completed":
      return {
        ...currentState,
        planKey: event.planKey,
        status: "active",
        subscriptionId: event.subscriptionId,
      };
    case "invoice.payment_failed":
      return {
        ...currentState,
        status: "past_due",
      };
    case "customer.subscription.updated":
      return {
        ...currentState,
        planKey: event.planKey ?? currentState.planKey,
        status: event.status,
      };
    case "customer.subscription.deleted":
      return {
        ...currentState,
        status: "canceled",
      };
    default:
      return currentState;
  }
}
