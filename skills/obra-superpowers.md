# Skill: Superpowers

## Summary

- ID: `obra-superpowers`
- Status: `watching`
- Trust level: `medium`
- Source: <https://github.com/obra/superpowers>
- Checked: 2026-06-15
- Checked commit: `6fd4507659784c351abbd2bc264c7162cfd386dc`
- Version observed: `5.1.0`
- Default branch: `main`
- License: MIT
- Author: Jesse Vincent

## Purpose

Superpowers is a multi-skill software development methodology for coding agents. It packages a set of composable skills and platform-specific plugin manifests so agents can follow structured workflows for brainstorming, planning, implementation, TDD, debugging, code review, parallel/subagent work, worktrees, and branch completion.

It is more than a single skill. It is best understood as a coding-agent workflow system.

## Why It Matters

This repository tracks AI tools and skills that may improve future agent workflows. Superpowers is relevant because it attempts to make coding agents more disciplined and autonomous by giving them a repeatable development process.

Useful scenarios:

- Clarify vague feature ideas before writing code.
- Turn an approved design into a detailed implementation plan.
- Enforce RED-GREEN-REFACTOR TDD.
- Use systematic debugging instead of ad-hoc fixes.
- Request and respond to code review.
- Use git worktrees for isolated development.
- Run subagent-driven development with review checkpoints.

## Install Or Access

Not installed locally as of 2026-06-15.

Claude Code official marketplace:

```text
/plugin install superpowers@claude-plugins-official
```

Claude Code Superpowers marketplace:

```text
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

Codex CLI/App:

```text
Install Superpowers from the official Codex plugin marketplace UI.
```

Factory Droid:

```bash
droid plugin marketplace add https://github.com/obra/superpowers
droid plugin install superpowers@superpowers
```

Gemini CLI:

```bash
gemini extensions install https://github.com/obra/superpowers
gemini extensions update superpowers
```

Cursor:

```text
/add-plugin superpowers
```

GitHub Copilot CLI:

```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

## Repository Structure Observed

- `skills/`: individual `SKILL.md` workflows.
- `.codex-plugin/plugin.json`: Codex plugin manifest.
- `.claude-plugin/plugin.json`: Claude plugin manifest.
- `.cursor-plugin/plugin.json`: Cursor plugin manifest.
- `.opencode/`: OpenCode plugin/install files.
- `gemini-extension.json`: Gemini extension metadata.
- `hooks/`: hook definitions and scripts.
- `tests/`: tests for skill triggering, platform integration, and sync behavior.
- `docs/`: platform docs and design/implementation plans.

## Skills Observed

- `brainstorming`
- `using-git-worktrees`
- `writing-plans`
- `executing-plans`
- `subagent-driven-development`
- `test-driven-development`
- `requesting-code-review`
- `receiving-code-review`
- `finishing-a-development-branch`
- `systematic-debugging`
- `verification-before-completion`
- `dispatching-parallel-agents`
- `writing-skills`
- `using-superpowers`

## Evaluation Notes

Read source:

- `README.md`
- `LICENSE`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `.cursor-plugin/plugin.json`
- `package.json`
- `skills/using-superpowers/SKILL.md`
- repository file structure from a shallow clone

Not yet done:

- Local installation in Codex or another harness.
- Running the plugin on a disposable coding task.
- Reviewing all skills in full.
- Reviewing hooks and platform-specific install behavior in detail.
- Testing how it interacts with this repository's existing `AGENTS.md` and workflow preferences.

Suggested first evaluation task:

1. Install in a disposable project or project-local context.
2. Ask for a small feature change with clear tests.
3. Observe whether brainstorming, planning, TDD, review, and completion behavior are useful or too heavy.
4. Confirm user instructions remain higher priority than Superpowers instructions.
5. Decide whether to promote status to `evaluating` or keep as `watching`.

## Risks

- This is a behavior-shaping workflow system. It can strongly influence how an agent responds, asks questions, writes tests, and performs code review.
- The `using-superpowers` skill tells agents to invoke relevant skills before any response or action. That may add overhead or conflict with a faster local working style.
- TDD and subagent-driven workflows can be beneficial for larger code changes but may be too heavy for small edits.
- Installing into plugin marketplaces or agent skill directories can affect future sessions.
- Hooks and platform-specific adapters should be reviewed before enabling in important repositories.
- User instructions are documented as higher priority than Superpowers skills, but this should be verified in the actual harness.

## Usage Guidance

Use Superpowers when the work benefits from a rigorous coding process:

- Non-trivial feature design.
- Debugging.
- Test-heavy backend or application changes.
- Multi-step refactors.
- Tasks where planning and verification matter more than speed.

Avoid or defer it when:

- The task is a tiny one-off edit.
- The repository already has a strict conflicting workflow.
- The user explicitly asks for a lightweight, direct change.
- There is no time to test how Superpowers changes the agent's behavior.

## Links

- GitHub: <https://github.com/obra/superpowers>
- README: <https://github.com/obra/superpowers/blob/main/README.md>
- Codex plugin manifest: <https://github.com/obra/superpowers/blob/main/.codex-plugin/plugin.json>
- Claude plugin manifest: <https://github.com/obra/superpowers/blob/main/.claude-plugin/plugin.json>
- Cursor plugin manifest: <https://github.com/obra/superpowers/blob/main/.cursor-plugin/plugin.json>
- License: <https://github.com/obra/superpowers/blob/main/LICENSE>
- Release announcement: <https://blog.fsck.com/2025/10/09/superpowers/>

## Next Actions

- [ ] Decide whether to install in a disposable project.
- [ ] Review all skills before making it active.
- [ ] Review hooks and generated files per target harness.
- [ ] Test a small feature implementation and compare process overhead.
- [ ] Reclassify as `evaluating`, `active`, or `rejected`.
