# Tool: SkillsMP

## Summary

- ID: `skillsmp-com`
- Status: `watching`
- Trust level: `medium`
- Website: <https://skillsmp.com/>
- Checked: 2026-06-15
- Source repository: not confirmed
- Type: hosted skill marketplace, directory, REST API, and MCP service

## Purpose

SkillsMP is a hosted community marketplace for SKILL.md-based AI agent skills. It indexes public GitHub skill sources and exposes discovery through web search, categories, creators, repositories, SOC occupation filters, a REST API, and an MCP endpoint.

It is not a single installable skill. In this repository it belongs under `tools` as a discovery and research surface for finding candidate skills.

## Why It Matters

SkillsMP can help find skills to evaluate for Codex, Claude Code, ChatGPT, and other SKILL.md-style agent workflows. It is useful as a map of the skill ecosystem, especially when searching by task, domain, occupation, creator, or repository.

Useful scenarios:

- Search for skills before adding them to `registries/skills.json`.
- Let an agent query skills through REST or MCP.
- Browse creators, repositories, categories, and occupation-based clusters.
- Use public skill pages as a starting point, then return to the source GitHub repository for review.

## Access

Hosted site:

```text
https://skillsmp.com/
```

AI-readable overview:

```text
https://skillsmp.com/index.md
https://skillsmp.com/llms.txt
```

OpenAPI spec:

```text
https://skillsmp.com/openapi.json
```

MCP endpoint:

```text
https://skillsmp.com/mcp
```

MCP manifest:

```text
https://skillsmp.com/.well-known/mcp
```

Observed MCP tools:

- `search_skills`
- `get_skill`
- `list_categories`

## REST API Notes

Base URL:

```text
https://skillsmp.com
```

Search endpoint:

```text
GET /api/v1/skills/search
```

Common parameters:

- `q`: search query
- `page`: page number
- `limit`: result count
- `sortBy`: `stars` or `recent`
- `category`: category slug
- `occupation`: SOC occupation slug

Rate limits stated in docs:

- Anonymous: 50 requests/day, 10 requests/minute, keyword search only.
- Authenticated: 500 requests/day, 30 requests/minute, free API key.

## Evaluation Notes

Read source:

- Homepage HTML metadata.
- `index.md`.
- `llms.txt`.
- `openapi.json`.
- `.well-known/mcp`.
- About page.
- Terms of Service.
- Privacy Policy.
- API docs page.
- `robots.txt`.

Not yet done:

- Confirm whether the site has a public source repository.
- Authenticate and test API key management.
- Connect the MCP endpoint to a local agent.
- Audit individual skills discovered through the marketplace.

## Risks

- Marketplace trust is not skill trust. SkillsMP states that indexed skills are third-party content and should be reviewed before installation.
- The service states it is independent and not affiliated with Anthropic or OpenAI.
- Indexed skills come from public GitHub repositories and each retains its own license.
- Terms say not to scrape or systematically download large portions of the site. Use the documented API and respect rate limits.
- Privacy policy lists analytics and tracking services, including Google Analytics, Microsoft Clarity, and Ahrefs Analytics.
- API keys should be stored in a secret manager or environment variable and never committed.
- Public inventory counts are dynamic and not audit guarantees. Public pages mention 1.7M+ skills, while the MCP manifest observed during review mentioned 900K+ Claude Code skills.

## Usage Guidance

Use SkillsMP for discovery and triage. When a promising skill is found:

1. Open the original GitHub source.
2. Read `SKILL.md`, scripts, references, assets, license, and install commands.
3. Add it to `registries/skills.json` with its own detail page.
4. Keep it as `watching` until installed or tested locally.

Do not treat a SkillsMP listing as proof that a skill is safe, maintained, or suitable for local installation.

## Links

- Website: <https://skillsmp.com/>
- AI overview: <https://skillsmp.com/index.md>
- LLM docs: <https://skillsmp.com/llms.txt>
- API docs: <https://skillsmp.com/docs/api>
- OpenAPI: <https://skillsmp.com/openapi.json>
- MCP endpoint: <https://skillsmp.com/mcp>
- MCP manifest: <https://skillsmp.com/.well-known/mcp>
- About: <https://skillsmp.com/about>
- Terms: <https://skillsmp.com/terms>
- Privacy: <https://skillsmp.com/privacy>

## Next Actions

- [ ] Confirm whether the site code has a public repository and license.
- [ ] Test a low-volume anonymous API search.
- [ ] Test MCP connection only after deciding how to manage rate limits.
- [ ] Use discovered skills as candidates for separate source review.
