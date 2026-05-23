"""配置管理 — 从 .env 读取配置"""

import os
from dataclasses import dataclass, field
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    # Discord
    discord_bot_token: str = field(default_factory=lambda: os.getenv("DISCORD_BOT_TOKEN", ""))
    discord_app_id: str = field(default_factory=lambda: os.getenv("DISCORD_APP_ID", ""))

    # DeepSeek
    deepseek_api_key: str = field(default_factory=lambda: os.getenv("DEEPSEEK_API_KEY", ""))
    deepseek_api_base: str = field(default_factory=lambda: os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com/v1"))
    deepseek_model: str = field(default_factory=lambda: os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))

    # 硅基流动
    siliconflow_api_key: str = field(default_factory=lambda: os.getenv("SILICONFLOW_API_KEY", ""))
    siliconflow_api_base: str = field(default_factory=lambda: os.getenv("SILICONFLOW_API_BASE", "https://api.siliconflow.cn/v1"))
    siliconflow_model: str = field(default_factory=lambda: os.getenv("SILICONFLOW_MODEL", "Qwen/Qwen2-7B-Instruct"))

    # Proxy（国内访问 Discord 需要）
    http_proxy: str = field(default_factory=lambda: os.getenv("HTTP_PROXY", ""))
    https_proxy: str = field(default_factory=lambda: os.getenv("HTTPS_PROXY", ""))

    # Bot
    bot_prefix: str = field(default_factory=lambda: os.getenv("BOT_PREFIX", "/"))
    bot_activity: str = field(default_factory=lambda: os.getenv("BOT_ACTIVITY", "📸 今天去拍点什么呢~"))

    @property
    def is_discord_ready(self) -> bool:
        return bool(self.discord_bot_token and self.discord_app_id)

    @property
    def is_deepseek_ready(self) -> bool:
        return bool(self.deepseek_api_key)


config = Config()
