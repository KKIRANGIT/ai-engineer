# Weeks 33-35: Product B - AI Workflow or Outreach Product

Back to [Phase 4](../README.md)

## Goal

Build a workflow automation product that combines model output, tools, execution steps, and real task completion rather than only information delivery.

This track is where the product should start doing useful work on behalf of the user instead of only answering questions.

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

## What This Track Is Actually Training

This track is training six deeper skills:

1. decomposing a messy manual workflow into explicit steps
2. deciding where AI helps and where deterministic logic should stay in control
3. validating structured outputs before the workflow advances
4. adding review gates when side effects or risk matter
5. logging workflow state so failures can be debugged
6. connecting the build to a believable ROI story

The real outcome is not "I automated something." The real outcome is "I built a workflow product with a clear before-and-after value story and safe execution boundaries."

## Scope Boundary For This Track

This track focuses on:

- workflow decomposition
- structured output design
- deterministic tools
- approval and review boundaries
- workflow-state visibility
- ROI comparison

This track does not require:

- broad CRM integration breadth
- complex agent swarms
- dozens of automations
- production-grade third-party delivery infrastructure

The correct goal is a narrow workflow that feels believable, inspectable, and commercially meaningful.

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

## Best Source Strategy For This Track

Use sources in this order:

1. the local Product B workspace
2. your earlier tool-use, workflow, and eval notes from Phase 2
3. official docs for the exact workflow stack you choose

Do not treat this track like prompt iteration only. The product value lives in workflow shape and execution safety.

## Recommended Official References

Use these as the small companion stack:

- OpenAI structured outputs guide: <https://platform.openai.com/docs/guides/structured-outputs>
- OpenAI function calling guide: <https://platform.openai.com/docs/guides/function-calling>
- Anthropic tool use overview: <https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview>

These are enough to reinforce the workflow patterns without creating source overload.

## Execution Plan

### Week 33: Workflow analysis and decomposition

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

### Week 34: Build the workflow engine

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

### Week 35: Quality, ROI, and product story

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

## Hands-On Workspace Structure

```text
weeks-33-35-product-b-ai-workflow-or-outreach-product/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- week-33-workflow-analysis-and-decomposition/
|   |-- week-34-build-the-workflow-engine/
|   `-- week-35-quality-roi-and-product-story/
|-- notes/
|   |-- 01-track-plan.md
|   |-- 02-review-boundary-checklist.md
|   |-- 03-roi-framing-guide.md
|   `-- 04-case-study-outline.md
`-- projects/
    `-- lead-outreach-workflow-copilot/
```

## Exercises

The exercises are organized by week so the workflow product stays measurable and defensible.

You will practice:

- mapping the manual workflow and risk boundaries
- designing the structured outputs and validation checks
- comparing manual effort versus product-assisted effort

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [lead-outreach-workflow-copilot](projects/lead-outreach-workflow-copilot/README.md)

This project is a workflow product for lead research and outreach drafting. It teaches:

- workflow decomposition
- deterministic enrichment tools
- structured lead-brief outputs
- approval gating before outreach is sent
- audit logging and ROI comparison

It stays narrow on purpose so the value story remains easier to inspect than a larger generic automation platform.

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

## Exit Criteria

You are ready to move to Product C only if:

- the workflow has explicit states and review boundaries
- the product can complete a meaningful subset of the task
- the outputs are structured enough for downstream use
- you can point to one measurable time-saving or consistency gain
- you have recorded user or tester feedback

## Common Mistakes To Avoid

- automating a workflow you do not understand clearly
- hiding execution state from the user
- skipping human review where consequences are meaningful
- optimizing prompt wording before fixing workflow design
- pretending ROI exists without measuring a baseline

## Expert Notes That Matter Here

### Workflow clarity is product clarity

If the process is fuzzy, the product will be fuzzy.

### Human review is often a feature, not a weakness

Especially for business workflows, controlled review points increase trust and usability.

### ROI stories make products credible

If you can clearly explain time saved or consistency improved, the product becomes much easier to defend.

## Final Standard For This Track

The correct outcome is not:

"I made an AI automation demo."

The correct outcome is:

"I built a workflow product with a clear before/after story, structured outputs, execution boundaries, and a believable value proposition."
