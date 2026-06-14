# AI Agent Knowledge Base

这是一个用于管理 AI 项目、skills、工具、文档和研究笔记的个人知识仓库。目标是让人类长期维护方便，也让 Codex、Claude、ChatGPT、Cursor 等 AI 工具能够快速理解你关注过什么、安装过什么、信任什么、正在评估什么。

## 推荐用法

1. 新项目先放到 `inbox/`，用一句话记录来源和为什么值得看。
2. 评估后把结构化信息写入 `registries/` 对应 JSON 文件。
3. 详细分析、安装过程、风险判断、使用心得放入对应目录的 Markdown 文件。
4. 重要取舍写入 `decisions/`，方便未来 AI 工具理解上下文。
5. 每次变更运行 `python3 scripts/validate_registry.py`，再提交到 GitHub。

## 目录结构

| 路径 | 用途 |
| --- | --- |
| `AGENTS.md` | 给 AI 编码/研究助手的仓库读取规则 |
| `ai-index.md` | 给 AI 工具快速检索的总索引 |
| `registries/` | 结构化清单，适合 AI 和脚本读取 |
| `projects/` | AI 项目、公司、开源仓库、研究方向的详细页 |
| `skills/` | Codex/Claude/ChatGPT 等可安装 skill 或能力包 |
| `tools/` | MCP、CLI、浏览器插件、IDE 插件、服务和工作流工具 |
| `documents/` | 论文、官方文档、教程、报告和规范 |
| `research-notes/` | 调研笔记、比较分析、实验记录 |
| `decisions/` | 长期有效的技术/工具选择记录 |
| `templates/` | 新条目模板 |
| `docs/` | 分类体系、流程、安全策略和发布说明 |

## 核心分类

- `project`: AI 产品、开源项目、模型、框架、研究组织。
- `skill`: 给 AI agent 安装或加载的能力包、提示词包、任务工作流。
- `tool`: MCP server、CLI、SDK、插件、自动化工具、本地服务。
- `document`: 官方文档、论文、教程、规范、报告。
- `research_note`: 调研、对比、测试、复盘和结论。
- `decision`: 为什么采用、拒绝、暂停或替换某个项目或工具。

## 状态字段

统一使用以下状态，便于后续筛选：

- `watching`: 关注中，还没有深入评估。
- `evaluating`: 正在测试或阅读。
- `active`: 已经在使用。
- `paused`: 暂停使用，但未来可能恢复。
- `rejected`: 明确不采用。
- `archived`: 历史资料，不再维护。

## GitHub 发布

本地提交完成后，如果已经有 GitHub 空仓库：

```bash
git remote add origin git@github.com:<your-user>/<repo-name>.git
git push -u origin main
```

如果安装了 GitHub CLI：

```bash
gh auth login
gh repo create ai-agent-knowledge-base --private --source=. --remote=origin --push
```

更详细步骤见 [docs/github-publish.md](docs/github-publish.md)。
