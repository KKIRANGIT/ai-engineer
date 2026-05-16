# Week 19 Exercises

Back to [Week 19 README](../README.md)

## Purpose

These exercises are designed to teach React fundamentals as interface design decisions, not as disconnected syntax drills.

The order matters. Start with component decomposition, then move into state ownership, then forms, then effects.

## Exercise Groups

### 1. Component thinking

Files:

- [01_break_dashboard_into_components.md](component-thinking/01_break_dashboard_into_components.md)
- [02_props_contract_example.jsx](component-thinking/02_props_contract_example.jsx)

Focus:

- turning one screen into smaller responsibilities
- understanding which component should own which data
- thinking in contracts instead of copy-pasted sections

### 2. State and derived data

Files:

- [01_state_ownership_notes.md](state-and-derived-data/01_state_ownership_notes.md)
- [02_derived_queue_view.js](state-and-derived-data/02_derived_queue_view.js)

Focus:

- choosing where state should live
- understanding shared state vs local draft state
- deriving visible lists and stats from one source of truth

### 3. Forms and validation

Files:

- [01_controlled_form_example.jsx](forms-and-validation/01_controlled_form_example.jsx)
- [02_validation_rules.js](forms-and-validation/02_validation_rules.js)

Focus:

- controlled input handling
- validation timing
- normalized submit data

### 4. Effects and UI shells

Files:

- [01_effect_for_local_storage.js](effects-and-ui-shells/01_effect_for_local_storage.js)
- [02_dashboard_shell_sketch.md](effects-and-ui-shells/02_dashboard_shell_sketch.md)

Focus:

- identifying when an effect is justified
- designing dashboard layout regions before coding every component

## How To Use These Exercises

For each file:

1. read the explanation
2. explain the pattern in your own words
3. compare it to the main project
4. decide what lesson should carry into the project

These are not meant to replace the project. They are meant to make the project easier to reason about.
