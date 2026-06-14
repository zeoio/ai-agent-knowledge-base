# AI Index

Use this file as the fast entry point for AI tools. It summarizes where to look before reading the whole repository.

## Current Map

| Need | Start Here | Then Read |
| --- | --- | --- |
| Find tracked AI projects | `registries/projects.json` | `projects/` |
| Find installed or candidate skills | `registries/skills.json` | `skills/` |
| Find tools, MCP servers, CLIs, plugins | `registries/tools.json` | `tools/` |
| Find docs, papers, tutorials | `registries/documents.json` | `documents/` |
| Understand categories and statuses | `docs/taxonomy.md` | `docs/workflow.md` |
| Add a new item | `templates/` | `docs/workflow.md` |
| Check safety posture | `docs/security-and-trust.md` | relevant registry entry |

## Query Strategy For AI Assistants

1. Use registry JSON for broad filtering.
2. Use Markdown detail pages for context, decisions, and caveats.
3. Prefer `active` and `evaluating` entries over `watching`.
4. Treat `rejected` and `archived` entries as historical unless the user asks to revisit them.
5. If a source link may have changed, verify online before giving current installation or pricing advice.

## Important Conventions

- Registry IDs are stable and should not be renamed casually.
- Detail pages should use the same ID in the filename when practical.
- Dates use `YYYY-MM-DD`.
- Links should point to official docs, GitHub repositories, release notes, or primary papers when available.
