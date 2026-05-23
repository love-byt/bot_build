@echo off
chcp 65001
echo ================================
echo QQ 自动回复机器人启动脚本
echo ================================
echo.

echo 1. 启动 go-cqhttp...
start "" "go-cqhttp.exe"

echo 2. 等待 3 秒...
timeout /t 3 /nobreak >nul

echo 3. 启动 Python bot...
python bot.py

pause
