from flask import Blueprint, request, jsonify
from .services import MediaController, SystemController

main = Blueprint('main', __name__)

media_controller = MediaController()
system_controller = SystemController()

@main.route('/play_pause', methods=['POST'])
def play_pause():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.play_pause(is_vlc)
  return jsonify({'message': 'Play/pause triggered', 'success': success})

@main.route('/volume_up', methods=['POST'])
def volume_up():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.volume_up(is_vlc)
  return jsonify({'message': 'Volume up triggered', 'success': success})

@main.route('/volume_down', methods=['POST'])
def volume_down():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.volume_down(is_vlc)
  return jsonify({'message': 'Volume down triggered', 'success': success})

@main.route('/jump_forward', methods=['POST'])
def jump_forward():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.forward(is_vlc)
  return jsonify({'message': 'Forward triggered', 'success': success})

@main.route('/jump_backward', methods=['POST'])
def jump_backward():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.backward(is_vlc)
  return jsonify({'message': 'Backward triggered', 'success': success})

@main.route('/next', methods=['POST'])
def next():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.next(is_vlc)
  return jsonify({'message': 'Next triggered', 'success': success})

@main.route('/previous', methods=['POST'])
def previous():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.previous(is_vlc)
  return jsonify({'message': 'Previous triggered', 'success': success})

@main.route('/shutdown', methods=['POST'])
def shutdown():
  system_controller.shutdown()
  return jsonify({'message': 'Shutdown triggered', 'success': True})

@main.route('/')
def hello():
  return jsonify({'message': 'Hello, World!'})