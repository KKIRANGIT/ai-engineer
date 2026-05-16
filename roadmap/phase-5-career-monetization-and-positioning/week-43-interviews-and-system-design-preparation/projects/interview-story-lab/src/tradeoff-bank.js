export function buildTradeoffAnswers(story) {
  return [
    `We used retrieval because the workflow required grounded answers for ${story.user}.`,
    `The main tradeoff was that we ${story.tradeoff}.`,
    "We treated failure handling as part of the product trust model, not an afterthought."
  ];
}
