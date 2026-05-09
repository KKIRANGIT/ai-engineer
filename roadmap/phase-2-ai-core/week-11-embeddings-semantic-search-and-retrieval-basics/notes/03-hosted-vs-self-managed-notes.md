# Hosted vs Self-Managed Retrieval Notes

Back to [Week 11](../README.md)

## Hosted Retrieval

Examples:

- OpenAI Retrieval API
- File Search in Responses

Advantages:

- fast setup
- less infrastructure work
- provider-managed chunking, indexing, and search

Tradeoffs:

- less transparent mechanics
- less control over chunking and ranking details
- provider-specific pricing and behavior

## Self-Managed Retrieval

Examples:

- `pgvector`
- custom vector stores
- hybrid ranking pipelines

Advantages:

- full control over chunking, filters, and ranking
- easier debugging of your own logic
- better fit for custom retrieval design

Tradeoffs:

- more implementation complexity
- more infrastructure responsibility
- more tuning responsibility

## Good Engineering Attitude

Learn the mechanics deeply enough that hosted retrieval is a convenience choice, not a mystery box you depend on blindly.
