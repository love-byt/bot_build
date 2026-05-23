# QQ 自动回复机器人

基于 OneBot 协议的 QQ 自动回复机器人。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置 go-cqhttp

1. 下载 go-cqhttp：https://github.com/Mrs4s/go-cqhttp/releases
2. 将 `go-cqhttp.exe` 放在项目目录中
3. 运行 `go-cqhttp.exe` 生成配置文件
4. 修改 `config.yml` 中的 QQ 账号和密码
5. 配置反向 WebSocket 地址为 `ws://127.0.0.1:8080`

## 运行机器人

1. 先启动 go-cqhttp：
   ```bash
   go-cqhttp.exe
   ```

2. 再启动 Python bot：
   ```bash
   python bot.py
   ```

## 自定义回复规则

修改 `bot.py` 中的 `REPLY_RULES` 字典：

```python
REPLY_RULES = {
    "关键词": "回复内容",
    "你好": "你好呀！",
}
```

## 功能说明

- 支持私聊和群聊自动回复
- 关键词触发回复
- 默认回复所有消息
- 日志记录
