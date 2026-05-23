"""中期记忆 — 用户档案 SQLite（Phase 4 完善）"""

import logging

log = logging.getLogger(__name__)


class MediumTermMemory:
    """中期记忆：用户档案存储（SQLite，Phase 4 实现）"""

    async def initialize(self) -> None:
        """初始化数据库（预留）"""
        pass

    async def get_user_profile(self, user_id: int) -> dict:
        """获取用户档案"""
        return {}

    async def update_user_profile(self, user_id: int, data: dict) -> None:
        """更新用户档案"""
        pass


medium_term_memory = MediumTermMemory()
