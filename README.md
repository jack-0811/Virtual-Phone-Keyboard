# 📱 Phone Virtual Keyboard
Turn your phone into a wireless numpad for your PC! Connect via the web to control your computer's input using your phone's screen.
Mainly because I don't have numpad on my keyboard and I really need it in some situation (like gaming/working softwares)

## ✨ Features

-  **Digital numpad** - Includes 0-9, decimal point, backspace, and enter. Perfect for fixing the "missing numpad" problem on 86-key mechanical keyboards.
-  **Wireless** - Connects over WiFi. No cables needed.
-  **Real-time** - Instant response with low latency.
-  **Tunneling** - Supports public access via ngrok

## 📋 System requirements

- Windows 7/10/11
- Python 3.7 or higher
- Phone and PC connected to the same WiFi

## 🚀 Quick Start

### Method 1: One-click Start (Recommended)

1. Double-click `start.bat`
2. Wait for the server to launch.
3. Open the displayed address on your phone's browser or scan the QR Code.

### Method 2: Manual Setup

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Start the server**
```bash
python app.py
```

3. **Access from phone**

### Public Access (via ngrok)

If you need to access the keyboard from a different network:

1. **Install ngrok**
```bash
pip install pyngrok
```

2. **Register & Configure ngrok**
   - Sign up at https://ngrok.com/
   - Get your auth token.
   - Run the config command:
   ```bash
   ngrok authtoken YOUR_AUTH_TOKEN
   ```

3. **Start the server**
   - The script will automatically launch ngrok.
   - Check the terminal for the public URL.
   - Access that URL from your phone, anywhere.

## 🔧 Configuration

### Changing the Port

Edit `app.py` and find the last line:

```python
app.run(host='0.0.0.0', port=5000, debug=False)
```
Change port=5000 to whatever port you prefer.

### Adding More Keys

Add mappings to the `KEY_MAPPING` dictionary in `app.py`:
```python
KEY_MAPPING = {
    'a': 'a',  # Add letter a
    'ctrl': Key.ctrl,  # Add Ctrl
}
```
Then, add the corresponding button to templates/index.html
