# Week 19: React Fundamentals

Back to [Phase 3](../README.md)

## Goal

Become productive enough in React that interface building stops feeling like syntax assembly and starts feeling like component and state design.

This week is about interface thinking, not just JSX familiarity.

## Why This Week Matters

Most AI products fail to feel usable not because the model is weak, but because the interface is weak:

- state is confusing
- forms are awkward
- feedback is unclear
- layout is improvised

React is the first layer where product quality becomes visible. If your interface model is weak, every later feature becomes harder to express cleanly.

## Week 19 Outcomes

By the end of this week, you should be able to:

- think in components instead of pages of mixed logic
- manage local state with confidence
- use effects correctly for external synchronization
- build forms and list views cleanly
- separate presentational and behavioral concerns
- create a small dashboard or app shell that feels coherent

## What To Learn

## 1. Component mental model

A React component is not just a function that returns UI. It is a unit of:

- structure
- state ownership
- event handling
- reuse

You should learn to ask:

- what belongs in this component
- what state belongs here
- what should be passed in as props

## 2. Composition over duplication

React becomes powerful when you compose:

- layout components
- reusable input components
- cards, tables, shells, and sections

Important rule:

Do not solve repeated UI by copy-pasting first. Ask whether a reusable component is justified.

## 3. State and render flow

You need a clean mental model of:

- render
- state updates
- derived values
- controlled inputs

Many beginner React bugs come from weak state ownership decisions rather than syntax mistakes.

## 4. Effects and external synchronization

Effects should be used to synchronize with external systems, not as a default place to put logic.

Learn:

- what `useEffect` is for
- what should stay in render logic
- how to avoid unnecessary effect complexity
- when patterns such as `useEffectEvent` are useful in modern React for reading latest values inside effects without re-synchronizing unnecessarily

## 5. Forms and validation

Real products are full of forms.

You should be comfortable with:

- controlled form fields
- submit handling
- validation feedback
- disabled and loading states

Good form UX matters especially for AI products because many user inputs are large, multi-step, or expensive to process.

## 6. Accessibility basics

You do not need deep accessibility specialization yet, but you should respect:

- labels
- keyboard flow
- focus states
- semantic elements
- readable feedback messages

## Best Learning Sequence For This Week

1. component model
2. props and composition
3. local state
4. forms and events
5. effects
6. UI shell assembly

## Recommended Daily Breakdown

### Day 1: Component thinking

Focus:

- component boundaries
- props
- reusable UI pieces

### Day 2: State and forms

Focus:

- controlled inputs
- local state transitions

### Day 3: Lists, dashboards, and composition

Focus:

- render collections
- cards, lists, panels, shells

### Day 4: Effects and synchronization

Focus:

- fetching or syncing carefully
- avoiding effect misuse

### Day 5: Accessibility and cleanup

Focus:

- labels
- form feedback
- semantic layout

### Day 6: Build one dashboard or app shell

### Day 7: Refactor and document component decisions

## Build Plan

Build at least:

- one dashboard screen
- one form-heavy flow
- one chat-style or activity-feed style interface shell

## Deliverables

- one React UI module or mini app
- one note on state ownership decisions
- one before/after refactor note if you improved a messy component split

## Exit Criteria

- you can decompose a page into components confidently
- you can manage local state without tangling it
- you can build forms with clear validation states
- you understand what effects are actually for

## Common Mistakes To Avoid

- putting too much logic in one component
- using effects for logic that belongs in render or event handlers
- making forms uncontrolled and hard to validate
- copying UI fragments instead of composing reusable pieces

## Expert Notes That Matter Early

### Components are architecture

Component boundaries shape maintainability.

### State ownership matters more than hook count

The hardest React bugs often come from state living in the wrong place.

### Forms are product-critical

If your inputs are clumsy, the rest of the product feels weak.

## Final Standard For This Week

The correct outcome of Week 19 is not "I know React hooks."

The correct outcome is:

"I can design and build small React interfaces with sensible component boundaries, state ownership, and usable interaction patterns."
