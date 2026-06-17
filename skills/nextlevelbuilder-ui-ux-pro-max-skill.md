# Skill: UI/UX Pro Max

## Summary

- ID: `nextlevelbuilder-ui-ux-pro-max-skill`
- Status: `watching`
- Trust level: `medium`
- Source: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill>
- Homepage: <https://uupm.cc>
- Checked: 2026-06-17
- Checked commit: `b7e3af80f6e331f6fb456667b82b12cade7c9d35`
- Version observed: `2.5.0`
- Latest tag observed: `v2.5.0`
- npm version checked: `uipro-cli` `2.2.3`
- Default branch: `main`
- License: MIT in root license and package metadata; `cli/README.md` says CC-BY-NC-4.0.

## Purpose

UI/UX Pro Max is a multi-agent design intelligence skill for frontend and product UI work. It provides a searchable rule and data set for style selection, product-specific UI patterns, color palettes, typography, UX quality checks, chart choices, accessibility, and framework-specific implementation guidance.

The key capability is a Python search and design-system generator that can produce a recommended pattern, style, color system, typography, effects, anti-patterns, and delivery checklist from a product query. The npm CLI installs generated skill files into multiple AI coding assistants.

## Why It Matters

This repository tracks AI tools and skills that can improve recurring research and development workflows. UI/UX Pro Max is relevant because it gives AI coding assistants a structured design vocabulary and a local retrieval script instead of relying only on generic design advice.

Useful scenarios:

- Generate a first-pass design system for a landing page, dashboard, SaaS product, admin panel, or mobile app.
- Review UI code for accessibility, spacing, responsive behavior, touch targets, animation, and visual consistency.
- Pick color palettes and typography that fit product category and audience.
- Ask for stack-specific guidance for React, Next.js, Vue, Svelte, Astro, SwiftUI, React Native, Flutter, shadcn/ui, Tailwind, Nuxt, Angular, Laravel, and related stacks.
- Persist generated design-system docs into a project for later AI retrieval.

## Install Or Access

Not installed locally as of 2026-06-17.

Claude Code marketplace:

