# Weeks 33-35: Product B - AI Workflow or Outreach Product

Back to [Phase 4](../README.md)

## Goal

Build a workflow automation product that combines model output, tools, execution steps, and real task completion rather than only information delivery.

This is the product track where your system should start doing useful work on behalf of the user.

## Why This Product Category Matters

Workflow products are often commercially attractive because they can show:

- time saved
- reduced repetitive work
- better throughput
- more consistent outputs

This category is also where many AI products break in subtle ways, because usefulness depends on:

- structured outputs
- correct tool use
- human review boundaries
- retry-safe execution
- integration with external systems

That makes it a strong test of Phase 2 and Phase 3 together.

## What This Product Should Prove

By the end of this track, your product should prove that you can:

- model a repeated workflow
- identify where AI adds leverage
- connect tools and execution safely
- measure whether the workflow is actually better than the manual baseline
- communicate ROI clearly

## Good Product Directions

Examples:

- lead research and outreach drafting
- support ticket triage
- resume screening workflow
- meeting preparation assistant
- sales call summarization and follow-up drafting

Choose a workflow where:

- repetition is real
- the manual process is expensive or slow
- there is a clear before/after story

## Success Criteria For This Product

You should consider the product successful if:

- the workflow is clearly defined
- the system can complete a meaningful subset of the workflow
- outputs are structured and usable
- human review is possible where needed
- you can explain time saved or quality improved

## What To Optimize

This product should optimize for:

- task completion rate
- reduction in manual effort
- structured output reliability
- correct use of tools or integrations
- clarity of approval and review flow

## What To Learn While Building

This track should strengthen your understanding of:

- structured outputs
- tool use
- job workflows
- human-in-the-loop boundaries
- side-effect safety
- workflow evaluation
- ROI framing

## Execution Plan

## Week 33: Workflow analysis and decomposition

Focus:

- choose the workflow
- map the manual steps
- identify where AI helps and where deterministic logic helps

Deliverables:

- workflow map
- before/after process note
- product brief

Questions to answer:

- what step actually creates the most pain
- what should be automated
- what must still be reviewed by a human

## Week 34: Build the workflow engine

Focus:

- structured output design
- tool and integration layer
- background execution where needed

Deliverables:

- working workflow path
- logs or traces
- first end-to-end outputs

Questions to answer:

- what output shape is required at each stage
- which tool boundaries need validation
- which steps can fail independently

## Week 35: Quality, ROI, and product story

Focus:

- compare manual workflow vs product workflow
- identify failure points
- gather user or tester feedback

Deliverables:

- before-vs-after workflow comparison
- realistic sample tasks
- ROI-oriented case study

## Build Requirements

At minimum, the product should include:

- structured outputs
- at least one meaningful tool or external action path
- clear workflow states
- approval or review step if side effects matter
- background processing if the workflow is slow

Recommended additions:

- usage tracking
- export or send step
- audit log or trace view

## User Validation Expectations

Ask testers or domain contacts:

- did this reduce manual effort
- where did they still need to step in
- what output was missing or untrustworthy
- would they use it for real work

## Deliverables

By the end of this track, you should have:

- one workflow automation product demo
- sample input and output set
- before-vs-after workflow note
- user feedback notes
- case study with ROI explanation

## Common Mistakes To Avoid

- automating a workflow you do not understand clearly
- hiding execution state from the user
- skipping human review where consequences are meaningful
- optimizing prompt wording before fixing workflow design

## Expert Notes That Matter Here

### Workflow clarity is product clarity

If the process is fuzzy, the product will be fuzzy.

### Human review is often a feature, not a weakness

Especially for business workflows, controlled review points increase trust and usability.

### ROI stories make products credible

If you can clearly explain time saved or consistency improved, the product becomes much easier to defend.

## Final Standard For This Track

The correct outcome is not "I made an AI automation demo."

The correct outcome is:

"I built a workflow product with a clear before/after story, structured outputs, execution boundaries, and a believable value proposition."
