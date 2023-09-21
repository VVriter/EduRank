import requests
from python_json_config import ConfigBuilder
import facebook

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
            error_message = f"API request failed with status code {response.status_code}: {response.text}"
            return {"error": error_message}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def get_google_map_cords_by_prompt(prompt):
    api_key = config.google_map_engine_key
    url = f"http://dev.virtualearth.net/REST/v1/Locations?query={prompt}&key={api_key}"
    response = requests.get(url)
    return response.json()

class FacebookApiProcessor():

    def __init__(self):
        self.__app_id = config.fb_id
        self.__app_secret = config.fb_secret
        self.__app_access_token = config.fb_access_token
        self.__graph = facebook.GraphAPI(access_token=self.get_app_access_token, version='3.1')
        
    def get_app_id(self):
        return self.__app_id
    
    def get_app_secret(self):
        return self.__app_secret
    
    def get_app_access_token(self):
        return self.__app_access_token
    
    def get_graph(self):
        return self.__graph

    def search(self, prompt):
        return ""