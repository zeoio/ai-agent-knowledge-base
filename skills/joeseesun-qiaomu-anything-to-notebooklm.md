# Skill: Qiaomu Anything to NotebookLM

## Summary

- ID: `joeseesun-qiaomu-anything-to-notebooklm`
- Status: `watching`
- Trust level: `low`
- Source: <https://github.com/joeseesun/qiaomu-anything-to-notebooklm>
- Checked: 2026-06-15
- Checked commit: `cea6ceee8cdcd01a573af5ae75c2d3cffc20650b`
- Default branch: `main`
- License: MIT

## Purpose

Qiaomu Anything to NotebookLM is a Claude Code Skill for collecting content from many sources, converting or fetching it when needed, uploading it to Google NotebookLM, and asking NotebookLM to generate outputs such as podcasts, slide decks, mind maps, quizzes, reports, flashcards, infographics, data tables, and Feishu documents.

The repository positions the skill as a natural-language workflow: the user gives a URL, local file, search query, or mixed set of sources, and the skill decides whether to pass the source directly to NotebookLM, fetch content through scripts/proxies, convert files with `markitdown`, call a transcript API, or run a deeper analysis flow through `main.py`.

## Why It Matters

This is relevant to an AI research workflow because NotebookLM can be useful for digesting papers, articles, videos, podcasts, and document bundles. A reusable agent skill around that flow could reduce manual collecting, converting, uploading, and prompt repetition.

Useful scenarios:

- Turn long PDFs, EPUBs, articles, and notes into NotebookLM-ready sources.
- Generate summaries, audio overviews, slide decks, quizzes, and mind maps from source material.
- Analyze podcasts or video links when transcript access is configured.
- Run a recursive-question analysis workflow over long documents.
- Save finished analysis into Feishu when that integration is configured.

## Install Or Access

Not installed locally as of 2026-06-15.

Upstream install flow:

```bash
cd ~/.claude/skills/
git clone https://github.com/joeseesun/qiaomu-anything-to-notebooklm
cd qiaomu-anything-to-notebooklm
./install.sh
```

NotebookLM authentication required after installation:

```bash
notebooklm login
notebooklm list
```

Optional Get笔记 API configuration for podcast, Bilibili, Xiaoyuzhou, and Ximalaya transcript workflows:

```bash
export GETNOTE_API_KEY="your_api_key"
export GETNOTE_CLIENT_ID="your_client_id"
```

Do not run the installer in a daily environment before reviewing the source and deciding whether the compliance and data-handling risks are acceptable.

Observed installer behavior:

- Checks for Python 3.9 or newer.
- Clones `https://github.com/Bwkyd/wexin-read-mcp.git` into the skill directory if missing.
- Installs Python dependencies from the MCP server and skill `requirements.txt`.
- Installs Playwright Chromium.
- Installs `notebooklm-py` from `https://github.com/teng-lin/notebooklm-py.git` if `notebooklm` is missing.
- Prints a Claude MCP config snippet for `weixin-reader`.
- Requires separate `notebooklm login` authentication.

## Files Or Capabilities

Observed files:

- `SKILL.md`: main skill instructions and source-routing workflow.
- `README.md`: overview, supported sources, installation, examples, and paywall-bypass explanation.
- `install.sh`: dependency installer and MCP setup guidance.
- `requirements.txt`: Python dependencies including `fastmcp`, `playwright`, `beautifulsoup4`, `lxml`, and `markitdown[all]`.
- `main.py`: deep-analysis workflow entry point.
- `scripts/fetch_url.sh`: URL fetcher with proxy cascade and paywall-bypass logic.
- `scripts/get_podcast_transcript.py`: Get笔记 transcript workflow.
- `feishu-read-mcp/`: Feishu-related MCP files.
- `check_env.py`: environment check helper.

Supported sources observed:

