export function buildPortfolioSummary(project, target) {
  const projectText = `${project.problem} ${project.system}`.toLowerCase();
  const alignedTheme =
    [...target.priorityThemes]
      .sort((left, right) => themeScore(right, projectText) - themeScore(left, projectText))[0] ||
    target.priorityThemes[0];

  return {
    title: project.name,
    audience: target.targetBuyer,
    summary: `For ${project.user}, I built a ${project.system} that addressed ${project.problem}. The work emphasized ${alignedTheme} and ${project.tradeoff}.`,
    result: project.result
  };
}

function themeScore(theme, projectText) {
  return theme
    .toLowerCase()
    .split(/\s+/)
    .reduce((score, token) => {
      return projectText.includes(token) ? score + 1 : score;
    }, 0);
}
