INSERT INTO users (email, full_name) VALUES
    ('asha@example.com', 'Asha Patel'),
    ('ravi@example.com', 'Ravi Shah');

INSERT INTO projects (owner_user_id, name, status, created_at) VALUES
    (1, 'AI Study Planner', 'active', '2026-05-01'),
    (2, 'Portfolio Site Refresh', 'active', '2026-05-03');

INSERT INTO tasks (project_id, title, status, priority, due_date) VALUES
    (1, 'Write schema notes', 'open', 5, '2026-05-10'),
    (1, 'Add SQL examples', 'open', 4, '2026-05-11'),
    (2, 'Review design system', 'done', 3, '2026-05-08');

INSERT INTO tags (name) VALUES
    ('backend'),
    ('docs'),
    ('priority');

INSERT INTO task_tags (task_id, tag_id) VALUES
    (1, 2),
    (1, 3),
    (2, 1),
    (3, 1);
