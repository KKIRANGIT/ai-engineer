# Week 04: Git, GitHub, Linux CLI, and Developer Workflow

Back to [Phase 1](../README.md)

## Goal

Remove operational friction from your day-to-day engineering work so that tools stop slowing you down.

This week is not about becoming a DevOps expert. It is about becoming comfortable enough with Git, GitHub, the terminal, environment variables, and basic automation that you can move faster and with less fear.

By the end of this week, you should be able to:

- initialize and inspect repositories confidently
- create and switch branches safely
- commit in smaller, meaningful units
- explain merge vs rebase at a practical level
- open and merge your own pull requests
- navigate and inspect projects from the terminal
- use `.gitignore`, `.env`, and `.env.example` correctly
- understand a small GitHub Actions workflow

Week 04 is where engineering workflow starts becoming a repeatable system rather than a source of anxiety.

## What This Week Is Actually Training

At surface level, Week 04 looks like "learn Git commands and some shell basics."

The real training target is deeper:

- understanding repository state before making changes
- building a habit of checking what changed and why
- reducing fear around branch-based work
- learning to use the terminal as a fast working interface
- treating setup, config, and automation as part of engineering quality

That is why this week matters so much. Strong engineers are not only better coders. They also operate their tools more cleanly.

## Scope Boundaries

Study deeply this week:

- Git state model
- common Git commands
- staging and commit discipline
- branch-based workflow
- pull request flow
- terminal navigation and file inspection
- `.gitignore`, `.env`, `.env.example`
- SSH at a practical level
- basic CI workflow structure

Do not go deep on these yet:

- advanced Git internals
- dangerous history rewriting
- complex shell scripting
- advanced CI/CD pipelines
- container deployment automation
- release engineering tooling

The goal is confidence and consistency, not tool maximalism.

## Week 04 Outcomes

You are successful this week if you can do most of the following with confidence:

- explain the difference between working tree, staging area, and commit history
- use `git status`, `git diff`, `git add`, and `git commit` intentionally
- create a feature branch and describe why it exists
- navigate a project from the terminal without relying entirely on the editor UI
- explain why `.env.example` and `.gitignore` matter
- read a simple GitHub Actions workflow and explain what it runs
- use one reusable starter project as a clean template for future weeks

## How Week 04 Builds On Week 03

Week 03 made you work with systems outside your code through HTTP and APIs.

Week 04 makes you work more professionally around your codebase:

- with Git
- with GitHub
- with the terminal
- with setup and automation

That means Week 04 is not a side topic. It is the operational layer around everything you build later.

## Core Workflow Concepts To Master

## 1. Git Mental Model

Before commands, understand the state model:

- working directory
- staging area
- commit history
- branches as movable references to commits

Many beginner Git mistakes are not command mistakes. They are state-model mistakes.

Important rule:

If you do not know the current repository state, stop and run `git status`.

## 2. Core Git Commands

You should become comfortable with:

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

Clarity matters more than command count. A few commands used well are better than many commands used mechanically.

## 3. Branches and Pull Requests

You need to understand:

- why feature branches exist
- how to isolate work
- why pull requests improve review and safety
- how a branch becomes a PR
- how a PR becomes a merge

Even when working alone, branches build professional workflow habits.

## 4. Merge vs Rebase

You do not need advanced history surgery this week, but you should know:

- merge preserves branch history as-is
- rebase rewrites your branch's commits onto a new base

Safe beginner guidance:

- understand both
- use them intentionally
- do not rewrite shared history casually

## 5. Terminal Navigation and Inspection

You should be able to:

- list files
- move between directories
- inspect file contents
- create folders
- search for files
- search inside files
- understand relative vs absolute paths

The terminal is often the fastest interface for understanding a codebase.

## 6. Environment Variables and Config Hygiene

You should understand:

- what environment variables are
- what belongs in code vs config
- why `.env.example` documents expected settings
- why `.gitignore` prevents accidental commits of generated or secret files

This becomes critical later for API keys, databases, and deployments.

## 7. SSH and Authentication Thinking

You should understand at a practical level:

- what SSH is for
- how SSH keys support authentication
- why GitHub SSH setup exists
- that HTTPS + token auth is also common

You do not need deep protocol theory. You do need enough understanding to avoid treating authentication setup as magic.

## 8. Continuous Integration Basics

This is your first light introduction to automation.

You should understand:

- what CI means
- what a workflow trigger is
- what a job is
- what a step is
- why tests should run automatically on push or pull request

This week only requires a very small workflow. The important habit is:

- code health should not depend only on memory

## Best Learning Sequence For This Week

Use this order:

1. Git state model
2. core Git commands
3. branches and pull requests
4. terminal navigation and search
5. `.gitignore` and `.env` patterns
6. SSH and remote workflow concepts
7. GitHub Actions workflow reading
8. starter template review

## A No-Doubt Execution Plan For The Week

### Day 1: Git state and basic commands

Study:

- working tree
- staging area
- commits
- diffs

Practice:

- run the Git basics exercise
- inspect the practice sandbox

Checkpoint:

- can you explain what `git status` is telling you

### Day 2: Branches and pull requests

Study:

- branches
- switching
- feature workflow
- PR purpose

Practice:

- run the branching exercise
- simulate a branch-based change in the sandbox project

Checkpoint:

- can you explain why feature branches make work safer

### Day 3: Terminal fluency

Study:

- navigation
- search
- file inspection
- path thinking

Practice:

- run the CLI navigation exercise
- inspect the starter template mostly from the terminal

Checkpoint:

- can you inspect a project structure quickly without depending on the file explorer

### Day 4: Config and environment hygiene

Study:

- `.gitignore`
- `.env`
- `.env.example`

Practice:

