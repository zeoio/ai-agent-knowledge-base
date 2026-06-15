# Tool: Memanto

## Summary

- ID: `moorcheh-ai-memanto`
- Status: `watching`
- Trust level: `medium`
- Tool type: persistent agent memory CLI, REST API, UI, and MCP integration
- Source: <https://github.com/moorcheh-ai/memanto>
- Homepage: <https://memanto.ai>
- Docs: <https://docs.memanto.ai>
- Checked: 2026-06-15
- Checked commit: `262db90e30b34444ae49e5aef66be6d689607493`
- Version observed: `0.2.0`
- MCP package observed: `memanto-mcp` `0.1.0`
- Default branch: `main`
- License: MIT

## Purpose

Memanto is an open-source persistent semantic memory layer for AI agents. It gives agents three main operations: `remember`, `recall`, and `answer`, with typed memories for facts, preferences, instructions, decisions, goals, events, artifacts, errors, and related long-term context.

The main install surface is a Python CLI package. It can run in a local/on-prem setup managed through Docker and Ollama, or in a cloud setup backed by Moorcheh's hosted semantic engine. It also exposes a local REST API, a browser UI, agent connection commands, and a separate MCP server package.

## Why It Matters

This repository tracks tools that can improve AI research and agent workflows. Memanto is relevant because memory is one of the main weak points in recurring AI use: agents forget project decisions, user preferences, task history, and lessons after context resets.

Useful scenarios:

- Preserve stable user and project preferences across Codex, Claude Code, Cursor, and other agent sessions.
- Store technical decisions and recall them before changing architecture.
- Keep debugging lessons, recurring errors, and project conventions available across time.
- Upload documents into an agent memory namespace for later semantic recall.
- Use MCP memory tools in clients that support Model Context Protocol.

## Install Or Access

Not installed locally as of 2026-06-15.

Main CLI install:

```bash
pip install memanto
memanto
```

Interactive setup options observed:

- On-prem: choose `On-Prem`, with Docker and Ollama used for local services.
- Cloud: choose `Cloud`, then provide a Moorcheh API key from <https://console.moorcheh.ai/api-keys>.

Common commands:

```bash
memanto status
memanto agent create my-agent
memanto remember "User prefers concise answers" --type preference
memanto recall "communication style"
memanto answer "What does the user prefer?"
memanto upload notes.md
memanto serve
memanto ui
```

Agent integration examples:

```bash
memanto connect claude-code
memanto connect codex
memanto connect codex --project-dir ./my-project
memanto connect codex --global
```

MCP server install:

```bash
pip install memanto-mcp
```

Example MCP environment variables:

```bash
export MOORCHEH_API_KEY="your_api_key"
export MEMANTO_DEFAULT_AGENT_ID="codex-research"
```

## Configuration

Local config paths observed:

- `~/.memanto/config.yaml`: CLI configuration, active agent/session, server settings, encrypted API key metadata.
- `~/.memanto/.key`: Fernet key for decrypting local config values.
- `.env`: local environment file for Docker or server deployment; should remain untracked.

Important commands and behavior:

- `memanto config show`: inspect config.
- `memanto config backend`: switch between local and cloud backend.
- `memanto agent delete`: can keep or purge cloud memories, depending on prompt choices.
- `memanto connect remove ...`: remove agent integration.
- `memanto memory export` and `memanto memory sync`: export/sync structured memory files such as `MEMORY.md`.

Agent integration behavior observed from source:

- Codex uses `AGENTS.md`, `.agents/skills`, and `~/.codex/skills`.
- Claude Code uses `CLAUDE.md`, `.claude/skills`, `~/.claude/skills`, and may add session-start hooks plus `Bash(memanto:*)` permissions.
- Cursor uses `.cursor/rules/memanto.mdc` and `.cursor/skills`.
- Other integrations include Windsurf, Antigravity, Gemini CLI, Cline, Continue, OpenCode, Goose, Roo, GitHub Copilot, and Augment.

## MCP Notes

The `memanto-mcp` package exposes memory tools:

- `remember`
- `batch_remember`
- `recall`
- `recall_recent`
- `recall_as_of`
- `recall_changed_since`
- `answer`

Optional admin tools are exposed when `MEMANTO_EXPOSE_ADMIN=true`:

- `create_agent`
- `list_agents`
- `get_agent`
- `delete_agent`

MCP transports observed:

- `stdio`
- `sse`
- `streamable-http`

The MCP README states that HTTP/SSE deployments need a reverse proxy and auth for production because the server authenticates to Moorcheh upstream but does not authenticate inbound MCP clients.

