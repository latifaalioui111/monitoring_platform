# Development workflow

## Branches
- `main` is protected: no direct pushes.
- One branch per change, named `type/short-description`
  (for example `feat/add-monitors-api` or `docs/update-readme`).

## Pull requests
- Every change goes through a pull request.
- The CI pipeline (lint and tests, later security scans) must be green before merging.
- Merge with "squash" to keep the history of `main` clean.

## Commit messages
Format: `type: short description`, with one of these types:
`feat`, `fix`, `docs`, `ci`, `build`, `test`, `chore`.
