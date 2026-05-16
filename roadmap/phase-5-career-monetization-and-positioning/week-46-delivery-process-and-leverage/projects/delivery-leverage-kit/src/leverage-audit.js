export function rankReusableTasks(process) {
  return [...process.repeatedTasks].sort((left, right) => {
    const leftScore = left.frequency + left.risk;
    const rightScore = right.frequency + right.risk;
    return rightScore - leftScore;
  });
}
