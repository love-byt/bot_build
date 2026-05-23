"""对话管理 — 上下文窗口、历史缓存、Token 控制（Phase 2 完善）"""

import logging
from collections import deque
from typing import Optional

log = logging.getLogger(__name__)


class ConversationManager:
    """对话管理器，管理每个用户的对话历史"""

    MAX_HISTORY = 10  # 每个用户最多保留 10 轮对话

    def __init__(self) -> None:
        # {user_id: deque of {role, content}}
        self._histories: dict[int, deque[dict]] = {}

    def get_history(self, user_id: int) -> list[dict]:
        """获取用户的历史消息"""
        history = self._histories.get(user_id)
        if history is None:
            return []
        return list(history)

    def add_message(self, user_id: int, role: str, content: str) -> None:
        """添加一条消息到历史"""
        if user_id not in self._histories:
            self._histories[user_id] = deque(maxlen=self.MAX_HISTORY)
        self._histories[user_id].append({"role": role, "content": content})

    def clear_history(self, user_id: int) -> None:
        """清除用户的历史"""
        self._histories.pop(user_id, None)

    @property
    def active_users(self) -> int:
        return len(self._histories)


# 全局单例
conversation_manager = ConversationManager()
