"""AI 对话 Cog — /chat（Phase 2 实现）"""

import logging

import discord
from discord import app_commands
from discord.ext import commands

log = logging.getLogger(__name__)


class ChatCog(commands.Cog):
    """AI 对话命令"""

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="chat", description="和三月的聊天（Phase 2 开放）")
    async def chat(self, interaction: discord.Interaction, message: str) -> None:
        """和三月的聊天"""
        await interaction.response.send_message(
            "🔧 对话功能正在准备中，三月七还在学说话~ 请期待 Phase 2！",
            ephemeral=True,
        )


async def setup(client: discord.Client) -> None:
    """加载 Cog"""
    await client.add_cog(ChatCog(client))
    log.info("  ✅ ChatCog 已注册（未激活）")
