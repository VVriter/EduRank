import requests
from python_json_config import ConfigBuilder

builder = ConfigBuilder()
config = builder.parse_config('configuration.json')

def fetch_images_by_prompt(prompt):
    api_key = config.search_engine_api_key
    cx = config.search_engine_cx

    search_url = f'https://www.googleapis.com/customsearch/v1?q={prompt}&cx={cx}&searchType=image&key={api_key}'

    try:
        response = requests.get(search_url)

        if response.status_code == 200:
            return response.json()
        else:
            # Handle API errors gracefully
            error_message = f"API request failed with status code {response.status_code}: {response.text}"
            return {"error": error_message}
    except Exception as e:
        # Handle other exceptions (e.g., network errors)
        return {"error": f"An error occurred: {str(e)}"}
    
def get_google_map_cords_by_prompt(prompt):
    api_key = config.google_map_engine_key
    url = f"http://dev.virtualearth.net/REST/v1/Locations?query={prompt}&key={api_key}"
    response = requests.get(url)
    return response.json()