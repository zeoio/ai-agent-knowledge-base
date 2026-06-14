# GitHub Publish Guide

## Option A: Existing Empty GitHub Repository

Create an empty repository on GitHub, then run:

```bash
git remote add origin git@github.com:<your-user>/<repo-name>.git
git push -u origin main
```

If `origin` already exists:

```bash
git remote set-url origin git@github.com:<your-user>/<repo-name>.git
git push -u origin main
```

## Option B: GitHub CLI

Install and authenticate GitHub CLI:

```bash
brew install gh
gh auth login
```

Create and push the repository:

```bash
gh repo create ai-agent-knowledge-base --private --source=. --remote=origin --push
```

Use `--public` instead of `--private` only if the repository will never contain private notes, local paths, installed tool details, or security-sensitive context.

## Recommended Defaults

- Visibility: `private`
- Default branch: `main`
- Repo name: `ai-agent-knowledge-base` or `ai-research-toolkit`
- Description: `Personal AI project, skill, tool, and document knowledge base for human and AI-assisted research.`

## After Pushing

Run:

```bash
git remote -v
git status --short --branch
```

Confirm that `main` tracks `origin/main`.
