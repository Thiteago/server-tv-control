from flask import Blueprint, request, jsonify
from ..services.search_services import SearchController

search_routes = Blueprint('search_routes', __name__)

search_controller = SearchController()

@search_routes.route('/search', methods=['POST'])
def search():
  data = request.get_json()
  search_query = data.get('search', "")
  platform = data.get('platform', "")
  result = search_controller.search(search_query, platform)
  return jsonify({'message': 'Search Triggered', 'success': result})

