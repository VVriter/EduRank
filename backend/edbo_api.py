import sqlite3
import requests
import json
import sys

class EdboApiFetcher():

    def __init__(self, url, database):
        print("Starting loading edbo database")
        self.url = url
        schools = database.schools_collection.find({}, {'_id': 0})
        if schools and len(list(schools)) > 5:
            schools_list = list(schools)
            self.json_response = json.dumps(schools_list)
            self.json_response = json.loads(self.json_response)
            print('Edbo database loaded')
            return

        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            json_string = response.text
            self.json_response = json.loads(json_string)
            database.schools_collection.insert_many(self.json_response)
            print('Database already loaded!')
        else:
            print("Error: Unable to fetch data from the URL. Status code:", response.status_code)
            sys.exit()

    def get_url(self):
        return self.url

    def get_json_response(self):
        return self.json_response
