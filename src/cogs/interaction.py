"""暧昧互动系统 Cog（Phase 5 实现）"""

import logging

import discord

log = logging.getLogger(__name__)


class InteractionCog(discord.Cog):
    """暧昧互动系统（预留）"""

    def __init__(self, client: discord.Client) -> None:
        self.client = client


async def setup(client: discord.Client) -> None:
    await client.add_cog(InteractionCog(client))
