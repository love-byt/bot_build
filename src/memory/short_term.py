"""短期记忆 — 当前会话缓存（Phase 2 完善）"""

import logging
from collections import defaultdict
from collections.abc import Generator
from dataclasses import dataclass, field

log = logging.getLogger(__name__)


@dataclass
class SessionEntry:
    role: str
    content: str


class ShortTermMemory:
    """短期记忆：当前会话的消息缓存（滑动窗口）"""

    MAX_TOKENS = 2048  # 粗略 token 上限

    def __init__(self) -> None:
        self._sessions: defaultdict[int, list[SessionEntry]] = defaultdict(list)

    def add(self, user_id: int, role: str, content: str) -> None:
        self._sessions[user_id].append(SessionEntry(role=role, content=content))
        self._trim(user_id)

    def get(self, user_id: int, limit: int = 10) -> list[SessionEntry]:
        return self._sessions[user_id][-limit:]

    def clear(self, user_id: int) -> None:
        self._sessions.pop(user_id, None)

    def _trim(self, user_id: int) -> None:
        """粗略的 token 裁剪"""
        # 简化为按条数裁剪，Phase 2 实现精确 token 计数
        while len(self._sessions[user_id]) > 50:
            self._sessions[user_id].pop(0)


short_term_memory = ShortTermMemory()
