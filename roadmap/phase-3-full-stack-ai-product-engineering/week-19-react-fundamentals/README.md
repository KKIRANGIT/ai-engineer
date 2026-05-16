# Week 19: React Fundamentals

Back to [Phase 3](../README.md)

## Goal

Become productive enough in React that interface building stops feeling like JSX assembly and starts feeling like component, state, and interaction design.

This week is about product-facing interface thinking, not just hook memorization.

## Why This Week Matters

Many AI products fail at the interface layer before they fail at the model layer.

The common failure pattern looks like this:

- state is scattered
- forms feel fragile
- feedback is unclear
- layout decisions are improvised
- components mix rendering, validation, and business rules in one place

React is where product quality becomes visible. If your interface model is weak, every later concern in Phase 3 becomes harder:

- streaming UX
- auth-aware shells
- billing states
- onboarding flows
- long-running task feedback
- admin and analytics panels

Week 19 should give you the UI discipline that later full-stack work depends on.

## What This Week Is Actually Training

Week 19 is training six deeper skills:

1. decomposing a screen into meaningful components
2. deciding where state should live
3. deriving views from state instead of duplicating data
4. building controlled forms with clear validation behavior
5. using effects only for true external synchronization
6. shaping one coherent UI shell instead of a pile of widgets

The real outcome is not "I used `useState`." The real outcome is "I can design a small React interface whose structure makes sense."

## Scope Boundary For This Week

This week focuses on:

- components
- props
- state ownership
- controlled forms
- derived lists and counters
- conditional rendering
- accessible UI patterns
- effects for external synchronization such as `localStorage` and `document.title`

This week does not require:

- server components
- full Next.js routing
- data fetching libraries
- advanced state managers
- deep animation systems
- form libraries

The correct goal is not maximum React coverage. The correct goal is strong fundamentals that reduce confusion in Weeks 20-28.

## Week 19 Outcomes

By the end of this week, you should be able to:

- break a screen into sensible components
- choose whether state belongs in a parent or child component
- build controlled forms without tangled handlers
- render filtered and sorted lists from derived state
- explain when an effect is justified and when it is a mistake
- assemble a small dashboard-style interface that feels coherent

## Best Source Strategy For This Week

Use sources in this order:

1. the local Week 19 workspace
2. official React learning pages
3. your own notes on state ownership and component boundaries

Do not overload this week with many tutorial sources. React becomes harder when you mix too many teaching styles at once.

## Recommended Official References

Use these official React sources as the primary external reference stack:

- React quick start: <https://react.dev/learn>
- Your first component: <https://react.dev/learn/your-first-component>
- Passing props to a component: <https://react.dev/learn/passing-props-to-a-component>
- Conditional rendering: <https://react.dev/learn/conditional-rendering>
- Rendering lists: <https://react.dev/learn/rendering-lists>
- Responding to events: <https://react.dev/learn/responding-to-events>
- State as a snapshot: <https://react.dev/learn/state-as-a-snapshot>
- Choosing the state structure: <https://react.dev/learn/choosing-the-state-structure>
- Sharing state between components: <https://react.dev/learn/sharing-state-between-components>
- Updating objects in state: <https://react.dev/learn/updating-objects-in-state>
- Updating arrays in state: <https://react.dev/learn/updating-arrays-in-state>
- Synchronizing with effects: <https://react.dev/learn/synchronizing-with-effects>
- You might not need an effect: <https://react.dev/learn/you-might-not-need-an-effect>
- Thinking in React: <https://react.dev/learn/thinking-in-react>
- `useEffect` reference: <https://react.dev/reference/react/useEffect>

These were chosen because they reflect current React guidance and reduce the chance of learning stale patterns.

## Recommended Project Direction For This Workspace

This workspace uses one realistic but manageable interface:

- a support workbench dashboard

Why this direction was chosen:

- it naturally teaches lists, filters, forms, and detail views
- it maps well to AI products that need operator-style dashboards
- it makes component boundaries visible
- it shows state ownership tradeoffs clearly
- it creates a good base for later Next.js and SaaS work

## Project Capabilities This Week Includes

The Week 19 project includes:

- a dashboard shell
- stat cards
- a controlled ticket composer form
- queue filters
- a searchable and filterable ticket list
- a selected-ticket detail panel
- a recent activity feed
- `localStorage` persistence
- document-title synchronization
- pure helper functions with Node-based tests

