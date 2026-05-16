export function buildResumeBullets(project) {
  return [
    `Built a ${project.system} for ${project.user} to address ${project.problem}, which ${project.result}.`,
    `Made a deliberate tradeoff by ${project.tradeoff}, keeping the system aligned with real-world quality expectations.`
  ];
}
