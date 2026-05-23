"""点歌功能 Cog — /点歌（Phase 3 实现）"""

import logging

import discord
from discord import app_commands

log = logging.getLogger(__name__)


class MusicCog(discord.Cog):
    """点歌功能（预留）"""

    def __init__(self, client: discord.Client) -> None:
        self.client = client

    @app_commands.command(name="点歌", description="搜索歌曲（Phase 3 开放）")
    async def play(self, interaction: discord.Interaction, keyword: str) -> None:
        await interaction.response.send_message(
            "🔧 点歌功能正在开发中~ 请期待 Phase 3！",
            ephemeral=True,
        )


async def setup(client: discord.Client) -> None:
    await client.add_cog(MusicCog(client))
