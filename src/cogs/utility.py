"""实用工具 Cog — /ping, /info"""

import logging
import time

import discord
from discord import app_commands
from discord.ext import commands

log = logging.getLogger(__name__)


class UtilityCog(commands.Cog):
    """实用工具命令"""

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="ping", description="检查 Bot 的响应延迟")
    async def ping(self, interaction: discord.Interaction) -> None:
        """检查 Bot 延迟"""
        start = time.perf_counter()
        await interaction.response.defer()
        end = time.perf_counter()

        api_latency = round((end - start) * 1000)
        ws_latency = round(self.client.latency * 1000)

        embed = discord.Embed(
            title="🏓 Pong!",
            color=0x87CEEB,
        )
        embed.add_field(name="📡 WebSocket 延迟", value=f"`{ws_latency} ms`", inline=True)
        embed.add_field(name="🔁 API 延迟", value=f"`{api_latency} ms`", inline=True)
        embed.set_footer(text="三月七随时待命~")

        await interaction.followup.send(embed=embed)
        log.info("📊 /ping: API=%dms WS=%dms", api_latency, ws_latency)


async def setup(client: discord.Client) -> None:
    """加载 Cog"""
    await client.add_cog(UtilityCog(client))
    log.info("  ✅ UtilityCog 已注册")
