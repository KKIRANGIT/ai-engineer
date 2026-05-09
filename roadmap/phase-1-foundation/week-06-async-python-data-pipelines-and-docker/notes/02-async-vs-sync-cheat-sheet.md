# Async vs Sync Cheat Sheet

## Synchronous thinking

- one step waits fully before the next step begins
- simple to read
- often enough for small scripts

## Asynchronous thinking

- useful when tasks spend time waiting on I/O
- helps overlap waiting periods
- adds coordination complexity

## Good use cases for async

- many HTTP requests
- multiple file reads
- message polling
- remote service calls

## Poor use cases for async

- tiny scripts
- CPU-heavy numeric work
- problems with no real I/O waiting

## Good question to ask

Am I mostly computing, or am I mostly waiting?
