# Entity Mapping Exercise

## What This Exercise Trains

- identifying entities
- identifying relationships
- turning a problem domain into tables

## Practice Scenario

Imagine a small project tracker application where:

- users create projects
- each project has tasks
- tasks can have multiple tags
- a task belongs to exactly one project
- one tag can be used on many tasks

## Your Job

Write down:

1. the tables you need
2. the likely columns in each table
3. the primary key of each table
4. the foreign keys you need
5. where a join table is required

## Success Check

You should be able to explain:

- why `task_tags` should exist instead of storing multiple tags in one text column
- why `project_id` belongs on `tasks`
- why each table represents one kind of fact
