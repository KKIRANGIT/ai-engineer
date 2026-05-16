export function totalWeeklyTouches(target) {
  return target.newSends + target.followUps + target.contentTouches;
}

export function rhythmSummary(target) {
  return `Weekly rhythm: ${target.newSends} new sends, ${target.followUps} follow-ups, ${target.contentTouches} content touch.`;
}
