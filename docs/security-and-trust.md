# Security And Trust

AI tooling often asks for unusually broad permissions: shell access, repository access, browser access, clipboard access, API keys, or local file indexing. Treat every install as a supply-chain decision.

## Before Installing

Check:

- Official source and maintainer identity.
- Installation method and whether it pipes remote scripts into a shell.
- Required permissions.
- Whether it reads local files, browser sessions, credentials, or private repositories.
- License and commercial usage constraints.
- Release activity and issue history.
- How to uninstall or revoke access.

## Risk Notes

Use `risk_notes` in registry entries for short structured warnings. Examples:

- `Requires full repository read access.`
- `Needs API key stored in local environment.`
- `Browser extension can inspect page content.`
- `Install script should be reviewed before execution.`
- `No recent release found at time of review.`

## Trust Levels

Do not treat popularity as trust. A useful tool can still be risky if it has broad permissions, unclear ownership, or weak release hygiene.

- Use `unknown` for new items.
- Use `medium` for tools from known maintainers with reasonable docs.
- Use `high` only after official source review and practical use.
- Use `critical` only for core dependencies where breakage affects daily work.

## Credential Handling

- Never commit API keys, tokens, cookies, SSH keys, private certificates, or `.env` files.
- Keep secret setup instructions in Markdown without revealing values.
- Prefer environment variables or OS keychain storage.
- Record where credentials are managed and how to revoke them.
