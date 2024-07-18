
import requests
import time
from comtypes import CLSCTX_ALL
from ..helpers.keyboard_events import PressKey, ReleaseKey
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class MediaController:
  VLC_PASSWORD = 'vlcpassword'
  VLC_URL = 'http://localhost:8080/requests/status.json'
  VK_MEDIA_PLAY_PAUSE = 0xB3
  VK_VOLUME_UP = 0xAF
  VK_VOLUME_DOWN = 0xAE
  VK_RIGHT = 0x27
  VK_LEFT = 0x25
  VK_MEDIA_NEXT_TRACK = 0xB0
  VK_MEDIA_PREV_TRACK = 0xB1
  
  @staticmethod
  def press_key(key):
    PressKey(key)
    time.sleep(0.5)
    ReleaseKey(key)

  @staticmethod
  def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(level, None)

  def send_vlc_command(self, command):
    url = f'http://localhost:8080/requests/status.json?command={command}'
    response = requests.get(url, auth=('', self.VLC_PASSWORD))
    return response.status_code == 200

  def play_pause(self, is_vlc):
    if is_vlc == "True":
      return self.send_vlc_command('pl_pause')
    else:
      self.press_key(self.VK_MEDIA_PLAY_PAUSE)
      return True

  def volume_up(self, is_vlc):
    if is_vlc == "True":
      return self.send_vlc_command('volume&val=%2B20')
    else:
      self.press_key(self.VK_VOLUME_UP)
      return True

  def volume_down(self, is_vlc):
    if is_vlc == "True":
      return self.send_vlc_command('volume&val=-20')
    else:
      self.press_key(self.VK_VOLUME_DOWN)
      return True

  def forward(self, is_vlc):
    if is_vlc == "True":
      return self.send_vlc_command('seek&val=+10')
    else:
      self.press_key(self.VK_RIGHT)
      return True

  def backward(self, is_vlc):
    if is_vlc == "True":
      return self.send_vlc_command('seek&val=-10')
    else:
      self.press_key(self.VK_LEFT)
      return True
    
  def next(self, is_vlc):
    if is_vlc == "True":
      return self.send_vlc_command('pl_next')
    else:
      self.press_key(self.VK_MEDIA_NEXT_TRACK)
      return True
    
  def previous(self, is_vlc):
    if is_vlc == "True":
      return self.send_vlc_command('pl_previous')
    else:
      self.press_key(self.VK_MEDIA_PREV_TRACK)
      return True
