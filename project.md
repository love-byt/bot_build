# 三月七 Discord AI 角色机器人

## 项目概述
基于 discord.py + DeepSeek API 的崩坏星穹铁道「三月七」AI 角色扮演机器人。

## 技术栈
- Bot 框架: discord.py 2.3+ (Slash Commands + Cog 模块化)
- AI 模型: DeepSeek V3（主力）/ 硅基流动（备选）
- 数据库: aiosqlite → 后续升级 PostgreSQL
- 向量存储: Chroma (RAG 长期记忆)
- 部署: Docker + Docker Compose

## 项目阶段（12周）

### Phase 1: 地基（第1周）— Discord 上线
- 项目初始化，搭建 discord.py 骨架
- Discord Developer Portal 配置
- Bot 上线，实现 `/ping` 验证

### Phase 2: AI 人设对话（第2-3周）— 三月七能聊天
- DeepSeek API 接入封装
- 加载三月七角色提示词
- 对话管理（上下文窗口、历史缓存）
- 实现 `/chat` Slash Command
- 延迟回复模拟

### Phase 3: 功能插件（第4-5周）— 能干活的 Bot
- `/点歌` 音乐搜索
- `/天气` 天气查询
- `/搜索` 联网搜索
- 入群欢迎系统
- `/info` 工具命令

### Phase 4: 记忆系统（第6-7周）— 有记忆的三月七
- 短期记忆（当前会话缓存）
- 中期记忆（用户档案 SQLite）
- 长期记忆（Chroma RAG 检索）

### Phase 5: 互动与体验（第8-9周）— 有灵魂的 Bot
- 暧昧互动系统（频率控制、话术库）
- 星穹日常素材轮换
- 频率控制与内容安全

### Phase 6: 工业化（第10-12周）— 简历级交付
- 错误处理与日志系统
- Docker 容器化部署
- README 与演示视频
- 简历包装

## 设计原则
- 模块化：每个功能独立 Cog，方便扩展
- 渐进式：从简单到复杂，每阶段都有可交付成果
- 简历导向：每个功能都考虑对求职的价值

## 关键产出
- 完整可运行的 Discord Bot
- 三月七角色扮演 AI 对话
- 三级记忆系统（RAG）
- 功能插件体系（点歌/天气/搜索/入群欢迎）
- Docker 一键部署方案
- 可用于简历的项目描述