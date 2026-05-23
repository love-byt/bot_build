"""LLM API 客户端封装 — 支持 DeepSeek（主）和硅基流动（备）"""

import logging
from typing import Optional

from openai import AsyncOpenAI

from config import config

log = logging.getLogger(__name__)


class LLMClient:
    """LLM API 客户端"""

    def __init__(self) -> None:
        self._client: Optional[AsyncOpenAI] = None
        self._model: str = ""
        self._ready = False

    async def initialize(self) -> None:
        """初始化 API 客户端（DeepSeek 优先，硅基流动备选）"""
        if config.is_deepseek_ready:
            self._client = AsyncOpenAI(
                api_key=config.deepseek_api_key,
                base_url=config.deepseek_api_base,
            )
            self._model = config.deepseek_model
            self._ready = True
            log.info("🤖 LLM 客户端已初始化（DeepSeek: %s）", self._model)
        elif config.siliconflow_api_key:
            self._client = AsyncOpenAI(
                api_key=config.siliconflow_api_key,
                base_url=config.siliconflow_api_base,
            )
            self._model = config.siliconflow_model
            self._ready = True
            log.info("🤖 LLM 客户端已初始化（硅基流动: %s）", self._model)
        else:
            log.warning("⚠️  未配置 API Key，AI 对话功能不可用")

    async def chat(
        self,
        messages: list[dict],
        temperature: float = 0.8,
        max_tokens: int = 512,
    ) -> str:
        """发送对话请求"""
        if not self._ready or not self._client:
            return "（AI 服务未配置，暂时无法回复...）"

        try:
            resp = await self._client.chat.completions.create(
                model=self._model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content or ""
        except Exception as e:
            log.error("❌ LLM API 调用失败: %s", e)
            return "（唔...信号不太好，再说一遍？）"

    @property
    def is_ready(self) -> bool:
        return self._ready

    @property
    def model_name(self) -> str:
        return self._model


# 全局单例
llm_client = LLMClient()
