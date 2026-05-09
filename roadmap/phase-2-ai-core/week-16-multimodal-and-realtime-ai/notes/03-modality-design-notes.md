# Modality Design Notes

Back to [Week 16 README](../README.md)

## Why This Note Exists

Many multimodal products are really combinations of smaller steps. The main design question is where the transitions should happen.

## Common Transition Patterns

### Audio -> Text -> Reasoning -> Text

Good when:

- you want inspection
- you want to store transcripts
- you want reuse with existing text systems

### Audio -> Realtime Speech Model -> Audio

Good when:

- conversational speed matters
- you want more natural turn-taking
- you are willing to manage event-driven sessions

### Image -> Structured Notes -> Reasoning

Good when:

- you want a clear extraction layer
- the downstream application expects typed fields

### Image + Text Together -> Reasoning

Good when:

- the user question depends on both the image and the surrounding context

## Week 16 Local Project Strategy

This workspace stays local and deterministic on purpose. It teaches:

- multimodal context fusion
- streaming chunks
- session events
- text-only vs multimodal differences

That gives you the mental model before a live provider API adds networking and model variability.