The project stays frontend-only on purpose so the React fundamentals remain inspectable.

## Recommended Build Sequence

1. define the screen regions and component map
2. identify the minimum shared state
3. build the form and list views separately
4. lift only the state that truly needs to be shared
5. derive filtered views and dashboard stats
6. add effects for real external synchronization only
7. refine the shell, feedback, and accessibility details

## Recommended Daily Breakdown

### Day 1: Component thinking

Focus:

- page regions
- reusable cards and panels
- props contracts

### Day 2: State ownership

Focus:

- local vs shared state
- derived state
- selection and filter behavior

### Day 3: Controlled forms

Focus:

- draft state
- validation
- submit handling
- disabled and error states

### Day 4: Lists and dashboard assembly

Focus:

- list rendering
- empty states
- detail panels
- stats derived from the same source data

### Day 5: Effects and synchronization

Focus:

- `localStorage`
- document title
- avoiding unnecessary effects

### Day 6: UI polish and accessibility

Focus:

- labels
- semantic headings
- keyboard-friendly structure
- readable status messages

### Day 7: Review and refactor

Focus:

- state ownership review
- simplify component responsibilities
- document your design decisions

## Hands-On Workspace Structure

```text
week-19-react-fundamentals/
|-- README.md
|-- exercises/
|   |-- README.md
|   |-- component-thinking/
|   |-- effects-and-ui-shells/
|   |-- forms-and-validation/
|   `-- state-and-derived-data/
|-- notes/
|   |-- 01-week-plan.md
|   |-- 02-state-ownership-checklist.md
|   `-- 03-react-review-questions.md
`-- projects/
    `-- support-workbench-react/
```

## Exercises

The exercises isolate the React decisions that beginners usually blur together.

You will practice:

- breaking a screen into components
- defining prop responsibilities
- choosing state ownership
- deriving filtered data without duplicating state
- building controlled form flows
- using effects only for external synchronization

Start here:

- [Exercises README](exercises/README.md)

## Main Project

Project:

- [support-workbench-react](projects/support-workbench-react/README.md)

This project is a React dashboard for managing a small support queue. It teaches:

- state ownership at the app and component level
- form validation using controlled inputs
- list and detail composition
- derived dashboard metrics
- filtered and selected views
- effects for `localStorage` and document metadata

It is intentionally realistic enough to feel like product work, but small enough that the architecture stays understandable.

## Deliverables

By the end of this week, you should have:

- one complete React fundamentals workspace
- one working dashboard-style React app
- one set of notes on state ownership and effect usage
- one small set of tested helper functions
- one clear explanation of your component split

## Exit Criteria

You are ready to move to Week 20 only if:

- you can explain why each major component exists
- you can point to the single source of truth for the main shared state
- your form logic is controlled and understandable
- your filters and stats are derived cleanly from shared data
- your effects are used only for external synchronization
- you can explain the difference between render logic, event logic, and effect logic

## Common Mistakes To Avoid

- storing values in state when they can be derived
- putting validation, rendering, and state orchestration in one giant component
- using effects to compute values that belong in render
- copying props into state without a real reason
- creating many tiny components before the responsibilities are clear
- building a visually complex UI that hides weak state decisions

## Expert Notes That Matter Early

### Components are architecture boundaries

A component split is not cosmetic. It determines how understandable your interface stays as more features arrive.

### State ownership matters more than hook count

The most common React bugs are not caused by forgetting a hook. They are caused by putting state in the wrong place.

### Derived views are cheaper than duplicated truth

If a list, count, or filtered view can be derived from existing state, derive it. Extra duplicated state creates drift.

### Effects are for the outside world

If the code is synchronizing with `localStorage`, browser metadata, timers, network calls, or subscriptions, an effect may be appropriate. If it is just computing a value for rendering, it usually is not.

### Product UIs win through clarity

A clean UI with obvious interaction flow teaches better engineering instincts than a flashy UI with weak data flow.

## Final Standard For This Week

The correct outcome of Week 19 is not:

"I can write JSX and hooks."

The correct outcome is:

"I can build a small React interface with sensible component boundaries, clear state ownership, controlled interactions, and effects used for the right reasons."
