# Week 05: SQL, Postgres, and Data Modeling

Back to [Phase 1](../README.md)

## Goal

Understand relational data properly so you can design systems intentionally instead of treating the database as a storage box you poke at randomly.

This week is about learning how applications represent structure, relationships, and constraints in data.

By the end of this week, you should be able to:

- explain what tables, rows, columns, and relationships represent
- design a schema for a small application
- use `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, and `JOIN`
- understand primary keys and foreign keys
- distinguish one-to-one, one-to-many, and many-to-many relationships
- write readable SQL that answers a real question
- connect application actions to database operations

This week is where backend thinking becomes much more concrete.

## What This Week Is Actually Training

At surface level, Week 05 looks like "learn SQL and use Postgres."

The real training target is deeper:

- thinking in entities and relationships instead of screens and forms
- understanding how constraints preserve truth
- learning to ask the database a clear question
- designing data so the application stays coherent later
- seeing how code and schema influence each other

That is why this week matters so much. Weak data modeling creates hidden problems everywhere later:

- auth state becomes messy
- billing data becomes fragile
- document metadata becomes inconsistent
- analytics become hard to trust
- reporting becomes painful

## Scope Boundaries

Study deeply this week:

- entities and relationships
- table design
- primary keys and foreign keys
- one-to-one, one-to-many, and many-to-many modeling
- `SELECT`, filters, ordering, grouping, and joins
- constraints and defaults
- transaction thinking
- CRUD from Python into a relational database

Do not go deep on these yet:

- advanced query optimization
- execution plans in detail
- stored procedures
- row-level locking details
- advanced indexing strategies
- multi-database scaling patterns

The goal is strong relational foundations, not database specialization.

## Important Implementation Note

This week is named around SQL, Postgres, and data modeling.

For the hands-on code in this workspace, the project uses Python's built-in `sqlite3` module so you can run the exercises and project without installing a separate database server first.

Why this is still a good engineering choice:

- SQL fundamentals transfer directly
- relational design principles transfer directly
- CRUD thinking transfers directly
- Python database access patterns still become clearer

You should treat SQLite here as a low-friction learning vehicle and PostgreSQL as the production-grade relational target you are moving toward.

## Week 05 Outcomes

You are successful this week if you can do most of the following with confidence:

- map a small application into tables and relationships
- explain why a primary key exists
- explain why a foreign key exists
- write joins intentionally instead of by random trial and error
- explain one normalization decision
- identify where constraints belong in the schema
- connect code actions like "create task" or "list project summary" to actual SQL operations

## How Week 05 Builds On Week 04

Week 04 improved your developer workflow around repositories, files, config, and automation.

Week 05 improves the internal structure of application data.

Now you are asking:

- what entities exist
- what facts should be stored
- what constraints should always remain true
- how code should read and write those facts

That makes this week one of the most important architectural weeks in Phase 1.

## Core Relational Concepts To Master

## 1. Relational Thinking

You are not storing screens in a database. You are storing facts about entities and relationships.

Think in terms of:

- what things exist
- what attributes describe them
- how they relate
- what must remain true

Example entities:

- users
- projects
- tasks
- tags
- invoices
- documents

Good schemas start with clear nouns and clear relationships.

## 2. Tables, Rows, and Columns

You should understand:

- table = one entity or one relationship table
- row = one record
- column = one attribute

Good early rule:

Design for meaning first, then for convenience.

## 3. Keys and Relationships

You must understand:

- primary key
- foreign key
- one-to-one
- one-to-many
- many-to-many through a join table

This is the real power of relational systems. If relationships are modeled poorly, the rest of the app starts fighting the schema.

## 4. Normalization and Practical Simplicity

Normalization aims to:

- reduce duplication
- reduce inconsistent updates
- improve data reliability

Beginner-friendly question:

If this value changes, how many places must I update it?

If the answer is "too many," you are likely duplicating data too aggressively.

You do not need perfect theory this week. You do need better structure than "copy data wherever convenient."

## 5. Core Querying

You need strong comfort with:

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`
- `GROUP BY`
- aggregate functions like `COUNT` and `AVG`
- `JOIN`

