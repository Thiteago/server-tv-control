from flask import Flask, request
import requests

app = Flask(__name__)

VLC_PASSWORD = 'vlcpassword'
VLC_URL = 'http://localhost:8080/requests/status.json'

def send_vlc_command(command):
  url = f'http://localhost:8080/requests/status.json?command={command}'
  response = requests.get(url, auth=('', VLC_PASSWORD))
  return response.status_code == 200

@app.route('/vlc/play_pause', methods=['POST'])
def vlc_play_pause():
  if send_vlc_command('pl_pause'):
    return 'VLC play/pause triggered'
  else:
    return 'Failed to trigger VLC play/pause', 500

@app.route('/vlc/stop', methods=['POST'])
def vlc_stop():
  if send_vlc_command('pl_stop'):
    return 'VLC stop triggered'
  else:
    return 'Failed to trigger VLC stop', 500

@app.route('/vlc/volume_up', methods=['POST'])
def vlc_volume_up():
  if send_vlc_command('volume&val=%2B20'):
    return 'VLC volume up triggered'
  else:
    return 'Failed to trigger VLC volume up', 500

@app.route('/vlc/volume_down', methods=['POST'])
def vlc_volume_down():
  if send_vlc_command('volume&val=-20'):
    return 'VLC volume down triggered'
  else:
    return 'Failed to trigger VLC volume down', 500

@app.route('/vlc/open', methods=['POST'])
def vlc_open():
  media_url = request.form['url']
  if send_vlc_command(f'in_play&input={media_url}'):
    return f'VLC open media {media_url}'
  else:
    return f'Failed to open media {media_url}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)