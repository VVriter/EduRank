from pymongo import MongoClient
import datetime

class Database():
    def __init__(self, url, database_name):
        self.url = url
        self.client = MongoClient(self.url)
        self.db = self.client[database_name]
        self.users_collection = self.db['users']

    def register_user(self, user_data):
        if not all(key in user_data for key in ('name', 'surname', 'userType', 'email')):
            raise ValueError("Incomplete user data provided")

        user = {
            'name': user_data['name'],
            'surname': user_data['surname'],
            'userType': user_data['userType'],
            'email': user_data['email'],
            'verified': False,
            'date': datetime.datetime.now(tz=datetime.timezone.utc)
        }

        try:
            post_id = self.users_collection.insert_one(user).inserted_id
            return post_id
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            return None