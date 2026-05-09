-- Week 05 - Joins and Aggregation Lab

-- Question 1:
-- Show each task together with its project name.
SELECT
    tasks.id,
    tasks.title,
    projects.name AS project_name
FROM tasks
JOIN projects ON tasks.project_id = projects.id
ORDER BY tasks.id;

-- Question 2:
-- Show how many tasks each project has.
SELECT
    projects.name,
    COUNT(tasks.id) AS task_count
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
GROUP BY projects.id, projects.name
ORDER BY task_count DESC, projects.name ASC;

-- Question 3:
-- Show each task with its assigned tags.
SELECT
    tasks.title,
    tags.name AS tag_name
FROM tasks
JOIN task_tags ON task_tags.task_id = tasks.id
JOIN tags ON tags.id = task_tags.tag_id
ORDER BY tasks.title, tags.name;
