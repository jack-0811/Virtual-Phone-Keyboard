from flask import Flask, render_template, request, jsonify
from pynput.keyboard import Controller, Key ,KeyCode
import threading
import os

app = Flask(__name__)
keyboard = Controller()

# 按键映射
KEY_MAPPING = {
    '0': KeyCode.from_vk(96),
    '1': KeyCode.from_vk(97),
    '2': KeyCode.from_vk(98),
    '3': KeyCode.from_vk(99),
    '4': KeyCode.from_vk(100),
    '5': KeyCode.from_vk(101),
    '6': KeyCode.from_vk(102),
    '7': KeyCode.from_vk(103),
    '8': KeyCode.from_vk(104),
    '9': KeyCode.from_vk(105),

    'enter': Key.enter,
    '.': KeyCode.from_vk(110),
    '+': KeyCode.from_vk(107), 
    '-': KeyCode.from_vk(109), 
    '*': KeyCode.from_vk(106), 
    '/': KeyCode.from_vk(111), 

    'backspace': Key.backspace,
    'escape': Key.esc,
    'tab': Key.tab,
    'space': Key.space,
    'up': Key.up,
    'down': Key.down,
    'left': Key.left,
    'right': Key.right,
}

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/keydown', methods=['POST'])
def keydown():
    """处理按下按键事件"""
    try:
        data = request.get_json()
        key = data.get('key', '')
        if key in KEY_MAPPING:
            keyboard.press(KEY_MAPPING[key])
            return jsonify({'status': 'success', 'action': 'down', 'key': key})
        return jsonify({'status': 'error', 'message': 'Invalid key'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/keyup', methods=['POST'])
def keyup():
    """处理松开按键事件"""
    try:
        data = request.get_json()
        key = data.get('key', '')
        if key in KEY_MAPPING:
            keyboard.release(KEY_MAPPING[key])
            return jsonify({'status': 'success', 'action': 'up', 'key': key})
        return jsonify({'status': 'error', 'message': 'Invalid key'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/status')
def status():
    """服务器状态"""
    return jsonify({'status': 'running', 'version': '1.0'})

def get_local_ip():
    """获取本机IP地址"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def start_ngrok():
    """启动ngrok内网穿透（如果已安装）"""
    try:
        from pyngrok import ngrok
        # 启动ngrok隧道
        public_url = ngrok.connect(5000, bind_tls=True)
        print(f"\n{'='*60}")
        print(f"🌐 ngrok公网地址: {public_url}")
        print(f"{'='*60}\n")
        return public_url
    except ImportError:
        print("\n【提示】未安装pyngrok，跳过内网穿透")
        print("如需公网访问，请运行: pip install pyngrok")
        print("或使用其他内网穿透工具（如frp、natapp等）\n")
        return None
    except Exception as e:
        print(f"\n【ngrok错误】{e}")
        print("请确保已注册ngrok并配置authtoken\n")
        return None

if __name__ == '__main__':
    # 获取本地IP
    local_ip = get_local_ip()
    
    print("\n" + "="*60)
    print("手机虚拟键盘服务启动中...")
    print("="*60)
    
    # 尝试启动ngrok
    ngrok_url = start_ngrok()
    
    print("\n📱 访问地址:")
    print(f"   本地访问: http://localhost:5000")
    print(f"   局域网访问: http://{local_ip}:5000")
    if ngrok_url:
        print(f"   公网访问: {ngrok_url}")
    print("\n💡 使用手机浏览器打开以上任一地址即可使用")
    print("="*60 + "\n")
    
    # 启动Flask服务器
    app.run(host='0.0.0.0', port=5000, debug=False)
