import { estimateOverallBand, scoreEssay } from "./rubric.js";

export function buildFeedback(submission) {
  const scores = scoreEssay(submission.essay);
  const overallBand = estimateOverallBand(scores);

  const priorities = [];

  if (scores.taskResponse < 6) {
    priorities.push("Develop the argument more fully before ending the essay.");
  }

  if (scores.coherenceAndCohesion < 6) {
    priorities.push("Use clearer paragraph progression and linking between ideas.");
  }

  if (scores.lexicalResource < 6) {
    priorities.push("Increase topic-specific vocabulary and avoid repeating simple words.");
  }

  if (scores.grammaticalRangeAndAccuracy < 6) {
    priorities.push("Use a wider range of sentence structures while checking accuracy.");
  }

  if (priorities.length === 0) {
    priorities.push("Strengthen examples and precision to push the response toward a higher band.");
  }

  return {
    submissionId: submission.submissionId,
    overallBand,
    scores,
    priorities,
  };
}
