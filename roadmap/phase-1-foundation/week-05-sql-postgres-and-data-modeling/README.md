# Week 05: SQL, Postgres, and Data Modeling

Back to [Phase 1](../README.md)

## Goal

Understand relational data properly so you can design systems intentionally instead of treating the database as a storage box you poke at randomly.

This week is about learning how applications represent structure, relationships, and constraints in data.

## Why This Week Matters

Many beginner apps fail structurally because the database design is weak.

Common symptoms:

- duplicated data everywhere
- confusing table shapes
- inconsistent updates
- hard-to-write queries
- fragile assumptions in code

Good data modeling improves:

- application correctness
- query clarity
- backend design
- future scalability

It also becomes essential later for:

- auth and user data
- billing state
- AI usage tracking
- document metadata
- analytics events

## Week 05 Outcomes

By the end of this week, you should be able to:

- explain what tables, rows, columns, and relationships represent
- design a schema for a small application
- use `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, and `JOIN`
- understand primary keys and foreign keys
- distinguish one-to-one, one-to-many, and many-to-many relationships
- write SQL that is readable and purposeful
- build a CRUD backend against Postgres or Supabase

## What To Learn

## 1. Relational Thinking

You are not storing "screens" or "features" in a database. You are storing entities and relationships.

You should think in terms of:

- what things exist
- what facts are stored about them
- how they relate to each other
- what constraints must always stay true

Example:

- users
- tasks
- organizations
- invoices
- documents

Each of these usually becomes a table or part of a table design.

## 2. Table Design Basics

You should understand:

- what a table represents
- what a row represents
- what a column represents
- what makes a good column name
- what data type fits which field

Expert beginner rule:

Design for meaning first, then for convenience.

## 3. Keys and Relationships

Learn:

- primary keys
- foreign keys
- one-to-one relationships
- one-to-many relationships
- many-to-many relationships with join tables

Important idea:

Relationships are the real power of relational systems. If you do not model them well, the rest of the system becomes messy.

## 4. Normalization and Practical Simplicity

You should understand the goal of normalization:

- reduce duplication
- reduce update inconsistency
- make structure more reliable

But also learn practical balance:

- not every beginner app needs perfect theoretical normalization
- clarity and correctness matter most

Good early question:

- if this value changes, how many places would I need to update it

If the answer is "too many," your structure may be too duplicated.

## 5. Core Querying

You need strong comfort with:

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`
- `GROUP BY`
- aggregate functions like `COUNT`, `SUM`, `AVG`
- `JOIN`

Expert beginner rule:

Do not only practice syntax. Always know what question the query is answering.

## 6. Joins

This is one of the most important parts of the week.

You should understand:

- inner join
- left join
- what rows appear and why
- how foreign keys relate to joins

If joins feel confusing, slow down and use small sample tables until the logic becomes obvious.

## 7. Constraints and Data Integrity

Learn why the database should enforce some truth, not just your application code.

Important constraints:

- primary key
- foreign key
- `NOT NULL`
- `UNIQUE`
- defaults

Why this matters:

- application bugs happen
- database constraints provide a second layer of protection

## 8. Indexing Basics

You do not need deep database optimization this week, but you should understand:

- what an index is
- why indexes help reads
- why they have a cost
- why not every column needs one

Important early intuition:

- indexes are about tradeoffs, not magic speed

## 9. Transactions and Consistency

At a concept level, learn:

- some operations should succeed or fail together
- partial writes can create bad state
- transactions help preserve consistency

Even if you do not build complex transactions yet, the concept matters.

## 10. Postgres and Supabase Workflow

You should get comfortable with:

- creating tables
- inserting rows
- updating rows
- deleting rows
- running queries manually

Supabase is useful because it gives you fast access to hosted Postgres and later integrates well with product work.

## Best Learning Sequence For This Week

Use this order:

1. relational thinking
2. tables and keys
3. relationships
4. core queries
5. joins
6. constraints
7. indexing basics
8. CRUD integration

## Recommended Daily Breakdown

### Day 1: Data modeling concepts

Focus:

- entities
- columns
- keys
- relationships

Build:

- sketch a schema for a small app on paper or in Markdown

### Day 2: Basic SQL queries

Focus:

- `SELECT`
- filtering
- ordering
- aggregates

Build:

- solve 10-15 query exercises

### Day 3: Joins and relationships

Focus:

- foreign keys
- join logic

Build:

- use two or three related tables and write joins against them

### Day 4: Constraints and schema cleanup

Focus:

- `NOT NULL`
- `UNIQUE`
- defaults

Build:

- improve your schema with explicit constraints

### Day 5: Postgres or Supabase practice

Focus:

- real table creation
- insert/update/delete

Build:

- create the full schema in a running database

### Day 6: CRUD backend integration

Focus:

- backend reads and writes
- mapping API actions to database operations

Build:

- simple CRUD backend for one resource

### Day 7: Review and schema justification

Focus:

- explain your schema
- explain your joins
- document tradeoffs

## Build Plan

This week should produce three things.

### 1. SQL exercise set

Solve 25-30 exercises across:

- filtering
- sorting
- aggregation
- joins
- updates
- inserts

### 2. Schema design for a real app

Pick one small product idea and model:

- users
- core resource tables
- relationships
- constraints

### 3. CRUD backend integration

Build one simple backend or script layer that:

- creates data
- reads data
- updates data
- deletes data

## Deliverables

By the end of this week, you should have:

- a folder of SQL queries or exercises
- a schema diagram or schema note
- SQL table creation scripts
- a small CRUD demo using Postgres or Supabase
- a short explanation of why your schema is shaped the way it is

## Exit Criteria

You are ready to move on only if:

- you can model a small app in tables with confidence
- you understand primary and foreign keys
- you can write joins without random trial and error
- you can explain at least one normalization decision
- you can connect application actions to SQL operations

## Common Mistakes To Avoid

- designing tables around UI screens instead of data entities
- duplicating too much data because it feels easier at first
- avoiding joins because they seem hard
- writing queries without understanding the question being asked
- skipping constraints that should be explicit

## Expert Notes That Matter Early

### Data modeling is application design

A weak schema usually leads to weak backend logic.

### Joins are not optional complexity

They are one of the main tools that make relational databases powerful.

### Constraints are part of correctness

Do not leave all data integrity to application code.

## Suggested References

- PostgreSQL documentation
- Supabase documentation
- SQL tutorial resources
- schema design and normalization references

## Final Standard For This Week

The correct outcome of Week 05 is not "I learned some SQL syntax."

The correct outcome is:

"I can model a small relational system, write purposeful queries, and use a real Postgres-backed CRUD workflow with confidence."
