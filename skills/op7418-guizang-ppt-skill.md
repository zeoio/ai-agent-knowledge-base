# Skill: Guizang PPT Skill

## Summary

- ID: `op7418-guizang-ppt-skill`
- Status: `watching`
- Trust level: `medium`
- Source: <https://github.com/op7418/guizang-ppt-skill>
- Target assistants: Claude Code, Codex, Cursor, and local agents with filesystem and shell access
- Checked: 2026-06-14
- Checked commit: `82fe5ae129e8c2a12e1155fcabed6703342749d6`
- License: AGPL-3.0

## Purpose

Guizang PPT Skill is an agent skill for creating single-file HTML presentation decks. It focuses on horizontal swipe web PPTs, presentation visuals, screenshots, and social cover images.

The skill provides two main visual systems:

- Style A: editorial magazine and electronic ink, suitable for narrative talks and opinion-driven sharing.
- Style B: Swiss international style, suitable for product, data, engineering, method, and technical presentations.

## Why It Matters

This fits the repository's AI workflow because it packages a repeatable presentation-generation process for agents. Instead of only asking an AI to "make slides", the skill supplies templates, layout rules, image prompt guidance, screenshot framing rules, and quality checklists.

Useful scenarios:

- Turn an article, Markdown file, product analysis, or research note into a 6-10 page HTML deck.
- Produce a more designed deck for an internal talk, demo day, product narrative, or AI project explanation.
- Generate matching presentation illustrations or platform covers after the slide structure is stable.

## Install Or Access

Not installed locally as of 2026-06-14.

Official README lists this install command:

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

Manual clone command from the README:

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill
```

Expected files after install:

- `SKILL.md`
- `assets/`
- `references/`
- `scripts/validate-swiss-deck.mjs`

## Capabilities

- Generate single-file HTML decks that can be opened directly in a browser.
- Support keyboard, wheel, touch, dots, and index-style navigation.
- Provide Style A editorial magazine templates and Style B Swiss-style locked layouts.
- Include guidance for image generation, screenshot framing, social covers, and deck QA.
- Include a Swiss deck validator script for stricter layout checks.

## Evaluation Notes

Read source:

- `README.md`
- `SKILL.md`
- GitHub repository metadata

Not yet done:

- Local installation.
- Running the skill in Codex.
- Creating a sample deck.
- Auditing all templates, bundled scripts, and reference files.

Suggested first evaluation task:

1. Install into a disposable skills directory.
2. Generate a short 5-page deck from a non-sensitive Markdown note.
3. Open the generated HTML locally.
4. Run `node scripts/validate-swiss-deck.mjs path/to/index.html` for a Swiss-style deck.
5. Check whether generated HTML imports third-party resources or exposes local/sensitive material.

## Risks

- Third-party skill. Review source before giving it broad local filesystem and shell access.
- Install path targets agent skills directories, so it can influence future agent behavior.
- AGPL-3.0 license should be reviewed before adapting templates or redistributing modified versions.
- Generated HTML decks may include browser runtime behavior, WebGL/canvas, local assets, and CDN fallbacks.
- User-provided screenshots, product data, or private notes may be embedded into generated presentation files.
- Visual quality depends on following the workflow, browser preview, and checklist rather than just generating HTML once.

## Usage Guidance

Use this skill when the user wants a designed web PPT, presentation visuals, or platform cover output, especially for Chinese AI/product/technical content.

Avoid it when:

- The user needs editable PPTX as the primary deliverable.
- The content is dense tabular training material.
- The work requires collaborative editing in PowerPoint or Google Slides.
- The source material contains sensitive information and the generated HTML has not been inspected.

## Links

- GitHub: <https://github.com/op7418/guizang-ppt-skill>
- README: <https://github.com/op7418/guizang-ppt-skill/blob/main/README.md>
- SKILL.md: <https://github.com/op7418/guizang-ppt-skill/blob/main/SKILL.md>
- License: <https://github.com/op7418/guizang-ppt-skill/blob/main/LICENSE>

## Next Actions

- [ ] Decide whether to install for evaluation.
- [ ] If installed, record local path and installed commit.
- [ ] Generate one non-sensitive sample deck.
- [ ] Review generated HTML dependencies and privacy exposure.
- [ ] Reclassify status to `evaluating`, `active`, or `rejected`.
