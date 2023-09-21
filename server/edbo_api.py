import sqlite3
import requests
import json
import sys

class EdboApiFetcher():

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        response.encoding = 'utf-8'  # Set the encoding to UTF-8
        if response.status_code == 200:
            json_string = response.text  # Use text instead of content for decoding
            self.json_response = json.loads(json_string)
            print('Database already loaded!')
        else:
            print("Error: Unable to fetch data from the URL. Status code:", response.status_code)
            sys.exit()

    def get_url(self):
        return self.url

    def get_json_response(self):
        return self.json_response
