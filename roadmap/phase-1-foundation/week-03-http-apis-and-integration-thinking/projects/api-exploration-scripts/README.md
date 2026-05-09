# API Exploration Scripts

These scripts help you see different API response shapes and common integration patterns without jumping straight into a larger client wrapper.

## Included Scripts

- `github_public_events.py`
- `jsonplaceholder_posts.py`
- `httpbin_echo_demo.py`

## What They Teach

- GitHub: public event streams and selected-field extraction
- JSONPlaceholder: simple REST-style `GET` and `POST`
- httpbin: request reflection, query parameters, and headers

## Important Note

These scripts call public internet endpoints. They require a working network connection to run successfully.

They also use Python's standard library so you do not need extra dependencies for the basic exploration.

## Run Examples

```powershell
python github_public_events.py
python jsonplaceholder_posts.py
python httpbin_echo_demo.py
```
