"""联网搜索 Cog — /搜索（Phase 3 实现）"""

import logging

import discord
from discord import app_commands

log = logging.getLogger(__name__)


class SearchCog(discord.Cog):
    """联网搜索（预留）"""

    def __init__(self, client: discord.Client) -> None:
        self.client = client

    @app_commands.command(name="搜索", description="联网搜索（Phase 3 开放）")
    async def search(self, interaction: discord.Interaction, keyword: str) -> None:
        await interaction.response.send_message(
            "🔧 搜索功能正在开发中~ 请期待 Phase 3！",
            ephemeral=True,
        )


async def setup(client: discord.Client) -> None:
    await client.add_cog(SearchCog(client))
