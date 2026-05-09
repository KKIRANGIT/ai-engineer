# Week 16: Multimodal and Realtime AI

Back to [Phase 2](../README.md)

## Goal

Move beyond text-only systems and understand the architecture, latency, and product tradeoffs behind voice, image, and low-latency interactive AI applications.

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

## Week 16 Outcomes

By the end of this week, you should be able to:

- explain the architecture of a voice or multimodal assistant
- compare speech-to-speech vs speech-to-text plus text-model plus text-to-speech pipelines
- build at least one image-understanding workflow
- understand what the Realtime API is for
- reason about latency and interaction quality
- build one small multimodal prototype

## What To Learn

## 1. Multimodal mental model

A multimodal application is not "the same app with more file types." Different modalities change:

- latency expectations
- UX expectations
- processing pipelines
- failure modes

You should think in terms of modality transitions:

- audio to text
- image to structured understanding
- text to speech
- audio and tool actions combined

## 2. Voice architecture choices

There are two major patterns to understand:

### Speech-to-speech

Useful when:

- low latency matters
- conversational naturalness matters

### Chained pipeline

Speech-to-text -> text model -> text-to-speech

Useful when:

- you want more control
- you already have a text agent
- latency is less strict

Current OpenAI guidance positions Realtime for low-latency voice agents and chained approaches as a reliable extension path from text-based systems.

## 3. Realtime APIs and sessions

Learn what realtime interaction changes:

- persistent session state
- streaming inputs and outputs
- event-driven conversation flow
- interruption handling

Important concept:

Realtime systems are as much about event design and UX flow as they are about model capability.

## 4. Speech-to-text and text-to-speech

You should know the strengths and tradeoffs of:

- transcription-focused pipelines
- speech generation pipelines
- low-latency vs more controlled voice responses

Think about:

- transcript quality
- speaker turns
- response delay
- user correction workflow

## 5. Vision and image understanding

You should understand:

- image input handling
- OCR-adjacent workflows
- document or screenshot analysis
- extracting structured information from images

Important rule:

Always ask whether the task is:

- open-ended image reasoning
- structured extraction
- image classification

The application design changes depending on which it is.

## 6. Streaming UX

Streaming is not just a technical feature. It changes how the product feels.

Learn to think about:

- partial text rendering
- progressive updates
- status indicators
- tool activity visibility
- graceful interruption

Good AI UX often depends on making latency legible.

## Best Learning Sequence For This Week

1. multimodal architecture concepts
2. voice pipeline choices
3. realtime concepts
4. image understanding
5. streaming UX
6. one multimodal prototype

## Recommended Daily Breakdown

### Day 1: Voice system architecture

Focus:

- chained vs realtime voice patterns

### Day 2: Audio input and transcription

Focus:

- speech-to-text
- transcript handling

### Day 3: Text-to-speech or speech response design

Focus:

- response path
- control vs naturalness tradeoffs

### Day 4: Image understanding

Focus:

- image input tasks
- structured extraction or Q&A

### Day 5: Realtime interaction patterns

Focus:

- sessions
- event handling
- latency expectations

### Day 6: Build prototype

Focus:

- combine at least one non-text modality with model reasoning

### Day 7: UX and latency review

Focus:

- document where delay occurs
- explain what would need improvement for production

## Build Plan

Choose one or two prototypes:

### Option A: Voice note summarizer

Flow:

- record or upload audio
- transcribe
- summarize
- optionally generate speech output

### Option B: Image Q&A or extraction tool

Flow:

- upload image or screenshot
- extract or analyze content
- answer questions or return structured fields

### Option C: Simple realtime interaction

Flow:

- stream audio or text
- receive incremental response
- expose session behavior clearly

## Deliverables

- one working multimodal prototype
- one architecture note
- one latency and UX tradeoff note

## Exit Criteria

- you can explain the moving parts of a voice or multimodal app
- you understand when Realtime is useful
- you can build at least one non-text model workflow
- you can discuss latency and UX as engineering concerns

## Common Mistakes To Avoid

- treating multimodal features as just alternate input fields
- ignoring latency until the end
- building voice flows with no plan for interruptions or delay
- conflating image reasoning with OCR-only tasks

## Expert Notes That Matter Early

### Modality changes architecture

Audio and image workflows are not just text workflows with wrappers.

### UX clarity matters more when latency is visible

Users tolerate delay better when they understand what is happening.

### Control vs naturalness is a design choice

Chained voice systems are often easier to control, while speech-to-speech systems often feel more natural.

## Suggested Official References

- OpenAI Realtime overview
- OpenAI audio and speech guide
- OpenAI images and vision guide

## Final Standard For This Week

The correct outcome of Week 16 is not "I tried voice and images."

The correct outcome is:

"I understand the architecture and tradeoffs of multimodal and realtime AI well enough to build and reason about non-text product experiences."
