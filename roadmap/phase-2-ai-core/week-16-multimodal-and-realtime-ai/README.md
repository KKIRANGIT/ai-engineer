# Week 16: Multimodal and Realtime AI

Back to [Phase 2](../README.md)

## Goal

Move beyond text-only systems and understand the architecture, latency, and product tradeoffs behind voice, image, and low-latency interactive AI applications.

This week is where you stop thinking only in prompts and start thinking in modalities, session events, and user-perceived delay.

## Why This Week Matters

Modern AI products increasingly combine:

- text
- images
- audio
- streaming interactions

If you only think in text prompts and text outputs, you will miss a major part of current application design.

This week matters because multimodal systems expose new engineering questions:

- what should be transcribed vs directly reasoned over
- how much latency is acceptable
- where should speech, text, and tools connect
- how should streaming responses shape the UX
- what changes when you have persistent session state

## What This Week Is Actually Training

Week 16 is training five deeper skills:

1. reasoning about modality transitions instead of only text prompts
2. understanding chained pipelines versus low-latency realtime flows
3. handling streaming outputs and partial updates
4. comparing text-only and multimodal context quality
5. thinking about latency and UX as part of system design

The real outcome is not "I tried an image input once." The real outcome is "I can design a multimodal interaction path deliberately."

## Scope Boundary For This Week

This week focuses on:

- multimodal architecture
- audio and voice pipelines
- image-understanding workflows
- realtime sessions and event flows
- streaming UX
- one local multimodal prototype

This week does not require:

- live WebRTC integration
- actual speech synthesis
- production voice infrastructure
- real mobile capture flows

The correct first goal is not "ship a full voice assistant." The correct first goal is "understand the moving parts and simulate them clearly."

## Week 16 Outcomes

By the end of this week, you should be able to:

- explain the architecture of a voice or multimodal assistant
- compare speech-to-speech vs speech-to-text plus text-model plus text-to-speech pipelines
- build at least one image-understanding workflow
- explain what the Realtime API is for
- reason about latency and interaction quality
- build one small multimodal prototype with streaming-style behavior

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 16 workspace
2. official provider docs for realtime, vision, and audio
3. your own event traces and architecture notes

Do not treat multimodal and realtime as feature checkboxes. Use this week to think structurally.

## Recommended Official References

Primary sources:

- OpenAI Realtime overview: <https://platform.openai.com/docs/guides/realtime/overview>
- OpenAI Responses input items reference: <https://platform.openai.com/docs/api-reference/responses/input-items>
- OpenAI Images and vision guide: <https://platform.openai.com/docs/guides/images?api-mode=responses>
- Anthropic Vision guide: <https://docs.anthropic.com/en/docs/build-with-claude/vision>

These references were chosen because multimodal and realtime guidance is highly time-sensitive and the event models have changed recently.

## Core Mental Models

## 1. Multimodal is not just "more file types"

A multimodal application is not the same app with more inputs attached.

Different modalities change:

- latency expectations
- UX expectations
- processing pipelines
- failure modes
- session design

You should think in modality transitions:

- audio to text
- image to structured understanding
- text to speech
- audio plus image plus tools combined

## 2. Voice architecture has real tradeoffs

There are two major patterns to understand:

### Speech-to-speech

Useful when:

- low latency matters
- conversational naturalness matters
- interruption handling is important

### Chained pipeline

Speech-to-text -> text model -> text-to-speech

Useful when:

- you want more control
- you already have a text-based system
- latency is less strict
- you want more inspectable intermediate states

Current OpenAI guidance positions Realtime for low-latency voice agents and chained pipelines as a practical extension path from text-based systems.

## 3. Realtime changes interaction design

Realtime interaction introduces:

- persistent session state
- event-driven inputs and outputs
- interruptions
- partial updates
- tool calls during ongoing interaction

Important concept:

Realtime systems are as much about event design and user experience as they are about model capability.

## 4. Vision tasks are not all the same

Image understanding can mean very different application shapes:

- open-ended visual reasoning
- structured extraction
- screenshot understanding
- document or receipt interpretation
- image classification

The right prompt, output contract, and evaluation method change depending on which kind of task you are solving.

