# Eval Design Checklist

Back to [Week 15 README](../README.md)

Use this checklist whenever you design an eval for an AI task.

## Success Criteria

- What does "good" mean for this task?
- Which parts can be checked automatically?
- Which parts may need rubric-based review?

## Dataset

- Does the dataset reflect real input patterns?
- Does it include edge cases?
- Does it include previous failures?
- Are labels or expected outputs clearly defined?

## Grading

- Are the graders aligned with the real task?
- Are exact-match checks used only where appropriate?
- Are required fields and format constraints measured?
- Is case-level feedback understandable?

## Comparison Discipline

- Are versions compared on the same cases?
- Did you change one main variable at a time?
- Are regressions visible instead of hidden by one average score?

## Optimization Judgment

- Is the failure caused by prompt ambiguity?
- Is the failure caused by missing knowledge?
- Is the failure caused by weak tool or workflow design?
- Is fine-tuning being considered only after better diagnosis?
