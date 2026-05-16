export function proofStrength(asset) {
  return [asset.project, asset.proof, asset.lesson].filter(Boolean).length;
}

export function isProofBacked(asset) {
  return proofStrength(asset) >= 3;
}