```text
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

CLI install:

```bash
npm install -g uipro-cli
uipro init --ai codex
```

Equivalent npx form from `skill.json`:

```bash
npx uipro-cli init --ai codex
```

Global Codex install:

```bash
uipro init --ai codex --global
```

Other useful CLI commands:

```bash
uipro versions
uipro update --ai codex
uipro init --ai codex --offline
uipro uninstall --ai codex
```

Observed Codex target:

```text
.codex/skills/ui-ux-pro-max/SKILL.md
```

## Files Or Capabilities

Main reviewed files:

- `README.md`: overview, features, install commands, supported platforms, and examples.
- `skill.json`: metadata with version `2.5.0`, supported platforms, and install command.
- `.claude/skills/ui-ux-pro-max/SKILL.md`: main Claude skill instructions.
- `.claude-plugin/plugin.json`: Claude plugin manifest.
- `src/ui-ux-pro-max/data/`: canonical CSV databases.
- `src/ui-ux-pro-max/scripts/search.py`: main search CLI.
- `src/ui-ux-pro-max/scripts/design_system.py`: design-system generator and persistence logic.
- `cli/package.json`: npm CLI package metadata.
- `cli/src/`: TypeScript installer, updater, uninstaller, GitHub release download helpers, and template renderer.
- `cli/assets/`: bundled data, scripts, and templates used by the installer.

Data inventory observed:

- 67 UI styles.
- 161 color palettes.
- 57 font pairings.
- 99 UX guidelines.
- 25 chart types.
- 161 product reasoning rules.
- 15+ stack guideline CSV files.

Additional Claude skill folders observed:

- `banner-design`
- `brand`
- `design`
- `design-system`
- `slides`
- `ui-styling`
- `ui-ux-pro-max`

## Evaluation Notes

Read source:

- GitHub repository through shallow clone.
- `README.md`
- `skill.json`
- `LICENSE`
- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `.claude/skills/ui-ux-pro-max/SKILL.md`
- `src/ui-ux-pro-max/scripts/search.py`
- `src/ui-ux-pro-max/scripts/design_system.py`
- `cli/package.json`
- `cli/README.md`
- `cli/src/index.ts`
- `cli/src/commands/init.ts`
- `cli/src/commands/update.ts`
- `cli/src/commands/uninstall.ts`
- `cli/src/utils/template.ts`
- `cli/src/utils/github.ts`
- npm registry metadata for `uipro-cli`

GitHub API returned 403 during review, so repository API metadata such as stars and topics was not used. `git ls-remote`, shallow clone content, and npm registry metadata were used instead.

Not yet done:

- Local installation.
- Running `uipro init --ai codex` in a disposable repository.
- Comparing npm package contents against repository HEAD.
- Testing the Python search script.
- Testing `--design-system --persist`.
- Reviewing every auxiliary Claude skill folder in full.
- Verifying exact behavior of global install and uninstall paths.

Suggested first evaluation task:

1. Create a disposable repository.
2. Run `npx uipro-cli init --ai codex --offline` first to avoid remote release download.
3. Inspect generated `.codex/skills/ui-ux-pro-max/`.
4. Run `python3 .codex/skills/ui-ux-pro-max/scripts/search.py "saas dashboard" --design-system`.
5. Test whether `--persist` writes only expected files under `design-system/`.
6. Review generated skill instructions against this repository's existing frontend-design preferences.
7. Decide whether to keep as `watching`, move to `evaluating`, or reject.

## Risks

- Installer commands can write skill files into project-local or global AI assistant directories. Global installs can affect future sessions across projects.
- The npm registry reported `uipro-cli` latest as `2.2.3`, while repository metadata and tag show `2.5.0`. Verify current release state before installing.
- Root `LICENSE` and package metadata say MIT, but `cli/README.md` says CC-BY-NC-4.0. Resolve this inconsistency before redistributing or adapting assets.
- `.claude-plugin/marketplace.json` still reports `2.2.1`, while `skill.json` and `plugin.json` report `2.5.0`.
- The CLI can fetch GitHub releases in legacy/update flows, and GitHub API access may hit rate limits or fail.
- Generated skill instructions can strongly shape design choices and may conflict with an existing product design system.
- `search.py --persist` writes `design-system/MASTER.md` and optional page override files into the current project.
- The repository includes many CSV databases, scripts, templates, TTF font assets, and multiple Claude skill directories. Review license and footprint before active use.
- The search engine is rule/database based. Recommendations still need human review for accessibility, brand fit, and implementation correctness.

## Usage Guidance

Use this skill when the task is materially about UI, UX, visual design, frontend implementation quality, responsive behavior, accessibility, typography, color, charts, animation, or design systems.

Avoid or defer it when:

- The project already has a strict design system and you have not mapped UI/UX Pro Max rules to it.
- The task is backend-only, infrastructure-only, or non-visual automation.
- You need legally clean redistributable assets and have not resolved the MIT vs CC-BY-NC license mismatch.
- You do not want generated files in `.codex/skills/` or `design-system/`.
- You have not tested the installer in a disposable repository.

## Links

- GitHub: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill>
- Homepage: <https://uupm.cc>
- README: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/README.md>
- Main skill: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md>
- Skill metadata: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/skill.json>
- Claude plugin manifest: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude-plugin/plugin.json>
- npm package: <https://www.npmjs.com/package/uipro-cli>
- License: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/LICENSE>

## Next Actions

- [ ] Test `npx uipro-cli init --ai codex --offline` in a disposable repository.
- [ ] Compare npm `uipro-cli` package version with GitHub `v2.5.0`.
- [ ] Resolve the MIT vs CC-BY-NC license mismatch.
- [ ] Run the Python search script on a sample UI task.
- [ ] Decide whether to promote to `evaluating`.
