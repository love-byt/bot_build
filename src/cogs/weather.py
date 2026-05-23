"""天气查询 Cog — /天气（Phase 3 实现）"""

import logging

import discord
from discord import app_commands

log = logging.getLogger(__name__)


class WeatherCog(discord.Cog):
    """天气查询（预留）"""

    def __init__(self, client: discord.Client) -> None:
        self.client = client

    @app_commands.command(name="天气", description="查询天气（Phase 3 开放）")
    async def weather(self, interaction: discord.Interaction, city: str) -> None:
        await interaction.response.send_message(
            "🔧 天气查询功能正在开发中~ 请期待 Phase 3！",
            ephemeral=True,
        )


async def setup(client: discord.Client) -> None:
    await client.add_cog(WeatherCog(client))
