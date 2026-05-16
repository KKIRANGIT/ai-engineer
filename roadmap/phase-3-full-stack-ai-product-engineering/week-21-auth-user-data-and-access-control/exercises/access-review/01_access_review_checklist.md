# Access Review Checklist

Review one existing feature using this checklist:

- Can an unauthenticated user reach the route?
- Can an authenticated but wrong user query the record directly?
- Is there a server-side check for the mutation path?
- Would the UI accidentally reveal metadata before access is denied?
- Does the audit trail capture who performed the action?

Write one concrete risk you found, even if the feature is only local.
