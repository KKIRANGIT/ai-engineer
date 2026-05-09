# Course Agents

This folder contains reusable agent prompts for this repository.

## Available Agent

- [ai-engineer-course-agent.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/ai-engineer-course-agent.md)
- [workspace-prompt-guide.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/workspace-prompt-guide.md)

## What It Is For

The course agent is designed to help you study this repository as a full learning system rather than as disconnected files.

It should be used when you want help with:

- understanding the current week
- planning daily study sessions
- reviewing code and notes
- explaining concepts at the right level
- turning roadmap content into exercises or implementation steps
- deciding whether you are ready to move to the next week

## How To Use It

Give the agent these context files first:

1. [roadmap-master-reference.md](/d:/Tutorials/InterviewPraparation/ai-engineer/roadmap-master-reference.md)
2. the current week `README.md`
3. any related exercise or project files you are working on

Then ask for a specific mode, such as:

- teach this week to me step by step
- review my understanding before I move on
- explain this code like I am still a beginner
- create today's study plan from this week folder
- compare my Week 01 and Week 02 progress

If you want ready-made prompt templates, use:

- [workspace-prompt-guide.md](/d:/Tutorials/InterviewPraparation/ai-engineer/.agents/workspace-prompt-guide.md)

## Design Principle

The agent is intentionally phase-aware, source-aware, and repo-aware.

That means it should:

- follow the structure rules already established in this repository
- use official docs first for technical truth
- keep explanations clear without making them shallow
- avoid generic advice when local roadmap context exists
- keep related README files synchronized when repository content changes

## Documentation Sync Rule

When the course agent is used for repository improvement work, it should update the relevant documentation layers in the same task.

Examples:

- update a week folder -> update that week `README.md`
- add or restructure a phase asset -> update the phase `README.md`
- change roadmap navigation or status -> update `roadmap/README.md`
- change repository-level usage or structure -> update the root `README.md`
- change repository rules or maintenance expectations -> update `roadmap-master-reference.md`

This workspace should not drift into a state where source files and README files disagree.
