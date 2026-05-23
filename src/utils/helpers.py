"""通用辅助函数"""

import logging
import random
import time

log = logging.getLogger(__name__)


def typing_delay(message: str, min_sec: float = 1.0, max_sec: float = 3.0) -> float:
    """模拟打字延迟（按消息长度调整）

    Args:
        message: 回复内容
        min_sec: 最小延迟（秒）
        max_sec: 最大延迟（秒）

    Returns:
        延迟秒数
    """
    base_delay = len(message) * 0.05  # 每字 50ms
    jitter = random.uniform(-0.5, 1.0)
    return max(min_sec, min(base_delay + jitter, max_sec))


def format_timestamp(t: float | None = None) -> str:
    """格式化时间戳"""
    if t is None:
        t = time.time()
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
