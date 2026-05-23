# 三月七 Discord Bot — 开发计划

> 崩坏：星穹铁道「三月七」角色扮演 AI 机器人 · Discord 版
> 基于 discord.py 2.3+ · Slash Commands · DeepSeek

---

## 一、为什么换 Discord


| 对比项      | QQ Bot            | Discord Bot                                  |
| -------- | ----------------- | -------------------------------------------- |
| **封号风险** | 极高（腾讯持续打压第三方协议）   | 零风险（官方 API）                                  |
| **开发效率** | 低（NoneBot2 插件体系重） | 高（discord.py 成熟稳定）                           |
| **交互能力** | 文本为主              | Slash Command / Button / Modal / Select Menu |
| **简历价值** | 一般                | **高**（游戏公司标配社群平台）                            |
| **可扩展性** | 受限于协议             | Discord App 生态，上限极高                          |
| **学习收益** | QQ Bot 技能通用性低     | Discord Bot + API 设计通用性强                     |


你的三月七 prompt 所有内容（人设、记忆、功能指令）**100% 可迁移**到 Discord，迁移成本几乎为零。

---

## 二、技术选型


| 层级           | 选型                              | 理由                             |
| ------------ | ------------------------------- | ------------------------------ |
| **Bot 框架**   | discord.py 2.3+                 | 最成熟 Python Discord 库，文档完善，社区活跃 |
| **命令系统**     | Slash Commands (`app_commands`) | Discord 推荐的现代交互方式              |
| **项目组织**     | Cog 模块化                         | 每个功能独立文件，好维护好扩展                |
| **AI 模型**    | **DeepSeek V3**（主） / 硅基流动（备） | 中文能力强，成本极低，兼容 OpenAI SDK |
| **HTTP 客户端** | openai (AsyncOpenAI)              | DeepSeek 原生支持 OpenAI SDK 格式 |
| **数据库**      | aiosqlite → PostgreSQL          | 先从轻量 SQLite 开始，后期可升级           |
| **向量存储**     | Chroma                          | RAG 语义记忆检索                     |
| **配置管理**     | python-dotenv (.env)            | 敏感信息不写进代码                      |
| **部署**       | Docker + Docker Compose         | 一键部署，环境隔离                      |


---

## 三、项目结构

```
march7-bot/
├── main.py                    # 入口：启动 Bot
├── config.py                  # 配置读取 (.env)
├── .env.example               # 环境变量模板
├── requirements.txt           # 依赖
├── docker-compose.yml         # Docker 编排
├── Dockerfile                 # 容器化
├── README.md
│
├── src/
│   ├── __init__.py
│   │
│   ├── bot/
│   │   ├── __init__.py
│   │   └── client.py          # Bot 客户端设置（Intents、Tree、同步）
│   │
│   ├── cogs/                  # 各功能模块（Cog）
│   │   ├── __init__.py
│   │   ├── chat.py            # AI 对话核心（三月七人设）
│   │   ├── music.py           # 点歌功能
│   │   ├── weather.py         # 天气查询
│   │   ├── search.py          # 联网搜索
│   │   ├── utility.py         # 实用工具
│   │   ├── interaction.py     # 暧昧/互动系统
│   │   └── events.py          # 事件监听（欢迎、状态等）
│   │
│   ├── llm/                   # AI 接入层
│   │   ├── __init__.py
│   │   ├── client.py          # LLM API 封装（Claude/GPT-4）
│   │   ├── prompts.py         # 三月七完整角色提示词
│   │   └── managers.py        # 对话管理（历史窗口、Token 控制）
│   │
│   ├── memory/                # 记忆系统
│   │   ├── __init__.py
│   │   ├── short_term.py      # 短期记忆（当前会话缓存）
│   │   ├── medium_term.py     # 中期记忆（用户档案 SQLite）
│   │   └── long_term.py       # 长期记忆（Chroma RAG 检索）
│   │
│   └── utils/                 # 工具
│       ├── __init__.py
│       └── helpers.py         # 通用辅助函数
│
└── data/                      # 数据持久化
    ├── memory.db              # SQLite 数据库
    └── chroma/                # Chroma 向量存储
```

