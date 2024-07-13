from flask import Flask, request, jsonify
from ctypes import windll
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

VLC_PASSWORD = 'vlcpassword'
VLC_URL = 'http://localhost:8080/requests/status.json'
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_VOLUME_UP = 0xAF
VK_VOLUME_DOWN = 0xAE

def press_key(hexKeyCode):
    windll.user32.keybd_event(hexKeyCode, 0, 0, 0)
    windll.user32.keybd_event(hexKeyCode, 0, 2, 0)

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(level, None)

def send_vlc_command(command):
    url = f'http://localhost:8080/requests/status.json?command={command}'
    response = requests.get(url, auth=('', VLC_PASSWORD))
    return response.status_code == 200

@app.route('/play_pause', methods=['POST'])
def play_pause():
    data = request.get_json()
    is_vlc = data.get('is_vlc', "False")
    if is_vlc == "True":
        success = send_vlc_command('pl_pause')
        return jsonify({'message': 'VLC play/pause triggered', 'success': success})
    else:
        press_key(VK_MEDIA_PLAY_PAUSE)
        return jsonify({'message': 'Play/pause triggered', 'success': True})

@app.route('/volume_up', methods=['POST'])
def volume_up():
    data = request.get_json()
    is_vlc = data.get('is_vlc', "False")
    if is_vlc == "True":
        success = send_vlc_command('volume&val=%2B20')
        return jsonify({'message': 'VLC volume up triggered', 'success': success})
    else:
        press_key(VK_VOLUME_UP)
        return jsonify({'message': 'Volume up triggered', 'success': True})

@app.route('/volume_down', methods=['POST'])
def volume_down():
    data = request.get_json()
    is_vlc = data.get('is_vlc', "False")
    if is_vlc == "True":
        success = send_vlc_command('volume&val=-20')
        return jsonify({'message': 'VLC volume down triggered', 'success': success})
    else:
        press_key(VK_VOLUME_DOWN)
        return jsonify({'message': 'Volume down triggered', 'success': True})

@app.route('/')
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(host='192.168.1.3', port=5000)