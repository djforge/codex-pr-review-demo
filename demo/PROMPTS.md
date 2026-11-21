# Demo prompts

## Desktop batch

> Review every open PR labeled `demo-desktop`. For each PR, inspect the diff, run relevant tests, and leave a concise GitHub review. Merge it with squash only if CI passes and you find no blocking correctness, security, or reliability issue. Otherwise request changes and explain the blocker. Finish with a table of reviewed, merged, and blocked PRs.

## iOS batch

> In `djforge/codex-pr-review-demo`, review every open PR labeled `demo-ios`. For each PR, inspect the diff and CI. Merge safe PRs with squash; request changes on unsafe PRs. Finish with a short success summary listing merged and blocked PR numbers.

## Success message

> Codex demo complete: all 12 PRs reviewed; safe changes merged; risky changes blocked with actionable feedback.
