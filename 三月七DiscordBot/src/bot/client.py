"""
三月七 Discord Bot — Client 核心
"""

import logging

from discord.ext import commands

log = logging.getLogger("march7.bot")


class March7Bot(commands.Bot):
    """三月七 Bot 主客户端"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        """启动时加载所有 Cog"""
        cogs = [
            "src.cogs.ping",
            # Phase 2+
            # "src.cogs.chat",
            # "src.cogs.music",
            # "src.cogs.weather",
            # "src.cogs.search",
            # "src.cogs.interaction",
            # "src.cogs.events",
        ]
        for cog in cogs:
            try:
                await self.load_extension(cog)
                log.info(f"Cog 已加载: {cog}")
            except Exception as e:
                log.warning(f"Cog 加载失败: {cog} — {e}")

        # 同步 Slash Command（开发环境：同步到测试服务器）
        # 上线后改成全局同步
        # await self.tree.sync()
        log.info("三月七 Bot 启动完成！")

    async def on_ready(self):
        log.info(f"已登录为 {self.user} (ID: {self.user.id})")
        log.info(f"当前在 {len(self.guilds)} 个服务器中")
