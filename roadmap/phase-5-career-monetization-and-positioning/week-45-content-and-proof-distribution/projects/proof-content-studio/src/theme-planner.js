export function chooseLeadTheme(assets) {
  return assets[0];
}

export function summarizeTheme(asset) {
  return `${asset.theme} for ${asset.audience} using ${asset.proof}.`;
}
