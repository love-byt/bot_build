"""Bot 客户端 — March7Bot"""

import logging

import discord
from discord import app_commands
from discord.ext import commands

from config import config

log = logging.getLogger(__name__)

# ── 权限 Intents 配置 ──
# - message_content: 读取消息内容（AI 对话需要）
# - members: 获取成员信息（欢迎系统需要）
# - voice_states: 语音状态（点歌需要，预留）
INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.members = True
INTENTS.voice_states = True


class March7Bot(commands.Bot):
    """三月七 Bot 客户端"""

    def __init__(self, proxy: str | None = None) -> None:
        super().__init__(command_prefix="/", intents=INTENTS, proxy=proxy)
        self._synced = False

    async def setup_hook(self) -> None:
        """加载所有 Cog"""
        await self._load_cogs()
        if not self._synced:
            await self.tree.sync()
            self._synced = True
            log.info("✅ Slash 命令已同步")

    async def _load_cogs(self) -> None:
        """加载 cogs 目录下所有 Cog 模块"""
        cogs_list = [
            "src.cogs.utility",   # /ping, /info
            "src.cogs.chat",      # /chat
            "src.cogs.events",    # 事件监听
            # Phase 3+
            # "src.cogs.music",
            # "src.cogs.weather",
            # "src.cogs.search",
            # "src.cogs.interaction",
        ]
        for cog_path in cogs_list:
            try:
                await self.load_extension(cog_path)
                log.info("  ✅ 已加载 Cog: %s", cog_path)
            except Exception as e:
                log.warning("  ⚠️  加载 Cog 失败 %s: %s", cog_path, e)

    async def on_ready(self) -> None:
        """Bot 就绪事件"""
        log.info("=" * 50)
        log.info("🤖 三月七 Bot 已上线！")
        log.info("  用户: %s", self.user)
        log.info("  ID:   %s", self.user.id)
        log.info("  延迟: %.0f ms", self.latency * 1000)
        log.info("=" * 50)

        # 设置状态
        activity = discord.Game(name=config.bot_activity)
        await self.change_presence(activity=activity)

    def run(self) -> None:
        """启动 Bot"""
        super().run(token=config.discord_bot_token, log_handler=None)
