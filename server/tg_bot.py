import telebot
from telebot import types
from bson import ObjectId
from threading import Thread
 
class TgBot():
    def __init__(self, token, admin_id, database):
        print("Starting telegram bot")
        self.bot = telebot.TeleBot(token)
        self.token = token
        self.admin_id = admin_id
        self.database = database

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query_handler(call):
            print('asdasdasd')
            if call.data.startswith('approve'):
                id = call.data.split()[1]
                self.database.reviews_collection.update_one({"_id": ObjectId(id)}, {"$set": {'approved': True}})
            
    def start_polling(self):
        tg_bot_thread = Thread(target=self.bot.infinity_polling)
        tg_bot_thread.start()

    def send_for_approvement(self, review, id):
        button_approve = types.InlineKeyboardButton('Approve', callback_data=f"approve {id}")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button_approve)
        self.bot.send_message(self.admin_id, f"```\n{review}\n```", reply_markup=keyboard, parse_mode='MarkdownV2')
