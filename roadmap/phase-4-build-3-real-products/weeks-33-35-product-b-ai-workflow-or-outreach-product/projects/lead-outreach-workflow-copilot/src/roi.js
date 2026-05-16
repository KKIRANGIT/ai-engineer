export function compareWorkflowMinutes({ manualMinutes, assistedMinutes, tasksPerWeek }) {
  const timeSavedPerTask = manualMinutes - assistedMinutes;
  const weeklyMinutesSaved = timeSavedPerTask * tasksPerWeek;

  return {
    timeSavedPerTask,
    weeklyMinutesSaved,
  };
}
