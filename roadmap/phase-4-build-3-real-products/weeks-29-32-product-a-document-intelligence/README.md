# Weeks 29-32: Product A - Document Intelligence

Back to [Phase 4](../README.md)

## Goal

Build a grounded document assistant for a specific real-world use case where trust, source quality, and retrieval behavior matter.

This track is about evidence-backed answers, not generic chat over files.

## Why This Product Category Matters

Document-heavy workflows are everywhere:

- legal review
- compliance and policy reading
- insurance processing
- financial analysis
- operations SOP lookup
- internal knowledge access

These workflows are strong product candidates because:

- the pain is familiar
- the value proposition is understandable
- grounding matters
- there is often clear time-saving value

This category is also unforgiving, which makes it a strong portfolio test:

- hallucinations are visible
- retrieval errors matter
- citation quality matters
- upload and parsing reliability matter

## What This Track Is Actually Training

This track is training six deeper skills:

1. choosing a narrow document workflow with believable pain
2. ingesting and structuring real source material
3. debugging retrieval rather than blaming the model vaguely
4. exposing evidence clearly enough that users can trust or challenge an answer
5. evaluating failure cases with concrete question sets
6. turning a technically correct assistant into a product case study

The real outcome is not "I built chat with PDFs." The real outcome is "I built a focused document product with evidence, boundaries, and a believable user workflow."

## Scope Boundary For This Track

This track focuses on:

- document ingestion
- metadata modeling
- chunking and retrieval
- grounded answer generation
- citation and debug UX
- failure analysis and tester feedback

This track does not require:

- broad multi-tenant SaaS complexity
- every document format under the sun
- heavy design-system work
- advanced agent orchestration for its own sake

The correct goal is a narrow, high-trust product with inspectable retrieval behavior.

## What This Product Should Prove

By the end of this track, your product should prove that you can:

- choose a narrow document use case
- ingest real documents
- ground answers in source material
- present sources clearly
- improve the system based on retrieval and answer failures

## Recommended Niches

Good niches for this product include:

- legal summaries
- company policy assistants
- insurance claim support docs
- due-diligence or report assistants
- internal SOP and operations assistants

Choose a niche where:

- documents are dense
- users ask repeated questions
- users currently waste time searching manually

## Success Criteria For This Product

You should consider the product successful if:

- a user can upload or access relevant documents
- the system can answer a meaningful set of grounded questions
- the answer shows useful evidence or citations
- the retrieval behavior is inspectable
- the user can tell when the system is uncertain or unsupported

## What To Optimize

This product should optimize for:

- retrieval quality
- hallucination resistance
- upload reliability
- chunk relevance
- source clarity
- question-answer trust

Do not over-optimize for fancy UI before the core trust loop works.

## What To Learn While Building

This track should sharpen your understanding of:

- document ingestion
- parsing and text extraction
- chunk design
- metadata-aware retrieval
- grounded generation
- citation UX
- retrieval debugging
- evaluation design for knowledge tasks

## Best Source Strategy For This Track

Use sources in this order:

1. the local Product A workspace
2. your earlier Phase 2 retrieval and grounding notes
3. one or two official docs for the stack or libraries you actually use

Do not overload this track with many vector-database tutorials. The value comes from understanding why grounded retrieval succeeds or fails for this product.

## Recommended Official References

Use these as the small external companion stack:

- OpenAI RAG guide: <https://platform.openai.com/docs/guides/retrieval>
- Anthropic prompt engineering overview: <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview>
- MDN File API: <https://developer.mozilla.org/en-US/docs/Web/API/File_API>

These are enough to support the product build without pushing you into source overload.

## Execution Plan

### Week 29: Scope and ingestion

Focus:

- choose the niche
- gather representative documents
- design ingestion and metadata model

Deliverables:

- product brief
- sample document set
- ingestion plan

Questions to answer:

- what kinds of documents will this product handle
- how large are they
- what metadata will be needed for filtering or trust

### Week 30: Retrieval and grounding

Focus:

- chunking strategy
- retrieval implementation
- source display format

Deliverables:

- working retrieval-backed question flow
- first grounded responses
- retrieval debug output

Questions to answer:

- what chunk size works best for the document type
- what metadata filters improve relevance
- how will users inspect support for an answer

### Week 31: Quality and trust

Focus:

- evaluate failure cases
- improve grounding behavior
- reduce unsupported claims

Deliverables:

- question test set
- failure log
- revised prompt or retrieval strategy

Questions to answer:

- where do wrong answers come from
- is the problem retrieval, context packing, or synthesis
- how do you communicate uncertainty

### Week 32: Product polish and feedback

Focus:

- improve workflow clarity
- collect tester feedback
- prepare case-study material

Deliverables:

- product demo
- user feedback notes
- case study

## Build Requirements

At minimum, the product should include:

- file upload or document selection
- parsing and chunking
- metadata-aware retrieval
- grounded answers with visible sources
- simple usage or query logging
- basic evaluation set

Recommended additions:

- document-level filters
- debug view for retrieved chunks
- answer feedback mechanism

## Hands-On Workspace Structure

```text
weeks-29-32-product-a-document-intelligence/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- week-29-scope-and-ingestion/
|   |-- week-30-retrieval-and-grounding/
|   |-- week-31-quality-and-trust/
|   `-- week-32-product-polish-and-feedback/
|-- notes/
|   |-- 01-track-plan.md
|   |-- 02-retrieval-debugging-guide.md
|   |-- 03-feedback-interview-guide.md
|   `-- 04-case-study-outline.md
`-- projects/
    `-- policy-evidence-assistant/
```

## Exercises

The exercises are organized by week so the product build stays disciplined instead of turning into a random prototype sprint.

You will practice:

- defining the niche and ingestion constraints
- designing retrieval and metadata filters
- logging failure cases and trust gaps
- collecting feedback and shaping the case study

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [policy-evidence-assistant](projects/policy-evidence-assistant/README.md)

This project is a focused document-intelligence product for internal policy and operations answers. It teaches:

- document ingestion from a controlled corpus
- metadata-aware chunk retrieval
- grounded answer generation with citations
- retrieval debug inspection
- simple eval and query logging

It stays narrow on purpose so you can inspect the trust loop instead of hiding weak retrieval behind a larger app shell.

## User Validation Expectations

Try to get at least 3-5 real testers, even if informal.

Ask them:

- was the answer useful
- did they trust the answer
- did the sources help
- what type of question failed

## Deliverables

By the end of this track, you should have:

- one document intelligence product demo
- representative document set
- grounded question test set
- user feedback notes
- case study

## Exit Criteria

You are ready to move to Product B only if:

- the product answers a meaningful set of questions from the document set
- the citations are inspectable and relevant
- you can explain at least one retrieval failure clearly
- you have a basic eval set and query log
- you have external or simulated tester feedback recorded

## Common Mistakes To Avoid

- building generic "chat with PDF" with no domain focus
- hiding sources or making them hard to inspect
- assuming all failures are model failures instead of retrieval failures
- ignoring document ingestion quality
- trying to support every file type before the niche is proven

## Expert Notes That Matter Here

### Trust is the core product feature

In document intelligence, the strongest UX feature is often not style. It is evidence.

### Domain scope is product strategy

A narrow, high-value document niche is better than a broad generic assistant.

### Retrieval debugging is a competitive advantage

Most weak products fail because their builders cannot explain why the system answered badly.

## Final Standard For This Track

The correct outcome is not:

"I built a PDF chatbot."

The correct outcome is:

"I built a focused document-intelligence product that answers grounded questions, exposes evidence clearly, and has enough domain specificity to be believable."