## Evaluation Notes

Read source:

- GitHub repository metadata.
- `README.md`
- `SECURITY.md`
- `pyproject.toml`
- `docs/CLI_INSTALLATION.md`
- `docs/CLI_USER_GUIDE.md`
- `docs/AGENT_INTEGRATION_GUIDE.md`
- `integrations/mcp/README.md`
- `integrations/mcp/pyproject.toml`
- `memanto/cli/connect/agent_registry.py`
- `memanto/cli/connect/templates.py`
- `memanto/cli/commands/connect.py`
- `docker-compose.yml`
- `.env.example`
- PyPI metadata for `memanto` and `memanto-mcp`

Not yet done:

- Local installation.
- Running on-prem Docker/Ollama setup.
- Creating a cloud Moorcheh API key.
- Testing `memanto connect codex` in a disposable repository.
- Inspecting exactly what files are changed by every connection target.
- Testing deletion and cloud memory purge behavior.
- Reviewing the full REST API and UI implementation.

Suggested first evaluation task:

1. Create a disposable repository.
2. Install with `pipx install memanto` or a temporary virtual environment.
3. Use on-prem mode first if Docker/Ollama resources are acceptable.
4. Run `memanto connect codex --project-dir <disposable-repo>`.
5. Review changes to `AGENTS.md`, `.agents/skills`, and any config files before reusing.
6. Store only non-sensitive test memories.
7. Test recall, conflict handling, `memory export`, `memory sync`, and removal.
8. Decide whether this should become `evaluating`.

## Risks

- Memanto is designed to persist memory across agent sessions. This can include private preferences, project facts, implementation decisions, uploaded document content, errors, source-derived artifacts, and user instructions.
- Cloud mode sends memory and uploaded file content to Moorcheh services. Confirm privacy, retention, deletion, and compliance requirements before storing sensitive data.
- Local/on-prem mode still creates local services, containers, volumes, models, ports, and configuration files that need review.
- `memanto connect` modifies agent instruction files, skill directories, hooks, and permissions. Global connection commands can affect future sessions across projects.
- The CLI stores local config and session data under `~/.memanto/`; never commit `config.yaml`, `.key`, `.env`, API keys, or session tokens.
- Security docs mention Moorcheh API keys beginning with `mk_`, while MCP docs use `mch_` placeholders. Treat all Moorcheh-looking tokens as secrets.
- MCP HTTP/SSE transport can expose memory tools over a network. Do not bind it broadly without reverse proxy authentication.
- Memory poisoning is a real operational risk: stale, incorrect, overconfident, or malicious memories can influence future agent behavior.
- The `answer` command may use configured LLM models over stored memory context; verify provider routing before storing private material.
- Repository classifiers mark the main package as alpha, even though some docs say production-ready.

## Usage Guidance

Use Memanto only after deciding what should be remembered and what should not. A good first policy is to store stable workflow preferences, public project conventions, explicit decisions, and non-sensitive debugging lessons.

Avoid or defer it when:

- The repo or workspace contains secrets, customer data, private source context, or regulated data.
- You have not reviewed how `memanto connect` changes local or global agent instructions.
- You cannot verify where cloud memories are stored and how they are deleted.
- You need strict reproducibility and do not want agent behavior shaped by persistent memory.
- You cannot audit who has access to the Moorcheh API key, MCP endpoint, or local memory files.

## Links

- GitHub: <https://github.com/moorcheh-ai/memanto>
- Homepage: <https://memanto.ai>
- Docs: <https://docs.memanto.ai>
- PyPI package: <https://pypi.org/project/memanto/>
- MCP PyPI package: <https://pypi.org/project/memanto-mcp/>
- MCP README: <https://github.com/moorcheh-ai/memanto/blob/main/integrations/mcp/README.md>
- Security: <https://github.com/moorcheh-ai/memanto/blob/main/SECURITY.md>
- Paper: <https://arxiv.org/abs/2604.22085>
- License: <https://github.com/moorcheh-ai/memanto/blob/main/LICENSE>

## Next Actions

- [ ] Test `pip install memanto` in a disposable Python environment.
- [ ] Test on-prem mode separately from cloud mode.
- [ ] Run `memanto connect codex` only in a disposable repository first.
- [ ] Inspect generated or modified `AGENTS.md`, skill folders, and config files.
- [ ] Define a personal policy for what memories are safe to store.
- [ ] Decide whether to move status from `watching` to `evaluating`.
