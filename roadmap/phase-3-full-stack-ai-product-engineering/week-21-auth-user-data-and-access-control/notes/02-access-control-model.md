# Access-Control Model Notes

Use this structure when documenting the week project or your own product:

## Actors

- end user
- workspace member
- workspace admin

## Protected Assets

- tickets
- comments
- generated summaries
- billing metadata

## Enforcement Layers

- UI: hide actions the actor cannot use
- route or handler: reject unauthorized requests
- data layer: scope reads and writes to allowed owners

## Non-Negotiable Rule

Frontend visibility is not authorization.
