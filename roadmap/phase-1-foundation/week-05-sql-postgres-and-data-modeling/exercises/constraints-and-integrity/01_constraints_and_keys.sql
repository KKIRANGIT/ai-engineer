-- Week 05 - Constraints and Integrity Lab

-- These statements illustrate integrity rules you should recognize quickly.

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    owner_user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active',
    FOREIGN KEY (owner_user_id) REFERENCES users (id)
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'open',
    priority INTEGER NOT NULL CHECK (priority BETWEEN 1 AND 5),
    FOREIGN KEY (project_id) REFERENCES projects (id)
);

-- Questions to answer:
-- 1. Why should email be UNIQUE?
-- 2. Why is project_id NOT NULL on tasks?
-- 3. Why does priority use a CHECK constraint?
