# Structured Output Checklist

Back to [Week 10](../README.md)

Use this checklist when reviewing a structured-output prompt or integration.

## Task Design

- Is the task specific?
- Does the prompt define what to do on ambiguity?
- Does the prompt avoid asking for too many distinct behaviors at once?

## Schema Design

- Are the fields truly needed by the application?
- Are enums explicit where they should be?
- Are required fields actually required?
- Is `additionalProperties` disabled when appropriate?

## Output Handling

- Can your code detect refusals?
- Can your code detect invalid values?
- Does your app know what to do when the model cannot classify confidently?

## Regression Quality

- Do you have easy cases?
- Do you have ambiguous cases?
- Do you have malformed or unsupported cases?
- Can you compare prompt variants on the same cases?
