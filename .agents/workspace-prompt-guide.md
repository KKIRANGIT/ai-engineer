# Workspace Prompt Guide

This file is the practical prompt guide for using AI agents inside this `ai-engineer` workspace.

Use it when you want:

- a reliable prompt structure
- the right context files in the right order
- example prompts for learning, coding, review, and repository updates
- a consistent way to use [.agents/ai-engineer-course-agent.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/ai-engineer-course-agent.md)

This guide is designed to reduce prompt ambiguity and keep the agent aligned with the repository rules.

## Core Principle

Do not prompt the agent like it is working in a blank environment.

This workspace already has:

- a repository structure
- a master reference
- phase and week modules
- agent rules
- documentation sync requirements

The best prompts explicitly tell the agent to use that context.

## Mandatory Context Files

For most serious tasks, provide these in this order:

1. [roadmap-master-reference.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap-master-reference.md)
2. [.agents/ai-engineer-course-agent.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/ai-engineer-course-agent.md)
3. the relevant phase `README.md`
4. the relevant week `README.md`
5. the local exercise, project, or notes files you are working on

Short version:

- master reference for rules
- course agent for behavior
- week files for actual task context

## Best Default Prompt Pattern

Use this pattern for most work:

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `[target file or folder]` as the active workspace context.

Goal:
[what you want done]

Requirements:
- stay aligned with the repository structure
- keep documentation synchronized if files or structure change
- optimize for [beginner clarity / implementation depth / interview prep / production realism]
```

This is the most reusable general pattern.

## Prompt Templates By Use Case

## 1. Learn a Week

Use when you want the agent to teach a weekly module.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/README.md` as the active week context.

Teach this week to me step by step.

Requirements:
- use the local week material first
- explain concepts in beginner-friendly language
- tie each topic to why it matters later
- give me a clear day-by-day plan
```

## 2. Build a Week Workspace

Use when you want to turn a planning week into exercises, code, and notes.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `roadmap/phase-1-foundation/week-03-http-apis-and-integration-thinking/` as the active workspace context.

Expand this week into a full hands-on workspace like Week 01 and Week 02.

Requirements:
- create exercises, projects, and notes where appropriate
- keep the code beginner-readable but engineering-correct
- add clear comments only where they clarify intent
- update the relevant README files so the workspace stays in sync
```

## 3. Explain Code

Use when you want the agent to explain local source files.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `roadmap/phase-1-foundation/week-02-python-engineering-basics/projects/refactored-todo-app/todo_app/` as the active code context.

Explain this codebase to me like I am still learning.

Requirements:
- explain file responsibilities
- explain how the data moves through the system
- explain why the code is organized this way
- point out the key engineering lessons in this project
```

## 4. Review Readiness

Use when you want to know if you are ready to move forward.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `roadmap/phase-1-foundation/week-02-python-engineering-basics/README.md` as the active week context.

Review whether I am actually ready to move from this week to the next one.

Requirements:
- evaluate me using the exit criteria
- do not give false confidence
- identify the weakest missing capabilities
- tell me exactly what I should repeat before moving forward
```

## 5. Debug a Problem

Use when you are blocked by an error or failing behavior.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `roadmap/phase-1-foundation/week-01-python-core-and-problem-solving/projects/cli-todo-app/app.py` and related files as the active context.

Help me debug this problem.

Problem:
[paste the error or describe the failure]

Requirements:
- explain the root cause clearly
- show the debugging path, not only the fix
- relate the bug to the underlying concept I need to understand
```

## 6. Update Repository Content

Use when you want the agent to improve or change this repository.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `[target folder or file]` as the active workspace context.

Update this repository section.

Goal:
[what should change]

Requirements:
- preserve the existing structure unless there is a clear improvement path
- keep all related README files synchronized
- update the relevant phase, week, roadmap, or root docs if needed
- do not leave the workspace in a partially documented state
```

## 7. Create a Daily Study Plan

Use when you want a focused plan for one day.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `[current week folder]` as the active workspace context.

Create today's study plan for me.

