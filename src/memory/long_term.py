"""长期记忆 — Chroma RAG 检索（Phase 4 完善）"""

import logging

log = logging.getLogger(__name__)


class LongTermMemory:
    """长期记忆：语义检索（Chroma，Phase 4 实现）"""

    async def initialize(self) -> None:
        """初始化向量库（预留）"""
        pass

    async def add_memory(self, user_id: int, content: str) -> None:
        """添加记忆"""
        pass

    async def search(self, query: str, top_k: int = 5) -> list[str]:
        """检索相关记忆"""
        return []


long_term_memory = LongTermMemory()
