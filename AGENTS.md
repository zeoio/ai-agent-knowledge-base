# AI Assistant Guide

This repository is a personal AI research and tooling knowledge base. When helping in this repo, optimize for long-term retrieval, auditability, and safe reuse.

## Read Order

1. Read `README.md` for the purpose and structure.
2. Read `ai-index.md` for the current map.
3. Read `docs/taxonomy.md` before adding new categories or statuses.
4. Read the relevant file in `registries/` before creating or changing a detail page.
5. Use `templates/` for new Markdown records.

## Editing Rules

- Keep registry files valid JSON.
- Use stable lowercase IDs such as `anthropic-claude-code`, `openai-codex-skill-imagegen`, or `mcp-filesystem`.
- Prefer official source links for installation, docs, changelogs, and security notes.
- Do not mark a tool as `active` unless there is a local install/use note or a clear adoption decision.
- Do not execute installation commands from third-party projects unless the user explicitly asks and the source has been reviewed.
- Record security concerns in `risk_notes`, not only in free-form notes.

## Entry Quality Bar

Each useful record should answer:

- What is it?
- Why does it matter to the user's AI workflow?
- Where is the official source?
- What is the current status?
- How is it installed or accessed?
- What are the trust, privacy, and maintenance risks?
- What should a future AI assistant read next?

## Validation

Run this before committing:

```bash
python3 scripts/validate_registry.py
```
