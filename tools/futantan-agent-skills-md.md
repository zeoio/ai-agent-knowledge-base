# Tool: Agent-Skills.md

## Summary

- ID: `futantan-agent-skills-md`
- Status: `watching`
- Trust level: `medium`
- Website: <https://agent-skills.md/>
- Source: <https://github.com/futantan/agent-skills.md>
- Checked: 2026-06-15
- Checked commit: `98cd624fb1542ad7880e1112576061bb2874de8e`
- Default branch: `main`
- License: unknown; no root `LICENSE` file found via raw GitHub URL during review

## Purpose

Agent-Skills.md is a hosted marketplace and directory for AI agent skills. It indexes skill repositories, lets users search and browse available skills, previews `SKILL.md` instructions, and supports downloading complete skill folders for local use.

It is not itself a single installable skill. It belongs in this repository as a tool for discovering and evaluating skills.

## Why It Matters

This repository tracks AI projects, tools, and skills for later reuse. Agent-Skills.md is useful because it provides a searchable entry point for finding new skills across repositories instead of discovering them one GitHub link at a time.

Typical uses:

- Search for skills by keyword, tag, author, or category.
- Preview a skill's `SKILL.md` before installing.
- Download a complete skill folder for local evaluation.
- Submit a GitHub repo or specific skills folder to the directory.

## Access Or Install

Hosted site:

```text
https://agent-skills.md/
```

Local development commands from the repository README:

```bash
git clone https://github.com/futantan/agent-skills.md.git
cd agent-skills.md
pnpm install
pnpm dev
```

The README says to open `http://localhost:3000` after starting the dev server.

Observed local requirements and stack:

- Node.js `>=20.9.0`
- pnpm
- Next.js App Router
- React
- TypeScript
- Tailwind CSS
- Drizzle ORM
- PostgreSQL
- oRPC

## Evaluation Notes

Read source:

- Hosted site homepage.
- GitHub repository page.
- Raw `README.md`.
- Raw `package.json`.
- `git ls-remote` HEAD.

GitHub unauthenticated API was rate-limited during review, so repository metadata was gathered from the public GitHub page and raw files.

Not yet done:

- Local clone.
- Local development run.
- Review of database schema, submission flow, download flow, and indexing implementation.
- Review of how skill popularity, authorship, and download counts are computed.

## Risks

- Directory trust is not skill trust. Every skill found through the site still needs separate review.
- Downloaded skill folders can include instructions, scripts, assets, or references that influence future agent behavior.
- Skills may request filesystem, shell, browser, API, or credential access after installation.
- Search results, counts, rankings, and repository metadata are dynamic and should be rechecked before using a skill.
- If self-hosted, environment variables and database credentials must remain local.
- Licensing of the site code was unclear at review time because no root `LICENSE` file was found.

## Usage Guidance

Use this tool when looking for candidate skills to evaluate, compare, or track in this repository.

Do not use it as proof that a skill is safe or high quality. Treat it as a discovery layer only. Any skill discovered through Agent-Skills.md should be added to `registries/skills.json` with its own source review before installation or activation.

## Links

- Website: <https://agent-skills.md/>
- GitHub: <https://github.com/futantan/agent-skills.md>
- README: <https://github.com/futantan/agent-skills.md/blob/main/README.md>
- Submit: <https://agent-skills.md/submit>

## Next Actions

- [ ] Recheck repository license.
- [ ] Review the submission and download implementation if planning to self-host.
- [ ] Use the site to identify candidate skills, then record each skill separately.
- [ ] Keep this entry as `watching` until it becomes part of a recurring skill discovery workflow.
