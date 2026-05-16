export function buildMessage(templateContext) {
  return `I noticed ${templateContext.context}. I recently built ${templateContext.projectProof} around ${templateContext.proofTheme}, which is why your ${templateContext.targetType} stood out to me.`;
}
