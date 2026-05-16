export function buildRiskRegister(brief) {
  return brief.unknowns.map((unknown) => ({
    risk: unknown,
    mitigation: "validate during discovery before finalizing delivery commitments"
  }));
}
