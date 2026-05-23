"""
三月七 Discord Bot — 入口
"""

import asyncio
import logging

import discord

from config import Config
from src.bot.client import March7Bot

# ── 日志配置 ──────────────────────────────────────────
logging.basicConfig(
    level=logging.DEBUG if Config.DEBUG else logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("march7")


async def main():
    """应用入口"""
    try:
        Config.validate()
    except ValueError as e:
        log.error(e)
        return

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = March7Bot(intents=intents)

    async with bot:
        await bot.start(Config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
