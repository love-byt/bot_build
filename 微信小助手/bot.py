"""
QQ 自动回复机器人
基于 OneBot 协议
"""

import asyncio
import websockets
import json
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 自动回复规则
REPLY_RULES = {
    "你好": "你好呀！",
    "在吗": "在的，有什么可以帮你的吗？",
    "hello": "Hello! 你好呀！",
    "hi": "Hi! 你好！",
}

# 默认回复
DEFAULT_REPLY = "我收到你的消息了！"


async def handle_message(data):
    """处理收到的消息"""
    message_type = data.get("message_type")
    user_id = data.get("user_id")
    group_id = data.get("group_id")
    message = data.get("message", "")

    logger.info(f"收到消息: {message} (来自: {user_id})")

    # 查找匹配的回复
    reply = None
    for keyword, response in REPLY_RULES.items():
        if keyword in message:
            reply = response
            break

    if not reply:
        reply = DEFAULT_REPLY

    # 构造回复消息
    reply_data = {
        "action": "send_msg",
        "params": {
            "message_type": message_type,
            "user_id": user_id,
            "group_id": group_id,
            "message": reply
        }
    }

    return reply_data


async def connect_and_listen():
    """连接到 go-cqhttp 并监听消息"""
    uri = "ws://127.0.0.1:8080"

    try:
        async with websockets.connect(uri) as websocket:
            logger.info(f"已连接到 {uri}")

            while True:
                try:
                    message = await websocket.recv()
                    data = json.loads(message)

                    # 处理消息事件
                    if data.get("post_type") == "message":
                        reply_data = await handle_message(data)
                        await websocket.send(json.dumps(reply_data))
                        logger.info(f"已回复: {reply_data['params']['message']}")

                except json.JSONDecodeError:
                    logger.warning(f"无法解析消息: {message}")
                except Exception as e:
                    logger.error(f"处理消息时出错: {e}")

    except Exception as e:
        logger.error(f"连接失败: {e}")
        logger.info("请确保 go-cqhttp 正在运行并配置了反向 WebSocket")


if __name__ == "__main__":
    logger.info("QQ 自动回复机器人启动中...")
    asyncio.run(connect_and_listen())