## 5. Streaming UX is part of the product

Streaming is not just a transport detail. It changes how the product feels.

You should think about:

- partial rendering
- progress messages
- status indicators
- visible tool activity
- graceful interruption

Good AI UX often depends on making latency legible instead of hiding it badly.

## Best Learning Sequence For This Week

1. multimodal architecture concepts
2. voice pipeline choices
3. realtime session concepts
4. image understanding workflows
5. streaming UX
6. one multimodal prototype

## Recommended Daily Breakdown

### Day 1: Multimodal architecture

Focus:

- modality transitions
- text-only vs multimodal reasoning

### Day 2: Voice and audio pipelines

Focus:

- speech-to-speech vs chained pipelines
- where transcription helps and where it adds latency

### Day 3: Vision workflows

Focus:

- image understanding task types
- extraction vs open reasoning

### Day 4: Realtime sessions

Focus:

- event flow
- session state
- interruption points

### Day 5: Streaming UX

Focus:

- partial responses
- progress indicators
- making delay visible

### Day 6: Build prototype

Focus:

- combine non-text context with a streaming output path

### Day 7: Latency and architecture review

Focus:

- document where delay occurs
- explain what would need improvement for production

## Hands-On Workspace Structure

```text
week-16-multimodal-and-realtime-ai/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- multimodal-mental-model/
|   |-- streaming-and-sessions/
|   |-- vision-workflows/
|   `-- voice-and-audio-pipelines/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-latency-checklist.md
|   `-- 03-modality-design-notes.md
`-- projects/
    `-- incident-assistant-multimodal-lab/
```

## Exercises

The exercises isolate the main multimodal and realtime concepts before the larger project combines them.

You will practice:

- thinking in modality transitions
- comparing chained and realtime-style voice architectures
- distinguishing vision task types
- reasoning about streaming updates and session events

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [incident-assistant-multimodal-lab](projects/incident-assistant-multimodal-lab/README.md)

This project is a local multimodal incident assistant that:

- compares text-only vs multimodal context
- combines text reports, transcript snippets, and image observations
- emits streaming-style response chunks
- records a session event trace

It stays local and deterministic on purpose so the architecture remains easy to inspect.

## Build Plan

Build and study one multimodal prototype that can:

- read an incident case with text and optional non-text observations
- compare text-only and multimodal reasoning quality
- simulate a realtime-style session with visible events
- stream a partial response instead of only returning one final block

Required qualities:

- readable local dataset
- explicit session events
- streaming output path
- text-only vs multimodal comparison
- architecture and latency notes

## Suggested Study Order Inside This Week

1. read this README fully
2. complete the exercises
3. read the project README
4. run a text-only case
5. run the same case in multimodal mode
6. run the streaming session mode
7. inspect the trace and notes

## Deliverables

By the end of Week 16, you should have:

- completed the exercises
- run a multimodal prototype
- compared text-only and multimodal outputs
- inspected the session trace
- written your own note on latency and UX tradeoffs

## Exit Criteria

You should not leave Week 16 until you can:

- explain the moving parts of a voice or multimodal app
- explain when chained audio pipelines are preferable
- explain when a realtime architecture is useful
- distinguish text-only and multimodal context quality
- discuss latency and UX as engineering concerns

## Common Mistakes To Avoid

- treating multimodal features as just alternate input fields
- ignoring latency until the end
- building voice flows with no plan for interruptions or delay
- conflating image reasoning with OCR-only tasks
- hiding streaming state so the user cannot tell what is happening

## Expert Notes That Matter Early

### Modality changes architecture

Audio and image workflows are not just text workflows with wrappers.

### UX clarity matters more when latency is visible

Users tolerate delay better when they understand what is happening.

### Control vs naturalness is a design choice

Chained voice systems are often easier to control, while speech-to-speech systems often feel more natural.

### Session design is a product decision

The event model is part of the user experience, not only backend plumbing.

## Final Standard For This Week

The correct outcome of Week 16 is not:

"I tried voice and images."

The correct outcome is:

"I understand the architecture and tradeoffs of multimodal and realtime AI well enough to build and reason about non-text product experiences."
