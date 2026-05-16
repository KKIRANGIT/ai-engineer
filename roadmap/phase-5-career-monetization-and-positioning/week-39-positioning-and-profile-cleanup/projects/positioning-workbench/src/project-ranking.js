export function scoreProject(project) {
  return project.relevance + project.proof + project.differentiation + project.valueClarity;
}

export function rankProjects(projects) {
  return [...projects].sort((left, right) => scoreProject(right) - scoreProject(left));
}
