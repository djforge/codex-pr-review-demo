# Codex PR Review Demo

A disposable Python service with intentionally mixed-quality pull requests for demonstrating Codex review and safe merge workflows.

## Demo rule

Ask Codex to review each PR, run the tests, leave an actionable GitHub review, and merge only when it finds no blocking issue and CI passes.

The PRs are split with the labels `demo-desktop` and `demo-ios`. Some are intentionally unsafe and should be blocked.

## Local checks

```bash
python -m unittest discover -s tests -v
```

See [`demo/PROMPTS.md`](demo/PROMPTS.md) for ready-to-use commands.
