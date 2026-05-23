"""
三月七 Discord Bot — 配置管理
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """应用配置，从环境变量读取"""

    # Discord
    DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")

    # DeepSeek
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_BASE_URL: str = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    DEEPSEEK_MODEL: str = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    # Bot 设置
    COMMAND_PREFIX: str = os.getenv("COMMAND_PREFIX", "/")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

    # 对话设置
    MAX_HISTORY: int = int(os.getenv("MAX_HISTORY", "20"))       # 最大历史轮数
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "2048"))       # 最大生成长度
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.8"))  # 创造力

    # 频率限制
    RATE_LIMIT_PER_CHANNEL: int = int(os.getenv("RATE_LIMIT_PER_CHANNEL", "3"))  # 条/分钟/频道
    RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))            # 窗口秒数

    @classmethod
    def validate(cls):
        """验证必要配置"""
        missing = []
        if not cls.DISCORD_TOKEN:
            missing.append("DISCORD_TOKEN")
        if not cls.DEEPSEEK_API_KEY:
            missing.append("DEEPSEEK_API_KEY")
        if missing:
            raise ValueError(f"缺少必要环境变量: {', '.join(missing)}")
