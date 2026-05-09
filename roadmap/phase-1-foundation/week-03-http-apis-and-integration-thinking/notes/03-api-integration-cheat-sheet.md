# API Integration Cheat Sheet

## Common request parts

- method
- URL
- headers
- body
- timeout

## Common response parts

- status code
- headers
- body

## Common status code meaning

- `200`: success
- `201`: created
- `204`: success with no body
- `400`: bad request
- `401`: unauthorized
- `403`: forbidden
- `404`: not found
- `429`: rate limited
- `500`: server error

## Integration habits

- set a timeout
- parse only what you need
- check status codes before assuming success
- keep secrets out of source files
- wrap repeated HTTP logic in helper functions or a client class

## Good questions to ask while reading an API response

- what is the top-level type
- which fields are required
- which fields are optional
- what is the paging model
- what errors should I expect
