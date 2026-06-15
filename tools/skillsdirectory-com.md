# Tool: Skills Directory

## Summary

- ID: `skillsdirectory-com`
- Status: `watching`
- Trust level: `medium`
- Website: <https://www.skillsdirectory.com/>
- Checked: 2026-06-15
- Source repository: not confirmed
- Related CLI: `openskills` at <https://github.com/numman-ali/openskills>
- Related CLI license: Apache-2.0
- Type: hosted secure skill directory, API, learning resource, and related CLI ecosystem

## Purpose

Skills Directory is a hosted directory for Claude and agent skills. It positions itself as security-first: the site says skills are scanned for malware, prompt injection, credential theft, data exfiltration, unsafe commands, hidden helpers, and supply-chain risk signals.

It is not a single installable skill. In this repository it belongs under `tools` as a discovery, triage, and security-signal surface for finding candidate skills.

## Why It Matters

This repository tracks AI tools and skills before adoption. Skills Directory is useful because it adds a security-oriented lens to skill discovery. It can help prioritize which skills deserve deeper source review.

Useful scenarios:

- Search for lower-risk Claude or agent skills.
- Filter by security grade, verified status, category, or popularity.
- Review A-F security grading before opening the source repository.
- Learn how to install, write, and compare skills.
- Use the related `openskills` CLI to install or load `SKILL.md` skills across agents.

## Access

Hosted site:

```text
https://www.skillsdirectory.com/
```

Important pages:

- Skills: <https://www.skillsdirectory.com/skills>
- Security overview: <https://www.skillsdirectory.com/security>
- Security methodology: <https://www.skillsdirectory.com/security/methodology>
- API docs: <https://www.skillsdirectory.com/api-docs>
- Learn hub: <https://www.skillsdirectory.com/learn>
- Submit: <https://www.skillsdirectory.com/submit>

## API Notes

The API docs state that all API requests require an API key.

Base URL:

```text
https://www.skillsdirectory.com
```

Observed endpoints:

- `GET /api/v1/skills`
- `GET /api/v1/skills/:slug`
- `GET /api/v1/skills/search`
- `GET /api/v1/categories`
- `GET /api/v1/stats`

Observed free tier:

- 100 requests/day.

Observed paid tiers:

- Pro: 1,000 requests/day.
- Enterprise: 10,000 requests/day.

API keys can be sent with:

```text
Authorization: Bearer <key>
x-api-key: <key>
```

## Related CLI

The site points users toward OpenSkills for installation and loading across coding agents.

NPM package:

```text
openskills
```

Source:

```text
https://github.com/numman-ali/openskills
```

Observed version:

```text
1.5.0
```

Example commands from the OpenSkills README:

```bash
npx openskills install anthropics/skills
npx openskills sync
```

OpenSkills can install from GitHub, local paths, or private repos, and can update `AGENTS.md` with available skills. Review its behavior before running it in an important repository.

## Evaluation Notes

Read source:

- Homepage metadata.
- `robots.txt`.
- `sitemap.xml`.
- Security overview.
- Security methodology.
- API docs.
- About page.
- NPM metadata for `openskills`.
- OpenSkills README and license.

Not yet done:

- Confirm public source repository for the hosted site.
- Create or test an API key.
- Run API queries.
- Install `openskills`.
- Review individual skills discovered through the directory.

## Security Model Observed

The site describes 50+ detection rules across 10 threat categories:

- Execution.
- Network.
- File system.
- Obfuscation.
- Credentials.
- Persistence.
- Prompt injection.
- Data exfiltration.
- Hidden helpers.
- Supply chain.

Observed grade scale:

- A: 90-100.
- B: 75-89.
- C: 60-74.
- D: 40-59.
- F: 0-39.

The site says Grade A skills are shown by default. At review time, its security page displayed 96,863 scanned skills and 92,024 Grade A skills. Treat those as dynamic figures, not fixed inventory.

## Risks

- Static scanning is not proof of safety. The methodology page states scans cannot guarantee intent, correctness, or future repository changes.
- Security grades can help triage, but each skill still needs source, license, script, asset, dependency, and permission review.
- The hosted site source repository was not confirmed during review.
- API access requires keys; do not commit keys.
- Higher-value fields such as full content, security grade/score, semantic search, security findings, and hashes may require paid tiers.
- `robots.txt` disallows `/api/`, `/login`, and `/auth` for crawlers. Use documented API access.
- OpenSkills can install skills into project or global skill directories and update `AGENTS.md`; review commands and target paths before running.

## Usage Guidance

Use Skills Directory as a discovery and risk-triage tool. Do not treat a grade as an approval to install.

Recommended workflow:

1. Use Skills Directory to find candidates and inspect grades.
2. Open the original source repository.
3. Read `SKILL.md`, scripts, references, assets, license, and install instructions.
4. Add the skill to `registries/skills.json` with its own detail page.
5. Keep it as `watching` until installed or tested locally.

## Links

- Website: <https://www.skillsdirectory.com/>
- Skills: <https://www.skillsdirectory.com/skills>
- Security: <https://www.skillsdirectory.com/security>
- Security methodology: <https://www.skillsdirectory.com/security/methodology>
- API docs: <https://www.skillsdirectory.com/api-docs>
- Learn: <https://www.skillsdirectory.com/learn>
- Submit: <https://www.skillsdirectory.com/submit>
- OpenSkills NPM: <https://www.npmjs.com/package/openskills>
- OpenSkills GitHub: <https://github.com/numman-ali/openskills>

## Next Actions

- [ ] Confirm whether the hosted site has public source code and a license.
- [ ] Test one low-volume API query only after deciding where to store the API key.
- [ ] Evaluate `openskills` separately before installing or using it to modify `AGENTS.md`.
- [ ] Add any discovered skills as separate `skill` entries before installation.