---

## 四、分阶段计划（12 周）

### Phase 1：地基（第1周）— Discord 上线

**目标：** Bot 能上线，响应 Slash Command


| #   | 任务            | 内容                                         | 产出      |
| --- | ------------- | ------------------------------------------ | ------- |
| 1.1 | 项目初始化         | 创建项目骨架，装 discord.py，配置 .env                | 项目就绪    |
| 1.2 | Discord 开发者后台 | 创建 Application，配 Bot Token 和 Intents       | Bot 可邀请 |
| 1.3 | Bot 核心        | main.py + client.py，实现启动和 Slash Command 同步 | Bot 在线  |
| 1.4 | 第一个命令         | `/ping` — 确认收发链路通                          | 验证通过    |


**学习资料：**

- [discord.py 官方文档](https://discordpy.readthedocs.io/)
- Discord Developer Portal：[https://discord.com/developers/applications](https://discord.com/developers/applications)

---

### Phase 2：AI 人设对话（第2-3周）— 三月七上线

**目标：** `/chat 消息` — 三月七用她的口吻跟你聊天


| #   | 任务         | 内容                             | 产出      |
| --- | ---------- | ------------------------------ | ------- |
| 2.1 | LLM 接入     | 封装 DeepSeek API 客户端（AsyncOpenAI） | API 就绪  |
| 2.2 | Prompt 系统  | 加载三月七角色提示词到 System Prompt      | 人设注入    |
| 2.3 | 对话管理       | 上下文窗口、历史缓存、Token 使用控制          | 多轮对话    |
| 2.4 | `/chat` 命令 | 创建 Chat Cog，实现 Slash Command   | AI 对话可用 |
| 2.5 | 延迟模拟       | 按 prompt 规则模拟思考延迟 + typing 状态  | 拟人体验    |


**关键实现思路：**

```
用户发送 /chat 你好
  → Bot 显示 "三月七正在输入..."
  → 延迟 3-15 秒（按规则随机）
  → DeepSeek API 调用（system=角色prompt + messages=历史）
  → 返回符合三月七风格的简短回复
  → 存储到对话历史
```

---

### Phase 3：功能插件（第4-5周）— 能干活的 Bot


| #   | 任务         | 内容                          | 产出   |
| --- | ---------- | --------------------------- | ---- |
| 3.1 | `/点歌 歌名`   | 调用音乐搜索 API，返回歌曲链接/信息        | 点歌功能 |
| 3.2 | `/天气 城市`   | 接入和风天气 / OpenWeatherMap API | 天气查询 |
| 3.3 | `/搜索 关键词`  | 调用搜索 API，按简短/详细格式输出         | 联网搜索 |
| 3.4 | 欢迎系统       | 新成员加入时触发三月七风格欢迎语            | 入群欢迎 |
| 3.5 | `/info` 工具 | 查看 Bot 状态、延迟、版本信息           | 工具命令 |


---

### Phase 4：记忆系统（第6-7周）— 有记忆的三月七

**目标：** 三月七记得你是谁、聊过什么、喜欢什么


| 层级     | 实现方案                 | 存储内容                     |
| ------ | -------------------- | ------------------------ |
| **短期** | 内存 dict（滑动窗口，最近 N 轮） | 当前对话上下文                  |
| **中期** | SQLite（aiosqlite）    | 用户档案：昵称、互动次数、偏好话题、上次对话时间 |
| **长期** | Chroma 向量库           | 对话摘要 embedding 存储，语义检索   |


**关键机制（RAG 流程）：**

```
对话进行中
  → 每次对话结束，小模型生成摘要
  → 摘要向量化存入 Chroma
  → 下次对话时，检索相关记忆
  → 注入到 DeepSeek 的 System Prompt 中
```

---

### Phase 5：互动与体验（第8-9周）— 有灵魂的 Bot


| #   | 任务         | 内容                      |
| --- | ---------- | ----------------------- |
| 5.1 | 暧昧互动系统     | 按 prompt 规则的触发词/时机/频率实现 |
| 5.2 | 星穹日常素材轮换   | 定时插入列车组日常话题             |
| 5.3 | 频率控制       | 防 spam：3条/分钟/频道         |
| 5.4 | Token 用量追踪 | 监控每日 Token 消耗           |


---

### Phase 6：工业化（第10-12周）— 简历级交付


| #   | 任务         | 内容                              | 产出    |
| --- | ---------- | ------------------------------- | ----- |
| 6.1 | 错误处理       | 全局异常捕获、API 重试、优雅降级              | 稳定运行  |
| 6.2 | 日志系统       | 分级日志、日志文件轮转                     | 可观测   |
| 6.3 | Docker 化   | Dockerfile + docker-compose.yml | 一键部署  |
| 6.4 | README 与演示 | 写 README、录演示 GIF/视频             | 简历素材  |
| 6.5 | 可选：Web 控制台 | 简单的管理后台（Streamlit / FastAPI）    | 可视化管理 |


---

## 五、Bot 指令一览


| 命令         | 描述        | 阶段  |
| ---------- | --------- | --- |
| `/ping`    | 检查 Bot 延迟 | P1  |
| `/chat 消息` | 和三月的聊天    | P2  |
| `/点歌 歌名`   | 搜索歌曲      | P3  |
| `/天气 城市`   | 查询天气      | P3  |
| `/搜索 关键词`  | 联网搜索      | P3  |
| `/info`    | Bot 状态信息  | P3  |
| `/记忆 操作`   | 查看/管理记忆   | P4  |
| `/设定 项 值`  | 用户个性化设定   | P4  |


---

## 六、模型与成本预估


| 阶段   | 模型                          | Token 用量/月     | 预估费用  |
| ---- | --------------------------- | -------------- | ------- |
| 开发测试 | DeepSeek V3（主） / 硅基流动（备） | ~5M tokens     | ~$1-3   |
| 正式运行 | DeepSeek V3                 | ~20-50M tokens | ~$3-10  |
| （备选） | 硅基流动免费模型                 | ~20-50M tokens | 免费/极低 |


DeepSeek 中文能力强、价格低，作为主力模型；如果想尝试其他风格可切 Claude。

---

## 七、简历写法

```
三月七 AI 角色机器人 | discord.py + DeepSeek API + Chroma RAG
https://github.com/你的名字/march7-bot

- 在 Discord 平台实现了崩坏星穹铁道「三月七」AI 角色扮演机器人
- 基于 DeepSeek 大模型，精确还原角色性格与说话风格
- 设计三级记忆系统：短期对话缓存 + 中期用户画像 + 长期向量 RAG 检索
- 实现拟人化交互（延迟回复、主动话题、暧昧互动触发机制）
- 模块化 Cog 架构，支持热插拔功能插件
- Docker 容器化部署，日均处理 1000+ 消息
```

**投递方向：** 游戏公司 AI 工具开发 / 社群运营工具 / 游戏平台技术运营

---

## 八、Phase 1 拆解

### 第1周：地基（可执行任务）

**Day 1：项目初始化**

- [ ] `mkdir march7-bot && cd march7-bot`
- [ ] `pip install discord.py python-dotenv openai`
- [ ] 创建 `main.py` + `config.py` + `.env`
- [ ] 在 Discord Developer Portal 创建 Application，拿到 Token
- [ ] 邀请 Bot 到你的测试服务器

**Day 2：Bot 核心**

- [ ] 实现 Client 启动、Intents 配置
- [ ] 创建 Cog 目录结构
- [ ] 实现 `/ping` Slash Command

**Day 3：调试与验证**

- [ ] 确保 Bot 24小时在线（本地测试）
- [ ] 确保 Slash Command 在所有频道可用
- [ ] 基础错误处理

**开始前需要：**

1. 一个 Discord 账号
2. 一个自己的 Discord 服务器（测试用）
3. 一个 DeepSeek API Key（https://platform.deepseek.com/）

---

> **下一步：** 确认计划后，转化为长期项目，从 Phase 1 Day 1 开始拉任务。

&nbsp;