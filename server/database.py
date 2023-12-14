from pymongo import MongoClient
import datetime
from mailing import send_html_email
from bson import ObjectId
 
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
            send_html_email(user['email'], f"""
                <div style="padding: 10px; width: 90%; background-color: rgb(51, 105, 185); border-radius: 10px; text-align: center;">
                    <div style="display: inline-block; width: fit-content;">
                        <img style="margin: auto; width: 300px; border-radius: 50%;" src="https://cdn.discordapp.com/attachments/1067766486673936438/1184864772571811880/logo.png?ex=658d864f&is=657b114f&hm=640709c9caaae0b161ab47ce5a9784687a19d2c6d9d6743573607c72b9326fc1&" alt="">
                        <h1 style="margin: auto; text-align: center; color: white; padding: 0; margin: 0;">Вітаємо вас {user['name']}!</h1>
                        <p style="width: 50%; margin: auto; text-align: center; margin-top: 10px; color: rgba(255, 255, 255, 0.671);">Щоб пройти веріфікацію - натисніть на кнопку нижче. Пам'ятайте, ваші данні в повній безпеці</p>
                        <a style="border-radius: 10px; width: 50%; margin: auto; text-align: center; padding: 10px; text-decoration: none; background-color: azure; display: block; margin-top: 20px;" href="http://localhost/verify/{post_id}">
                            <p style="margin: auto; color: black; background-color: azure;">Підтвердити!</p>
                        </a> 
                    </div>   
                </div>
            """, subject="Веріфікація EduRank")

            return post_id
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            return None
        
    def is_user_already_exists(self, email):
        return self.users_collection.find_one({'email': email})
    
    def verify_user(self, id):
        if not id:
            return False
        user = self.users_collection.find_one({'_id': ObjectId(id)})
        if not user:
            return False
        try:
            self.users_collection.update_one({'_id': ObjectId(id)}, {'$set': {'verified': True}})
            return True
        except:
            return False
        
    def send_verify_login(self, email):
        user = self.users_collection.find_one({'email': email})
        send_html_email(user['email'], f"""
                <div style="padding: 10px; width: 90%; background-color: rgb(51, 105, 185); border-radius: 10px; text-align: center;">
                    <div style="display: inline-block; width: fit-content;">
                        <img style="margin: auto; width: 300px; border-radius: 50%;" src="https://cdn.discordapp.com/attachments/1067766486673936438/1184864772571811880/logo.png?ex=658d864f&is=657b114f&hm=640709c9caaae0b161ab47ce5a9784687a19d2c6d9d6743573607c72b9326fc1&" alt="">
                        <h1 style="margin: auto; text-align: center; color: white; padding: 0; margin: 0;">Вітаємо вас {user['name']}!</h1>
                        <p style="width: 50%; margin: auto; text-align: center; margin-top: 10px; color: rgba(255, 255, 255, 0.671);">Щоб пройти веріфікацію - натисніть на кнопку нижче. Пам'ятайте, ваші данні в повній безпеці</p>
                        <a style="border-radius: 10px; width: 50%; margin: auto; text-align: center; padding: 10px; text-decoration: none; background-color: azure; display: block; margin-top: 20px;" href="http://localhost/verify/{user['_id']}">
                            <p style="margin: auto; color: black; background-color: azure;">Підтвердити!</p>
                        </a> 
                    </div>   
                </div>
            """, subject="Веріфікація EduRank")
        
    def get_user(self, token):
        return self.users_collection.find_one({'_id': ObjectId(token)})
        