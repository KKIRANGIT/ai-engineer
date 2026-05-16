# Exercise: State Ownership Notes

## Goal

Decide where state belongs before building the project.

## Rule Of Thumb

State should live in the lowest component that needs to control it.

Lift state upward only when:

- multiple components need the same changing value
- one component needs to affect another component's rendered result
- the value represents the shared truth of the screen

## Apply It To Week 19

### Good local state

- the current draft inside `TicketComposer`
- whether a small local panel is expanded

### Good shared state

- the ticket collection
- the selected ticket id
- active queue filters

### Good derived values

- visible tickets after filtering
- counts by status
- recent activity feed based on ticket history

## Bad Pattern To Avoid

Do not store:

- `visibleTickets`
- `openTicketCount`
- `selectedTicketObject`

if those values can be recomputed from the main ticket state and selected id.

If you store both the source data and many copies of derived truth, they will eventually drift apart.