- run the env/config exercise
- inspect both project folders for config hygiene

Checkpoint:

- can you explain what should never be committed

### Day 5: SSH and GitHub workflow concepts

Study:

- authentication options
- GitHub remote workflow
- clone / push / PR concepts

Practice:

- review the notes and prompts
- map local Git steps to GitHub actions

Checkpoint:

- can you describe the difference between local branch work and remote collaboration

### Day 6: GitHub Actions basics

Study:

- workflow triggers
- jobs
- steps
- CI health checks

Practice:

- inspect the starter template workflow
- run the local test command it mirrors

Checkpoint:

- can you explain what the workflow is doing line by line

### Day 7: Workflow synthesis

Build:

- use the practice sandbox for Git habits
- use the starter template as a reusable repo baseline
- review notes and command references

Checkpoint:

- can you explain how this week reduces engineering friction later

## Week 04 Workspace Standard

This week now includes a real hands-on workflow workspace.

Actual structure:

```text
week-04-git-github-linux-cli-and-developer-workflow/
|-- exercises/
|   |-- git-basics/
|   |-- branching-and-prs/
|   |-- cli-navigation/
|   |-- env-and-config/
|   |-- ci-reading/
|   `-- README.md
|-- projects/
|   |-- git-practice-sandbox/
|   `-- python-starter-template/
|       |-- .github/workflows/
|       |-- app/
|       |-- tests/
|       |-- scripts/
|       |-- .env.example
|       |-- .gitignore
|       `-- README.md
|-- notes/
`-- README.md
```

## Main Build Goals

This week has two build layers.

### Layer 1: Git and terminal practice sandbox

You need a local folder where you can safely practice:

- status
- add
- commit
- branch
- rename
- diff
- ignore patterns

That is what the `git-practice-sandbox/` project is for.

### Layer 2: Reusable starter repository

You also need one cleaner example of what a small professional project skeleton looks like.

That is what the `python-starter-template/` project is for.

It includes:

- project structure
- README
- `.gitignore`
- `.env.example`
- tests
- a local checks script
- a GitHub Actions workflow

## Deliverables

By the end of the week, you should have:

- completed the local command and workflow exercises
- practiced a branch-based workflow in the sandbox
- understood the starter template structure
- read the GitHub Actions workflow and matched it to the local test command
- written a short note about which Git and terminal commands now feel routine

## Best Sources For Week 04

Use sources in this order.

### Tier 1: Official Git Sources

1. Git documentation
   Link: https://git-scm.com/docs/git

2. Git tutorial
   Link: https://git-scm.com/docs/gittutorial

3. Git everyday workflow
   Link: https://git-scm.com/docs/giteveryday

4. Git branching
   Link: https://git-scm.com/docs/git-branch

5. Git switch
   Link: https://git-scm.com/docs/git-switch

6. Git rebase
   Link: https://git-scm.com/docs/git-rebase

### Tier 2: Official GitHub Sources

1. Cloning a repository
   Link: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

2. About pull requests
   Link: https://docs.github.com/articles/using-pull-requests?lang=en

3. Creating a pull request
   Link: https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=cli

4. Ignoring files
   Link: https://docs.github.com/ignore-files

5. Understanding GitHub Actions
   Link: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

6. Quickstart for GitHub Actions
   Link: https://docs.github.com/en/actions/writing-workflows/quickstart

### Tier 3: Shell and Command-Line Reference

1. GNU Coreutils manual
   Link: https://www.gnu.org/software/coreutils/manual/coreutils.html

Use it selectively for:

- `ls`
- `cp`
- `mv`
- `mkdir`

Important note:

Because you are on Windows, you may often use PowerShell equivalents in practice. The mental model still transfers:

- list files
- move files
- inspect paths
- search content

## Source Strategy That Avoids Confusion

For Week 04, use this source stack:

1. official Git docs
2. official GitHub docs
3. local practice exercises
4. the sandbox and starter template projects

That is enough.

## Exact Study Path Through The Sources

If you want the least ambiguity, use this sequence:

1. read the Git tutorial and mental-model sections
2. do the Git basics exercise
3. read the pull request and branch docs
4. do the branching exercise
5. read the ignore-files and GitHub Actions docs
6. inspect the starter template
7. run the local tests and local checks script
8. review the notes and workflow checklist

## Exit Criteria

You are ready for Week 05 only if most of these are true:

- Git no longer feels mysterious in everyday use
- you can branch, commit, and merge without panic
- you can navigate and inspect a project from the terminal
- you understand where environment variables and ignore rules fit
- you can read a basic CI workflow and explain what it runs
- you can describe what a clean starter repo should include

If these are not true, repeat the sandbox practice before moving on.

## Common Mistakes That Create Confusion Later

- committing everything in one giant commit
- avoiding branches because they feel inconvenient
- pushing secrets into repositories
- using Git without checking `status`
- copying commands without understanding repository state
- treating CI as optional decoration

## Expert Notes

### Good workflow is leverage

Fast engineers are usually not only better coders. They are also better operators of their tools.

### Small automation pays off repeatedly

Even one simple CI check can prevent many avoidable mistakes.

### Clarity beats bravado in Git

The safe, understandable command is better than the clever command you only half understand.

## How Week 04 Connects To Week 05

Week 05 moves into SQL, Postgres, and data modeling.

That week becomes easier if Week 04 is strong because database work usually involves:

- setup discipline
- terminal work
- project structure
- version-controlled schema or code changes
- environment-variable-based configuration

Workflow skill compounds into every later technical week.

## Final Standard For This Week

The correct outcome is not:

"I learned some Git commands."

The correct outcome is:

"I can work in a repository confidently, navigate my project from the terminal, manage setup cleanly, collaborate through GitHub workflows, and understand a small automated CI pipeline."
