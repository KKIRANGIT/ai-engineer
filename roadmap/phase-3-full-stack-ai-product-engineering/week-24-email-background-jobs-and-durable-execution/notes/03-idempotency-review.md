# Idempotency Review

Check each workflow step:

1. Can the step be retried?
2. What external effect could be duplicated?
3. What unique key or status check prevents double-processing?
4. What would the system look like if the same event arrived twice?

If the answer is "it would probably be fine," the workflow is still under-specified.
