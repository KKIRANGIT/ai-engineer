export function repurposeAsset(asset) {
  return {
    articleHook: `I learned that ${asset.lesson} while building ${asset.project}.`,
    socialPost: `Building ${asset.project} taught me that ${asset.lesson}.`,
    portfolioSnippet: `${asset.project}: ${asset.proof}.`
  };
}
