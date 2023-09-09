import sqlite3
import requests
import json
import sys

class DatabaseParser():

    url = None
    database_name = None
    json_response = None

    def __init__(self, url, database_name):
        self.url = url
        self.database_name = database_name
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
    
    def get_database_name(self):
        return self.database_name
    
    def execute_query(self, query, values):
        pass

    def get_json_response(self):
        return self.json_response
