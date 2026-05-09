# HTTP Debugging Checklist

Use this order when an integration fails.

1. Check the URL.
2. Check the method.
3. Check the query parameters.
4. Check the headers.
5. Check whether auth is required.
6. Check the status code.
7. Check whether the response body is JSON, text, or empty.
8. Check whether the response shape matches your assumption.
9. Check whether the failure is rate-limit related.
10. Check whether the timeout is too aggressive or missing.

Useful rule:

- do not start by editing random code
- start by checking what request you sent and what response you got back
