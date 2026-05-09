-- Show each project with the owner's name.
SELECT
    projects.name AS project_name,
    users.full_name AS owner_name
FROM projects
JOIN users ON users.id = projects.owner_user_id
ORDER BY projects.id;

-- Show open tasks ordered by highest priority first.
SELECT
    title,
    priority,
    due_date
FROM tasks
WHERE status = 'open'
ORDER BY priority DESC, due_date ASC;

-- Count how many tasks each project has.
SELECT
    projects.name,
    COUNT(tasks.id) AS task_count
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
GROUP BY projects.id, projects.name
ORDER BY task_count DESC;

-- Show each task with its tag names.
SELECT
    tasks.title,
    tags.name AS tag_name
FROM tasks
JOIN task_tags ON task_tags.task_id = tasks.id
JOIN tags ON tags.id = task_tags.tag_id
ORDER BY tasks.title, tags.name;
