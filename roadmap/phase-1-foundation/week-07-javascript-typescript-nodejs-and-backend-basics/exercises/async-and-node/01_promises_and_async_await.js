/**
 * This file simulates slow work so you can see how `async` / `await` keeps
 * asynchronous code readable.
 */

function wait(milliseconds) {
  return new Promise((resolve) => {
    setTimeout(resolve, milliseconds);
  });
}

async function loadCourseSection(sectionName, delay) {
  await wait(delay);
  return `Loaded section: ${sectionName}`;
}

async function main() {
  try {
    const foundation = await loadCourseSection("Foundation", 300);
    const aiCore = await loadCourseSection("AI Core", 200);

    console.log(foundation);
    console.log(aiCore);
  } catch (error) {
    console.error("Something failed while loading sections:", error);
  }
}

main();
