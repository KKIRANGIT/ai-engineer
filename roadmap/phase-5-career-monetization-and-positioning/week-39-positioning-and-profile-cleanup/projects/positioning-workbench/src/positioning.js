export function buildPositioningStatement(profile) {
  return `I build ${profile.builderType} systems for ${profile.userType} so they can ${profile.outcome}.`;
}

export function buildVerbalIntro(profile, projectNames) {
  const projectProof = projectNames.slice(0, 2).join(" and ");
  return `I build ${profile.builderType} systems for ${profile.userType}. Recently I worked on ${projectProof} to help teams ${profile.outcome}.`;
}
