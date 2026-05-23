"""三月七 Discord Bot — 入口"""

import logging

from config import config
from src.bot.client import March7Bot

# ── 日志 ──
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)-20s | %(levelname)-5s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def main() -> None:
    """启动 Bot"""
    if not config.is_discord_ready:
        log.error("❌ Discord Bot Token 或 App ID 未配置，请检查 .env 文件")
        return

    proxy = config.https_proxy or config.http_proxy
    if proxy:
        log.info("🌐 已配置代理: %s", proxy)

    bot = March7Bot(proxy=proxy if proxy else None)
    bot.run()


if __name__ == "__main__":
    main()
