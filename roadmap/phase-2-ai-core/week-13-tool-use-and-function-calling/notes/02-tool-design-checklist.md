# Tool Design Checklist

Back to [Week 13 README](../README.md)

Use this checklist whenever you create a tool for a model-enabled application.

## Tool Purpose

- Does the tool solve one clear job?
- Is the tool actually needed, or would normal application logic be simpler?
- Does the tool return information or perform an action?

## Tool Description

- Does the description explain what the tool does?
- Does it explain when the tool should be used?
- Does it explain when the tool should not be used?
- Does it describe important limits and failure conditions?

## Parameters

- Are required fields truly required?
- Are field names obvious?
- Are units explicit for numeric inputs?
- Are ambiguous free-form fields minimized?

## Safety

- What validation happens before execution?
- What should happen if a field is missing or malformed?
- Are there domain limits, thresholds, or access boundaries?
- Is there any action that should require human review?

## Traceability

- Will the system log tool selection?
- Will it log the requested arguments?
- Will it log whether validation succeeded?
- Will it log what output or error came back?

## Design Warning Signs

- one tool tries to do many unrelated things
- description is only one vague sentence
- required fields are unclear
- output format is inconsistent
- no trace exists for failures