Important rule:

Never write a query as only syntax practice. Always know what question it is answering.

## 6. Joins

This is one of the most important topics of the week.

You should understand:

- inner join
- left join
- why some rows appear and others do not
- how foreign keys make joins meaningful

If joins feel confusing, slow down and reason with tiny tables and tiny result sets.

## 7. Constraints and Integrity

The database should enforce some truth, not only your application code.

Important constraints:

- primary key
- foreign key
- `NOT NULL`
- `UNIQUE`
- `CHECK`
- defaults

This matters because bugs happen. Constraints give your system a second layer of protection.

## 8. Transactions

At the concept level, learn:

- some operations should succeed or fail together
- partial writes can leave the system in bad state
- transactions preserve consistency boundaries

The local project includes a simple example of doing multi-step writes safely.

## 9. Postgres and Supabase Mental Mapping

You should still learn how this week maps forward to Postgres:

- PostgreSQL remains the real target database for many production systems
- Supabase is a practical hosted Postgres path later in the roadmap
- SQL fundamentals and schema discipline still transfer directly

This week gives you a local low-friction path first, then a mental bridge to PostgreSQL.

## Best Learning Sequence For This Week

Use this order:

1. relational thinking
2. tables and keys
3. relationships
4. basic `SELECT` queries
5. joins and grouping
6. constraints and integrity
7. transactions
8. CRUD from Python

## A No-Doubt Execution Plan For The Week

### Day 1: Entities and schema design

Study:

- entities
- attributes
- relationships
- key selection

Practice:

- do the schema-design exercise
- inspect the project tracker schema

Checkpoint:

- can you explain why each table exists

### Day 2: Basic querying

Study:

- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`

Practice:

- do the select/filtering lab
- answer each query question in words before reading the SQL

Checkpoint:

- can you explain what each query is asking

### Day 3: Joins and aggregation

Study:

- `JOIN`
- grouping
- counts

Practice:

- do the joins-and-aggregation lab
- inspect the report queries in the project

Checkpoint:

- can you explain why the joined rows appear

### Day 4: Constraints and integrity

Study:

- `NOT NULL`
- `UNIQUE`
- foreign keys
- defaults

Practice:

- do the constraints lab
- inspect the project schema file closely

Checkpoint:

- can you explain which truths are enforced in the database vs in the app

### Day 5: Transactions and multi-step writes

Study:

- transaction boundaries
- consistency thinking

Practice:

- run the transaction demo
- inspect how the project writes tags and tasks together

Checkpoint:

- can you explain what should happen if the second half of a write fails

### Day 6: CRUD project walkthrough

Study:

- schema file
- repository functions
- reports

Practice:

- run the project demo
- read the repository methods one by one

Checkpoint:

- can you explain how Python code maps to SQL behavior

### Day 7: Review and schema defense

Review:

- reread the week README
- review the schema checklist
- explain your design choices aloud

Checkpoint:

- can you justify why the data is shaped this way

## Week 05 Workspace Standard

This week now includes a real hands-on database workspace.

Actual structure:

```text
week-05-sql-postgres-and-data-modeling/
|-- exercises/
|   |-- schema-design/
|   |-- select-filtering/
|   |-- joins-and-aggregation/
|   |-- constraints-and-integrity/
|   |-- transactions/
|   `-- README.md
|-- projects/
|   |-- sql-query-lab/
|   `-- project-tracker-db/
|       |-- app/
|       |-- sql/
|       |-- tests/
|       |-- data/
|       |-- .env.example
|       |-- .gitignore
|       `-- README.md
|-- notes/
`-- README.md
```

## Main Build Goals

This week has two build layers.

### Layer 1: SQL query practice

You need a local practice area for:

- schema creation
- inserts
- filters
- joins
- grouping
- integrity rules

That is what `projects/sql-query-lab/` is for.

### Layer 2: Real relational CRUD project

You also need one small application-facing database project that demonstrates:

- schema design
- seed data
- CRUD operations
- reporting queries
- transaction-aware writes

That is what `projects/project-tracker-db/` is for.

## Deliverables

By the end of the week, you should have:

- completed the SQL exercises
- reviewed the query lab scripts
- run the project tracker demo
- inspected the schema and repository code
- explained one normalization or relationship decision clearly
- written a short note about what now feels clearer about relational design

## Best Sources For Week 05

Use sources in this order.

### Tier 1: Official PostgreSQL Sources

1. PostgreSQL current documentation
   Link: https://www.postgresql.org/docs/current/

2. PostgreSQL tutorial: querying a table
   Link: https://www.postgresql.org/docs/current/tutorial-select.html

3. PostgreSQL constraints
   Link: https://www.postgresql.org/docs/current/ddl-constraints.html

4. PostgreSQL queries
   Link: https://www.postgresql.org/docs/current/queries.html

### Tier 2: Python and SQLite Reference

1. Python `sqlite3` documentation
   Link: https://docs.python.org/3/library/sqlite3.html

2. SQLite documentation
   Link: https://www.sqlite.org/docs.html

Important note:

The local code uses SQLite for low-friction practice, but the relational concepts are deliberately aligned with PostgreSQL-style thinking.

### Tier 3: Supabase Forward Link

1. Supabase database overview
   Link: https://supabase.com/docs/guides/database/overview

2. Supabase joins and nested tables
   Link: https://supabase.com/docs/guides/database/joins-and-nesting

Use these to understand where today's relational modeling flows later in the roadmap.

## Source Strategy That Avoids Confusion

For Week 05, use this source stack:

1. PostgreSQL docs for relational and SQL truth
2. Python `sqlite3` docs for local runnable workflow
3. local exercises for query and modeling repetition
4. the project tracker database project for real understanding

That stack is enough.

## Exact Study Path Through The Sources

If you want the least ambiguity, use this sequence:

1. read the PostgreSQL tutorial and constraints overview
2. do the schema-design exercise
3. run the select/filtering and joins labs
4. inspect the query lab schema and seed data
5. read the Python `sqlite3` docs selectively
6. inspect the project tracker schema and repository code
7. run the project demo and tests
8. review the notes and modeling checklist

## Exit Criteria

You are ready for Week 06 only if most of these are true:

- you can model a small app in tables with confidence
- you understand primary keys and foreign keys
- you can write joins without guessing blindly
- you can explain one normalization or anti-duplication decision
- you can map application actions to SQL operations
- you can explain why constraints matter

If these are not true, repeat the schema and query work before moving on.

## Common Mistakes That Create Confusion Later

- designing tables around UI screens instead of entities
- duplicating too much data because it feels easier early
- avoiding joins because they seem hard
- writing SQL without knowing the question being asked
- skipping constraints that should be explicit
- treating the database as passive storage instead of part of system correctness

## Expert Notes

### Data modeling is application design

A weak schema usually produces weak backend logic.

### Joins are not optional complexity

They are one of the main tools that make relational databases powerful.

### Constraints are part of correctness

Do not leave all integrity protection to application code.

## How Week 05 Connects To Week 06

Week 06 moves into async Python, data pipelines, and Docker.

That week becomes easier if Week 05 is strong because data pipelines and services still depend on:

- clean structure
- reliable records
- query clarity
- predictable data boundaries

Relational thinking keeps paying off even when the stack grows.

## Final Standard For This Week

The correct outcome is not:

"I learned some SQL syntax."

The correct outcome is:

"I can model a small relational system, write purposeful queries, explain why the schema is shaped the way it is, and use a real CRUD workflow from Python with confidence."