Requirements:
- tell me exactly what to read
- tell me exactly what to code
- tell me exactly what to verify
- define what "done for today" means
```

## 8. Compare Two Weeks or Two Projects

Use when you want structured comparison.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use both relevant week folders as active context.

Compare Week 01 and Week 02 from an engineering-learning perspective.

Requirements:
- explain what improved structurally
- explain what new engineering habits Week 02 adds
- explain what I should notice before I move on
```

## 9. Strengthen Documentation

Use when the main goal is improving README quality or keeping sections aligned.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `[target folder]` as the active workspace context.

Review this section for documentation drift and fix it.

Requirements:
- compare the actual files to the README descriptions
- update any stale documentation
- preserve the repository's documentation sync rules
```

## 10. Interview-Oriented Review

Use when you want the agent to reinterpret a week from an interview-prep angle.

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Then use `[target week or phase]` as the active workspace context.

Review this material from an interview-preparation perspective.

Requirements:
- identify the concepts I should be able to explain aloud
- identify the code I should be able to walk through
- identify the likely interview questions that connect to this week
```

## Recommended Prompt Add-Ons

You can append one of these lines depending on your goal.

For deeper teaching:

```text
Assume I am still early in learning and avoid skipping reasoning steps.
```

For implementation depth:

```text
Default to actually creating or updating the files instead of only describing what should be done.
```

For strict review:

```text
Be strict. Do not mark this as complete if the exit criteria are not truly met.
```

For documentation sync:

```text
If you change code, folders, or structure, update the related README files in the same task.
```

For source quality:

```text
Prefer official documentation and repository-local material over generic tutorials.
```

## Context Selection Guide

Use the smallest useful context, not the entire repository every time.

### For week-specific help

Include:

- `roadmap-master-reference.md`
- `.agents/ai-engineer-course-agent.md`
- the week folder or week `README.md`

### For phase-level planning

Include:

- `roadmap-master-reference.md`
- `.agents/ai-engineer-course-agent.md`
- the phase `README.md`
- any relevant week folders

### For repo-wide maintenance

Include:

- `roadmap-master-reference.md`
- `.agents/ai-engineer-course-agent.md`
- `README.md`
- `roadmap/README.md`
- the affected phase or week docs

## What To Avoid In Prompts

Avoid vague prompts like:

- help me with Python
- improve this
- explain everything
- make this better

These force the agent to guess too much.

Instead, specify:

- the target folder or file
- the goal
- the expected output
- the quality standard

## Best One-Line Prompt Starters

These are fast starters you can reuse:

- `Use roadmap-master-reference.md and .agents/ai-engineer-course-agent.md as context, then...`
- `Review this week against the repository standards and...`
- `Expand this folder into a full hands-on workspace and keep the README files synchronized.`
- `Explain this code using the local project structure, not generic Python advice.`
- `Audit this section for documentation drift and fix any mismatch.`

## Best Reference Chain For This Workspace

If you want the shortest reliable reference chain, use this order:

1. [roadmap-master-reference.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap-master-reference.md)
2. [.agents/ai-engineer-course-agent.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/ai-engineer-course-agent.md)
3. [README.md](/d:/Tutorials/InterviewPraparation/ai-engineer/README.md)
4. [roadmap/README.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap/README.md)
5. the relevant phase or week files

## Best Default Master Prompt

If you want one general-purpose prompt to keep reusing, use this:

```text
Use `roadmap-master-reference.md` and `.agents/ai-engineer-course-agent.md` as context.
Use the relevant local week, phase, or project files as the active workspace context.

Help me using the actual structure and standards of this repository, not generic advice.

Requirements:
- stay aligned with the repository structure
- prefer official references and local material
- keep explanations clear and technically correct
- if you change files or structure, update the related README files too
- do not consider the task complete if the workspace is left out of sync
```

## Final Note

This workspace works best when prompts are:

- context-aware
- target-specific
- structure-aware
- sync-aware

If you use this guide consistently, the agent will behave much more like a real course assistant embedded in this repository and much less like a generic AI chat tool.
