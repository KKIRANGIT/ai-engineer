# Environment and Git Ignore Lab

## What This Exercise Trains

- config hygiene
- secrets discipline
- `.env.example` usage
- `.gitignore` awareness

## Practice Target

Use:

- [python-starter-template](../../projects/python-starter-template)

## Suggested Flow

1. Read `.env.example`.
2. Create a local `.env` file by copying the example.
3. Read `.gitignore`.
4. Confirm that `.env` is ignored.
5. Explain why `.env.example` should be committed but `.env` usually should not.

## Questions To Answer

- what belongs in `.env.example`
- what should never be committed
- what kind of files should usually be ignored

## Success Check

You should be able to explain the difference between:

- shareable configuration shape
- private machine-specific configuration
