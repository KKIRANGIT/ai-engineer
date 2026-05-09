-- Week 05 - Select and Filtering Lab
--
-- Read each question first, then inspect the query.

-- Question 1:
-- Show all projects ordered by newest first.
SELECT id, name, status, created_at
FROM projects
ORDER BY created_at DESC;

-- Question 2:
-- Show only tasks that are still open.
SELECT id, title, priority, due_date
FROM tasks
WHERE status = 'open'
ORDER BY priority DESC, due_date ASC;

-- Question 3:
-- Show tasks for one specific project.
SELECT id, title, status
FROM tasks
WHERE project_id = 1
ORDER BY id;

-- Question 4:
-- Show the three highest-priority tasks.
SELECT id, title, priority
FROM tasks
ORDER BY priority DESC, id ASC
LIMIT 3;
