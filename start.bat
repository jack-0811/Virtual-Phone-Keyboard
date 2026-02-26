@echo off
chcp 65001 >nul
echo ========================================
echo 手机虚拟键盘服务启动器
echo ========================================
echo.

REM 检查Python是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python 3.7+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/2] 检查并安装依赖包...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo [警告] 安装依赖时出现问题，尝试继续运行...
)

echo.
echo [2/2] 启动服务器...
echo.

python app.py

if errorlevel 1 (
    echo.
    echo [错误] 服务器启动失败
    pause
    exit /b 1
)

pause
