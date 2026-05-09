INSERT INTO users (email, full_name) VALUES
    ('asha@example.com', 'Asha Patel'),
    ('ravi@example.com', 'Ravi Shah');

INSERT INTO projects (owner_user_id, name, status, created_at) VALUES
    (1, 'AI Engineer Roadmap', 'active', '2026-05-01'),
    (2, 'Portfolio Refresh', 'active', '2026-05-02');

INSERT INTO tasks (project_id, title, status, priority, due_date) VALUES
    (1, 'Design the learning schema', 'open', 5, '2026-05-11'),
    (1, 'Write join examples', 'open', 4, '2026-05-12'),
    (2, 'Clean landing page copy', 'done', 3, '2026-05-09');

INSERT INTO tags (name) VALUES
    ('sql'),
    ('docs'),
    ('important');

INSERT INTO task_tags (task_id, tag_id) VALUES
    (1, 1),
    (1, 3),
    (2, 1),
    (2, 2),
    (3, 2);
