# Taxonomy

This taxonomy keeps AI projects, tools, skills, and documents searchable across different assistants.

## Asset Types

| Type | Meaning | Typical Location |
| --- | --- | --- |
| `project` | Product, open source project, research project, model, company, lab, framework | `projects/` |
| `skill` | Agent skill, prompt workflow, task capability pack, reusable instruction bundle | `skills/` |
| `tool` | MCP server, CLI, SDK, plugin, extension, local app, hosted service | `tools/` |
| `document` | Paper, official docs, tutorial, report, standard, spec | `documents/` |
| `research_note` | Free-form analysis, experiment, comparison, review | `research-notes/` |
| `decision` | Adopt/reject/replace/pause decision with rationale | `decisions/` |

## Status

| Status | Meaning |
| --- | --- |
| `watching` | Worth monitoring, not yet evaluated deeply |
| `evaluating` | Currently being tested or read |
| `active` | Adopted and used in a real workflow |
| `paused` | Not currently used, but still potentially relevant |
| `rejected` | Reviewed and intentionally not adopted |
| `archived` | Kept only for history |

## Trust Level

| Level | Use When |
| --- | --- |
| `unknown` | New source, not reviewed |
| `low` | Weak maintenance, unclear origin, risky permissions, or poor docs |
| `medium` | Reasonable source and docs, but limited operational experience |
| `high` | Official source, strong maintenance, clear permissions, successful local use |
| `critical` | Core dependency for daily workflow; changes require extra review |

## Review Dimensions

Use these dimensions when evaluating an item:

- `use_case`: What job does it do?
- `source_quality`: Official docs, code quality, release cadence, community trust.
- `install_surface`: Local binary, package manager, browser extension, MCP, SaaS, API key.
- `data_access`: Files, browser, shell, credentials, clipboard, private repos, cloud data.
- `maintenance`: Last release, issue activity, compatibility, ownership.
- `cost`: Free, paid, usage-based, self-hosting cost.
- `lock_in`: How hard it is to replace.
- `ai_readability`: Whether an AI assistant can understand and reuse the record easily.

## Tags

Prefer concrete tags. Examples:

- `agent`
- `coding`
- `mcp`
- `rag`
- `browser-automation`
- `image-generation`
- `voice`
- `docs`
- `evals`
- `security`
- `local-first`
- `open-source`
- `paid-saas`
