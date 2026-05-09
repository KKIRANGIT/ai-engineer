# Git Command Cheat Sheet

## State inspection

- `git status`
- `git diff`
- `git log --oneline --graph --decorate`

## Starting a repo

- `git init`
- `git clone <url>`

## Staging and committing

- `git add <file>`
- `git add .`
- `git commit -m "message"`

## Branch workflow

- `git branch`
- `git switch -c feature/my-change`
- `git switch main`
- `git merge feature/my-change`

## Good habits

- check `git status` before and after meaningful steps
- commit related changes together
- write readable commit messages
- avoid giant mixed-purpose commits
