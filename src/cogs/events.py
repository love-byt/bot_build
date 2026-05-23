"""事件监听 Cog — 入群欢迎等"""

import logging

import discord
from discord.ext import commands

log = logging.getLogger(__name__)


class EventsCog(commands.Cog):
    """事件监听"""

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        """新成员入群欢迎"""
        if member.guild.system_channel is not None:
            welcome = (
                f"嗨嗨~ {member.mention}！欢迎来到服务器！🎉\n"
                "我是三月七，来自星穹列车的摄影爱好者！📸\n"
                "有什么想聊的尽管找我，也可以试试 `/ping` 看看我在不在哦~"
            )
            await member.guild.system_channel.send(welcome)
            log.info("👋 欢迎新成员: %s", member.name)


async def setup(client: discord.Client) -> None:
    """加载 Cog"""
    await client.add_cog(EventsCog(client))
    log.info("  ✅ EventsCog 已注册")
