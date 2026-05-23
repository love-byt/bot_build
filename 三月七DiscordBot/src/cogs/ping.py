"""
三月七 Discord Bot — Ping 命令（验证消息链路）
"""

import logging
import time

import discord
from discord import app_commands
from discord.ext import commands

log = logging.getLogger("march7.ping")


class PingCog(commands.Cog):
    """基础命令：ping / info"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="检查 Bot 延迟")
    async def ping(self, interaction: discord.Interaction):
        """检查 Bot 响应延迟"""
        start = time.perf_counter()
        await interaction.response.send_message("Pong! 测量中...")
        end = time.perf_counter()

        ws_latency = round(self.bot.latency * 1000)
        api_latency = round((end - start) * 1000)

        content = (
            f"🏓 Pong!\n"
            f"  WebSocket: `{ws_latency}ms`\n"
            f"  API 往返:  `{api_latency}ms`"
        )
        await interaction.edit_original_response(content=content)

    @app_commands.command(name="info", description="查看 Bot 信息")
    async def info(self, interaction: discord.Interaction):
        """显示 Bot 基本信息"""
        embed = discord.Embed(
            title="三月七 — 星穹列车特派记者",
            description="嗨~咱是三月七！来自星穹列车的摄影师，请多关照！",
            color=discord.Color.from_str("#FFB5C5"),
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.add_field(name="服务器数", value=str(len(self.bot.guilds)), inline=True)
        embed.add_field(name="延迟", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.set_footer(text="📸 不管过去怎样，现在的每一刻都值得记录！")

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(PingCog(bot))
