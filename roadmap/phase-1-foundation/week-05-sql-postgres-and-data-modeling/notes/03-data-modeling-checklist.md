# Data Modeling Checklist

Use this checklist when designing a small relational schema.

- What entities actually exist?
- What should each table represent?
- Which column is the primary key?
- Which values must always be present?
- Which values must be unique?
- Which tables need foreign keys?
- Where do I need a join table?
- Am I duplicating data that should live in one place?
- Which constraints should the database enforce directly?
- Which application actions will query or update this data most often?

If you cannot answer these clearly, the schema still needs work.
