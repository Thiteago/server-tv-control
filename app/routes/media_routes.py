from flask import Blueprint, request, jsonify
from ..services.media_services import MediaController
from ..services.system_services import SystemController

media_routes = Blueprint('media_routes', __name__)

media_controller = MediaController()
system_controller = SystemController()

@media_routes.route('/play_pause', methods=['POST'])
def play_pause():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.play_pause(is_vlc)
  return jsonify({'message': 'Play/pause triggered', 'success': success})

@media_routes.route('/volume_up', methods=['POST'])
def volume_up():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.volume_up(is_vlc)
  return jsonify({'message': 'Volume up triggered', 'success': success})

@media_routes.route('/volume_down', methods=['POST'])
def volume_down():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.volume_down(is_vlc)
  return jsonify({'message': 'Volume down triggered', 'success': success})

@media_routes.route('/jump_forward', methods=['POST'])
def jump_forward():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.forward(is_vlc)
  return jsonify({'message': 'Forward triggered', 'success': success})

@media_routes.route('/jump_backward', methods=['POST'])
def jump_backward():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.backward(is_vlc)
  return jsonify({'message': 'Backward triggered', 'success': success})

@media_routes.route('/next', methods=['POST'])
def next():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.next(is_vlc)
  return jsonify({'message': 'Next triggered', 'success': success})

@media_routes.route('/previous', methods=['POST'])
def previous():
  data = request.get_json()
  is_vlc = data.get('is_vlc', "False")
  success = media_controller.previous(is_vlc)
  return jsonify({'message': 'Previous triggered', 'success': success})

@media_routes.route('/shutdown', methods=['POST'])
def shutdown():
  system_controller.shutdown()
  return jsonify({'message': 'Shutdown triggered', 'success': True})

@media_routes.route('/schedule_shutdown', methods=['POST'])
def schedule_shutdown():
  data = request.get_json()
  minutes = data.get('minutes', 1)
  system_controller.schedule_shutdown(minutes)
  return jsonify({'message': f'Shutdown scheduled in {minutes} minutes', 'success': True})

@media_routes.route('/cancel_shutdown', methods=['POST'])
def cancel_shutdown():
  system_controller.cancel_shutdown()
  return jsonify({'message': 'Shutdown cancelled', 'success': True})