/**
 * This file demonstrates how TypeScript can describe the shape of an object
 * more explicitly than plain JavaScript.
 */

interface LearnerProfile {
  name: string;
  currentWeek: number;
  isConsistent: boolean;
}

function formatLearnerProfile(profile: LearnerProfile): string {
  return `${profile.name} is on Week ${profile.currentWeek}. Consistent: ${profile.isConsistent}`;
}

const profile: LearnerProfile = {
  name: "Asha",
  currentWeek: 7,
  isConsistent: true,
};

console.log(formatLearnerProfile(profile));
