from flask import Blueprint, request, jsonify
from ..services.search_services import SearchController

search_routes = Blueprint('search_routes', __name__)

search_controller = SearchController()

@search_routes.route('/search', methods=['POST'])
def search():
  data = request.get_json()
  search_query = data.get('search', "")
  platform = data.get('platform', "")
  results = search_controller.search(search_query, platform)
  
  def format_results(results):
    formatted_results = {}
    for platform, platform_results in results.items():
      formatted_results[platform] = []
      for result in platform_results:
        formatted_results[platform].append({
          'title': result['title'],
          'year': result['year'],
          'link': result['link'],
          'image_link': result['image_link']
        })
    return formatted_results

  formatted_results = format_results(results)
    
  return jsonify({"results": formatted_results})



