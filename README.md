# 三月七 Discord AI 角色机器人

基于 discord.py + DeepSeek API 的崩坏星穹铁道「三月七」AI 角色扮演机器人。

## 功能

- 🎭 **角色扮演** — 完美还原三月七的性格与说话风格
- 💬 **AI 对话** — 接入 DeepSeek V3 大模型，自然交流
- 🧠 **三级记忆** — 短期对话缓存 + 中期用户画像 + 长期 RAG 记忆
- 🎵 **点歌** — 音乐搜索功能
- 🌤️ **天气查询** — 实时天气信息
- 🔍 **联网搜索** — 获取最新信息

## 快速开始

### 1. 前置条件

- Python 3.10+
- Discord Bot Token（[开发者后台](https://discord.com/developers/applications)）
- DeepSeek API Key（[平台](https://platform.deepseek.com/)）

### 2. 安装

```bash
# 克隆仓库
git clone <your-repo-url>
cd march7-bot

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 Token 和 API Key
```

### 3. 启动

```bash
python main.py
```

### 4. Docker 部署

```bash
docker compose up -d
```

## 命令列表

| 命令 | 描述 | 阶段 |
|------|------|------|
| `/ping` | 检查 Bot 延迟 | P1 |
| `/chat 消息` | 和三月的聊天 | P2 |
| `/点歌 歌名` | 搜索歌曲 | P3 |
| `/天气 城市` | 查询天气 | P3 |
| `/搜索 关键词` | 联网搜索 | P3 |
| `/info` | Bot 状态信息 | P3 |
| `/记忆 操作` | 查看/管理记忆 | P4 |
| `/设定 项 值` | 用户个性化设定 | P4 |

## 项目结构

```
march7-bot/
├── main.py              # 入口
├── config.py            # 配置
├── src/
│   ├── bot/             # Bot 客户端
│   ├── cogs/            # 功能模块
│   ├── llm/             # AI 接入层
│   ├── memory/          # 记忆系统
│   └── utils/           # 工具
└── data/                # 数据持久化
```

## 技术栈

- **框架**: discord.py 2.3+ (Slash Commands + Cog)
- **AI**: DeepSeek V3 / 硅基流动
- **数据库**: SQLite → PostgreSQL
- **向量存储**: Chroma (RAG)
- **部署**: Docker + Docker Compose
