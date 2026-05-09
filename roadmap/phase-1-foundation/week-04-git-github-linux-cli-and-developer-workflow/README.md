# Week 04: Git, GitHub, Linux CLI, and Developer Workflow

Back to [Phase 1](../README.md)

## Goal

Remove operational friction from your day-to-day engineering work so that tools stop slowing you down.

This week is not about becoming a DevOps expert. It is about becoming comfortable enough with Git, GitHub, the terminal, environment variables, and basic automation that you can move faster and with less fear.

## Why This Week Matters

A surprising amount of beginner frustration has nothing to do with programming logic. It comes from:

- fear of Git mistakes
- weak terminal fluency
- confusion around branches and pull requests
- broken local setup
- inconsistent project workflow

If you fix this early, the rest of the roadmap becomes more efficient.

## Week 04 Outcomes

By the end of this week, you should be able to:

- initialize and clone repositories confidently
- create and switch branches safely
- commit with useful messages
- understand merge vs rebase at a practical level
- open and merge your own pull requests
- navigate and inspect files from the terminal
- use environment variables and `.env` files safely
- run simple automated checks in CI

## What To Learn

## 1. Git Mental Model

Before commands, understand the model:

- working directory
- staging area
- commit history
- branches as pointers to commits

Many Git fears come from not knowing what state your repository is actually in.

Important idea:

Git is not random. It is a history and snapshot tool with explicit states.

## 2. Core Git Commands

Be comfortable with:

- `git init`
- `git clone`
- `git status`
- `git add`
- `git commit`
- `git log`
- `git diff`
- `git branch`
- `git switch`
- `git merge`
- `git rebase`

Expert beginner rule:

Run `git status` constantly. It is the fastest way to reduce confusion.

## 3. Branching and Pull Requests

You should understand:

- why feature branches exist
- how to isolate work
- how to push a branch
- how to open a pull request
- how code review fits into workflow

Even when working alone, using branches helps you practice professional habits.

## 4. Merge vs Rebase

You do not need advanced Git history surgery this week, but you should know:

- merge keeps branch history visible
- rebase rewrites your branch history onto a new base

Practical beginner guidance:

- understand both
- use them intentionally
- avoid reckless history rewriting until the model is clear

## 5. GitHub Workflow

Learn how GitHub supports collaboration:

- repositories
- issues
- pull requests
- branches
- Actions

You should be able to:

- push code
- create a PR
- review changed files
- merge after checks pass

## 6. Linux and Terminal Basics

The goal here is comfort, not memorization.

Be able to:

- navigate directories
- list files
- read files
- create directories
- move or rename files
- search for files or text
- understand relative vs absolute paths

Important concept:

The terminal is not just a backup interface. It is often the fastest interface for engineering work.

## 7. Environment Variables and `.env`

You need to understand:

- what environment variables are
- why secrets should not live directly in code
- what `.env.example` is for
- how configuration changes across environments

This becomes essential later for:

- API keys
- database URLs
- deployment config

## 8. SSH and Basic Access Concepts

You should know at a practical level:

- what SSH is for
- how an SSH key is used
- why GitHub SSH setup matters

You do not need deep network theory this week. You do need enough familiarity to avoid treating SSH as a black box.

## 9. Simple CI With GitHub Actions

This is your first step into automation.

Learn:

- what CI means
- why automated checks matter
- how to run a simple workflow on push or pull request

A basic workflow that runs tests is enough this week.

The important habit is:

- code should prove basic health automatically

## 10. Workflow Discipline

This week is really about habits.

Useful habits:

- branch before meaningful work
- commit in logical chunks
- write readable commit messages
- run tests before pushing
- keep README and setup instructions current

## Best Learning Sequence For This Week

Use this order:

1. Git states and basic commands
2. branches and pull requests
3. terminal file navigation
4. environment variables
5. SSH basics
6. simple GitHub Actions workflow
7. reusable project template

## Recommended Daily Breakdown

### Day 1: Git fundamentals

Focus:

- repo state
- staging
- commits
- diffs

Build:

- create a small repo and practice status/add/commit/log repeatedly

### Day 2: Branches and PR flow

Focus:

- feature branches
- pushing
- opening PRs

Build:

- create a branch for a small change and merge it through GitHub

### Day 3: Terminal fluency

Focus:

- file navigation
- directory structure
- reading and searching files

Build:

- perform one full project change mostly through the terminal

### Day 4: Env vars and project hygiene

Focus:

- `.env`
- `.gitignore`
- `.env.example`

Build:

- clean configuration setup in one repo

### Day 5: SSH and access workflow

Focus:

- GitHub authentication setup
- understanding SSH at a practical level

### Day 6: CI with GitHub Actions

Focus:

- run tests on push
- read workflow logs

Build:

- basic CI pipeline for one Python repo

### Day 7: Reusable project template

Focus:

- create a starter repo structure
- include common files and conventions

Build:

- template repo you can reuse for later weeks

## Build Plan

You should build three concrete things this week.

### 1. A clean Git practice workflow

This includes:

- repo setup
- meaningful commits
- one feature branch
- one merged PR

### 2. A terminal-based project maintenance habit

Demonstrate that you can:

- inspect files
- search code
- run tools
- manage project structure from the CLI

### 3. One minimal CI-enabled template repo

Include:

- README
- `.gitignore`
- `.env.example`
- test command
- GitHub Actions workflow

## Deliverables

By the end of this week, you should have:

- at least two repos with better Git hygiene than before
- one merged pull request on your own repo
- one basic GitHub Actions workflow that runs tests
- one reusable starter template repo
- one short note listing the Git and terminal commands you now use confidently

## Exit Criteria

You are ready to move on only if:

- Git no longer feels mysterious in everyday use
- you can branch, commit, push, and merge without panic
- you can navigate and inspect a project from the terminal
- you understand where environment variables fit into setup
- you can explain what your CI workflow is doing

## Common Mistakes To Avoid

- committing everything in one giant commit
- avoiding branches because they feel inconvenient
- pushing secrets into repositories
- using Git without checking `status`
- copying commands without understanding repository state
- treating CI as optional decoration

## Expert Notes That Matter Early

### Good workflow is leverage

Fast engineers are usually not only better coders. They are also better operators of their tools.

### Small automation pays off repeatedly

Even one simple CI check can prevent many avoidable mistakes.

### Clarity beats bravado in Git

The safe, understandable command is better than the clever command you only half understand.

## Suggested References

- Git official documentation
- GitHub docs
- shell basics references
- GitHub Actions documentation

## Final Standard For This Week

The correct outcome of Week 04 is not "I learned some Git commands."

The correct outcome is:

"I can work in a repository confidently, collaborate through GitHub workflows, manage local setup cleanly, and rely on a basic automated workflow."