- WeChat articles.
- Web pages and paywalled articles.
- YouTube URLs, passed directly to NotebookLM.
- Podcasts, Xiaoyuzhou, Ximalaya, and Bilibili through Get笔记.
- X/Twitter posts.
- PDF, EPUB, Markdown, text, Office files, CSV, JSON, XML, images/OCR, audio files, ZIP archives, and search queries.

## Evaluation Notes

Read source:

- GitHub repository metadata.
- `README.md`
- `SKILL.md`
- `install.sh`
- `requirements.txt`
- `scripts/fetch_url.sh`
- top-level file structure from a shallow clone

Not yet done:

- Local installation.
- Running the installer in a disposable environment.
- Verifying NotebookLM CLI behavior.
- Reviewing `main.py` in full.
- Reviewing the Feishu MCP implementation in full.
- Testing source extraction or generated outputs.

Suggested first evaluation task:

1. Clone into a disposable macOS user or container-like environment.
2. Review `install.sh`, `main.py`, `scripts/fetch_url.sh`, and MCP server code fully.
3. Install without real personal secrets.
4. Authenticate NotebookLM with a low-risk account.
5. Test only on public-domain or personally owned content.
6. Inspect `/tmp`, NotebookLM notebooks, Feishu docs, and shell history for leaked source data or secrets.
7. Decide whether to keep status at `watching`, move to `evaluating`, or reject.

## Risks

- The repository explicitly implements paywall-bypass behavior for many news and media sites. This may violate site terms, copyright, subscription agreements, or local law.
- It collects, transforms, and uploads third-party content to NotebookLM/Google services. Review copyright, privacy, and data-handling constraints before use.
- The installer runs `pip3 install`, installs Playwright Chromium, clones an MCP server, and installs `notebooklm-py` from GitHub.
- WeChat access uses MCP/browser simulation and should be reviewed before granting local browser, account, or filesystem access.
- Optional Get笔记 integration uses `GETNOTE_API_KEY` and `GETNOTE_CLIENT_ID`; these secrets must not be committed.
- Outputs may be written to `/tmp`, Feishu documents, NotebookLM projects, and local generated files.
- Proxy services such as `r.jina.ai`, `defuddle.md`, `archive.today`, and related fetch methods may route requested URLs or content through third-party infrastructure.
- The SKILL says YouTube URLs should be passed directly to NotebookLM and should not be downloaded with `yt-dlp`, Whisper, or browser subtitle extraction.

## Usage Guidance

Use only for low-risk, legally usable source material until the install and data paths are tested. The best initial use case is owned notes, public-domain documents, permissively licensed PDFs, or internal documents that are already approved for NotebookLM.

Avoid it when:

- The source is paywalled, copyrighted, confidential, private, or bound by strict terms.
- You cannot upload the source to NotebookLM or Google services.
- You have not reviewed the install script, MCP server, and paywall-bypass scripts.
- You do not want an agent to use third-party proxy/fetch services.
- You cannot safely manage NotebookLM, Get笔记, Feishu, browser, or MCP credentials.

## Links

- GitHub: <https://github.com/joeseesun/qiaomu-anything-to-notebooklm>
- README: <https://github.com/joeseesun/qiaomu-anything-to-notebooklm/blob/main/README.md>
- SKILL: <https://github.com/joeseesun/qiaomu-anything-to-notebooklm/blob/main/SKILL.md>
- Installer: <https://github.com/joeseesun/qiaomu-anything-to-notebooklm/blob/main/install.sh>
- License: <https://github.com/joeseesun/qiaomu-anything-to-notebooklm/blob/main/LICENSE>

## Next Actions

- [ ] Review `main.py` fully.
- [ ] Review `feishu-read-mcp/` fully.
- [ ] Test in a disposable environment only.
- [ ] Confirm whether NotebookLM and Feishu outputs contain sensitive source text.
- [ ] Decide whether the paywall-bypass behavior makes this unsuitable for active use.
