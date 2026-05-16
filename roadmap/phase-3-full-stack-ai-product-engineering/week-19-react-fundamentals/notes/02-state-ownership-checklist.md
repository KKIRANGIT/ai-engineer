# State Ownership Checklist

Use this checklist when reviewing any React screen.

## Shared State

Ask:

- do multiple components need this changing value?
- does one component need to update something another component renders?

If yes, shared state in a parent may be justified.

## Local State

Ask:

- is this only needed for one component's temporary UI behavior?
- is this just draft input state?

If yes, keep it local unless there is a concrete reason to lift it.

## Derived Values

Ask:

- can this be computed from existing state and props?

Examples:

- filtered lists
- visible counts
- the selected object resolved from an id

If yes, derive it instead of storing it.

## Effects

Ask:

- am I synchronizing with something outside React?

Good examples:

- localStorage
- document title
- timers
- subscriptions

Bad example:

- computing values that belong in render

## Final Review Question

If you removed one piece of state, would the screen become simpler without losing correctness?

If yes, that state may not belong there.
