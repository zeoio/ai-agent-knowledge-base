# Workflow

## Intake

When you find a new project, skill, tool, or document:

1. Create a short note in `inbox/` or add an issue on GitHub.
2. Capture the original link, date found, and why it looks useful.
3. Do not install it immediately if it asks for shell, filesystem, browser, or credential access.

## Triage

Move the item into a registry when it has enough context:

- `registries/projects.json`
- `registries/skills.json`
- `registries/tools.json`
- `registries/documents.json`

Set `status` to `watching` unless you are actively testing it.

## Evaluation

For any item being tested:

1. Change `status` to `evaluating`.
2. Create a Markdown detail page from the relevant template.
3. Record installation commands, environment assumptions, observed behavior, and limitations.
4. Add `risk_notes` for permissions, data exposure, licensing, or unclear maintenance.

## Adoption

Only mark an item as `active` when:

- The official source is linked.
- Installation or access method is documented.
- Risks are recorded.
- There is at least one concrete use case.
- A future AI assistant can understand when to recommend it.

## Review Cadence

- Review `active` tools monthly.
- Review `evaluating` tools weekly while they are being tested.
- Review `watching` items when they appear in a new workflow or major release.
- Move stale items to `archived` instead of deleting them.
