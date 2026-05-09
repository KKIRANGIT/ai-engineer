/**
 * This exercise shows a few collection helpers and reminds you that modern
 * JavaScript code often favors small reusable functions.
 */

const learners = [
  { name: "Asha", track: "foundation" },
  { name: "Ravi", track: "ai-core" },
  { name: "Mina", track: "foundation" },
];

function groupNamesByTrack(items) {
  return items.reduce((result, learner) => {
    const existingNames = result[learner.track] ?? [];
    return {
      ...result,
      [learner.track]: [...existingNames, learner.name],
    };
  }, {});
}

function findLearnerByName(items, targetName) {
  return items.find((learner) => learner.name.toLowerCase() === targetName.toLowerCase());
}

function main() {
  console.log("Grouped learners:", groupNamesByTrack(learners));
  console.log("Found learner:", findLearnerByName(learners, "mina"));
}

main();
