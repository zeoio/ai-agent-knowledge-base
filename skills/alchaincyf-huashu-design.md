# Skill: Huashu Design

## Summary

- ID: `alchaincyf-huashu-design`
- Status: `watching`
- Trust level: `medium`
- Source: <https://github.com/alchaincyf/huashu-design>
- Target assistants: Claude Code, Codex, Cursor, OpenClaw, Hermes, and other markdown skill-compatible agents
- Checked: 2026-06-14
- Checked commit: `55ff7cc03e0817a39a7987a6331b7eef17faf40c`
- Default branch: `master`
- License: MIT

## Purpose

Huashu Design is an HTML-native design skill for AI agents. It is intended for visual deliverables made with HTML, CSS, JavaScript, React components, Playwright verification, and export scripts.

The skill focuses on:

- High-fidelity app and web prototypes.
- HTML presentation decks and editable PPTX export.
- Timeline-driven motion demos with MP4/GIF export.
- Design direction exploration and variations.
- Infographics and data visualizations.
- 5-dimension expert design reviews.

## Why It Matters

This skill is relevant because it turns design work into an agent-readable workflow. It does not only provide prompts; it includes operating rules, starter components, references, verification steps, export scripts, and anti-slop design constraints.

It is especially useful when the user wants an AI agent to produce a design artifact directly rather than only describe a design direction.

## Install Or Access

Not installed locally as of 2026-06-14.

Official README lists:

```bash
npx skills add alchaincyf/huashu-design
```

Manual clone option:

```bash
git clone https://github.com/alchaincyf/huashu-design.git
```

Observed runtime/export dependencies in `package.json`:

- `pdf-lib`
- `playwright`
- `pptxgenjs`
- `sharp`

## Repository Structure Observed

- `SKILL.md`: main agent instructions and design workflow.
- `README.md`: Chinese README with demos, installation, capabilities, and license notes.
- `README.en.md`: English README.
- `assets/`: starter components, deck engine, device frames, animation helpers, media assets.
- `references/`: task-specific design, animation, deck, export, critique, and workflow references.
- `scripts/`: verification and export scripts for video, PDF, PPTX, thumbnails, and related workflows.
- `demos/`: demonstration artifacts.
- `.env.example`: environment template for optional workflows.

## Capabilities

- Create clickable HTML prototypes for app or web concepts.
- Produce HTML slide decks and export PDF/PPTX variants.
- Build animation demos with Stage/Sprite-style timeline logic.
- Export video and GIF artifacts from HTML motion designs.
- Generate design variations and compare directions.
- Use brand asset protocols for logo, product image, UI screenshot, and color extraction.
- Run structured 5-dimension design critique.
- Verify outputs with browser inspection and Playwright-based tooling.

## Evaluation Notes

Read source:

- `README.md`
- `SKILL.md`
- `LICENSE`
- repository root metadata
- `package.json`

Not yet done:

- Local installation.
- Running the skill in Codex.
- Creating a sample prototype, deck, or animation.
- Auditing all export scripts and large bundled assets.
- Testing generated artifacts in a browser.

Suggested first evaluation task:

1. Install into a disposable skills directory.
2. Ask for a small non-sensitive HTML prototype or 3-page deck.
3. Inspect generated source for external network calls, asset paths, and secrets.
4. Run the recommended browser or Playwright verification.
5. Try one export path only, such as HTML to PDF, before using video/PPTX export workflows.

## Risks

- Third-party skill. Review source before granting broad filesystem, shell, browser, or media-export permissions.
- It can influence future agent behavior once installed into a skills directory.
- Workflows may download brand assets, public images, audio, or external references; each project needs its own source and license check.
- Generated outputs may embed confidential screenshots, private brand materials, customer data, local paths, or API-derived content.
- Optional voiceover and API workflows may require credentials in environment variables; `.env` files must stay local.
- Export tooling depends on Playwright and Node packages, increasing dependency and supply-chain surface.
- Repository is asset-heavy, so install size and update cadence should be evaluated before marking it active.

## Usage Guidance

Use this skill when the goal is a visual artifact:

- HTML prototype.
- HTML deck.
- Motion demo or launch-film-style animation.
- Infographic or visual explanation.
- Design direction exploration.
- Structured design review.

Avoid it when:

- The task is a production web app with backend behavior.
- The user only needs ordinary frontend implementation inside an existing product codebase.
- The project contains sensitive brand/customer assets and no privacy review has been done.
- The user needs a native Figma workflow or layer-level Figma editability as the primary deliverable.

## Links

- GitHub: <https://github.com/alchaincyf/huashu-design>
- README: <https://github.com/alchaincyf/huashu-design/blob/master/README.md>
- SKILL.md: <https://github.com/alchaincyf/huashu-design/blob/master/SKILL.md>
- License: <https://github.com/alchaincyf/huashu-design/blob/master/LICENSE>

## Next Actions

- [ ] Decide whether to install for evaluation.
- [ ] If installed, record local path and installed commit.
- [ ] Generate one non-sensitive sample artifact.
- [ ] Review generated HTML and export scripts before sharing outputs.
- [ ] Reclassify status to `evaluating`, `active`, or `rejected`.
