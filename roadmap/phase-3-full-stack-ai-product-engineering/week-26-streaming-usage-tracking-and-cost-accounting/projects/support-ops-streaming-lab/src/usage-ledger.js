export function recordUsage(entries, entry) {
  return [
    ...entries,
    entry,
  ];
}

export function summarizeUsageByUser(entries, userId) {
  return entries
    .filter((entry) => entry.userId === userId)
    .reduce(
      (summary, entry) => ({
        requests: summary.requests + 1,
        units: summary.units + entry.units,
      }),
      { requests: 0, units: 0 }
    );
}
