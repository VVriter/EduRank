from edbo_api import EdboApiFetcher
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from python_json_config import ConfigBuilder
from database import Database
import requests
import uuid
import json
import datetime
from bson import ObjectId
from tg_bot import TgBot
from search_engine import fetch_images_by_prompt, get_google_map_cords_by_prompt
from gMapsNear import find_schools_nearby


builder = ConfigBuilder()
config = builder.parse_config('configuration.json')

app = Flask(__name__)
CORS(app=app)

database = Database(url=config.database, database_name=config.database_name)
tg_bot = TgBot(config.tg_bot_token, config.admin_id, database)
databaseParser = EdboApiFetcher(config.schools_list_api_url, database)


@app.route('/api/search')
def search():
    query = request.args.get('query', '').lower()
    print(query)
    limit = request.args.get('limit')
    schools = databaseParser.get_json_response()

    matching_schools = [school for school in schools if query in school['institution_name'].lower() or query in school['short_name'].lower()]

    if len(query) <= 3:
        response_schools = matching_schools[:2]
    else:
        if limit:
            response_schools = matching_schools[:int(limit)]
        else:
            response_schools = matching_schools[:2]

    return jsonify(response_schools)

@app.route('/api/edbo')
def edbo():
    query = request.args.get('query')
    school_responce = None
    for school in databaseParser.get_json_response():
        if school['institution_id'] == query:
            school_responce = school

    if school_responce == None:
        return jsonify({
            'error': 'School not found'
        }), 404
    return jsonify(school_responce)

@app.route('/api/images')
def images():
    query = request.args.get('query')
    edbo = request.args.get('edbo')

    if not query or not edbo:
        return jsonify({'status': 'failed', 'message': 'Bad params'}), 400
    
    images = database.images_collection.find_one({"edbo": edbo})

    if not images:
        images_loaded = fetch_images_by_prompt(prompt=query)
        database.images_collection.insert_one({"edbo": edbo, "items": images_loaded['items']})
        return jsonify(images_loaded)
    else:
        return jsonify({
            "items": images['items']
        })

@app.route('/api/map')
def map():
    query = request.args.get('query')
    return jsonify(get_google_map_cords_by_prompt(prompt=query))

@app.route('/api/register', methods = ['POST'])
def register():
    try: 
        data = request.json
        print(data)
        if data and data['name'] and data['surname'] and data['userType'] and (data['userType'] == "parrent" or data['userType'] == "pupil" or data['userType'] == "teacher") and data['email']:
            if database.is_user_already_exists(data['email']):
                return jsonify({'status': 'failed'}), 400
            database.register_user(data)
            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'failed'}), 400
    except Exception as error:
        print(error)
        return jsonify({'status': 'failed', 'exception': error}), 500

@app.route('/api/verify', methods = ['POST'])
def verify():
    userId = request.args.get('id')
    if not userId:
        return jsonify({'status': 'failed'}), 400
    if database.verify_user(userId):
        return jsonify({'status': 'success', 'token': userId}), 200
    else:
        return jsonify({'status': 'failed'}), 400

@app.route('/api/login', methods = ['POST'])
def login():
    email = request.json['email']
    if not email:
        return jsonify({'status': 'failed'}), 400
    if database.is_user_already_exists(email):
        database.send_verify_login(email)
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'failed'}), 400
    
@app.route('/api/me', methods = ['GET'])
def me():
    token = request.headers.get('token')
    if token == 'null':
        return jsonify({'status': 'failed', 'message': 'Invalid token'}), 400
    if token:
        user = database.get_user(token)
        if user:
            return jsonify({'status': 'success', 'user': user}), 200
        else:
            return jsonify({'status': 'failed', 'message': 'Invalid token'}), 400
    else:
        return jsonify({'status': 'failed', 'message': 'Invalid token'}), 400
    
@app.route('/api/donate', methods = ['POST'])
def donate():

    data = request.json

    amount = int(request.args.get('amount'))
    description = data['description']
    contact = data['contact']

    if not amount or not contact:
        return jsonify({'status': 'failed'}), 400

    token = config.mono_token
    headers = {
        'Content-Type': 'application/json',
        'X-Token': token
    }
    body = {
        'amount': amount,
        'ccy': 980,
        'merchantPaymInfo': {
            'reference': str(uuid.uuid4()),
            'destination': f"Донат в підтримку проєкту EduRank від {contact}",
            'comment': description if description else 'Без опису',
        },
        'redirectUrl': f'{config.domen}/donate/success'
    }
    response = requests.post('https://api.monobank.ua/api/merchant/invoice/create', headers=headers, data=json.dumps(body))
    json_response = response.json()
    return jsonify({'status': 'success', 'mono': json_response}), 200

@app.route('/api/reviews', methods = ['PUT'])
def reviews_add():
    token = request.headers.get('token')
    edbo = request.args.get('edbo')
    data = request.json

    if not token or not edbo or not data:
        return jsonify({'status': 'failed', 'message': 'Bad params'}), 400
    
    user = database.get_user(token)
    if edbo in user['reviews']:
        return jsonify({'status': 'failed', 'message': 'Review already exists'}), 400
    if not user:
        return jsonify({'status': 'failed', 'message': 'Unknown user'}), 400
    
    database.reviews_collection.insert_one({
        'approved': True,
        'annon': False,
        'edbo': edbo,
        'review': data,
        'user': user,
        'time': datetime.datetime.now(tz=datetime.timezone.utc)
    })

    database.users_collection.update_one({'_id': ObjectId(token)}, {'$push': {'reviews': edbo}})
    return jsonify({'status': 'success'}), 200

@app.route('/api/reviews/annon', methods = ['PUT'])
def annon_reviews_add():
    data = request.json
    edbo = request.args.get('edbo')

    if not edbo or not data:
        return jsonify({'status': 'failed', 'message': 'Bad params'}), 400

    id = database.reviews_collection.insert_one({
        'approved': False,
        'edbo': edbo,
        'review': data,
        'time': datetime.datetime.now(tz=datetime.timezone.utc)
    }).inserted_id

    tg_bot.send_for_approvement(data, id)

    return jsonify({'status': 'success'}), 200


@app.route('/api/reviews', methods = ['GET'])
def reviews_get():  
    edbo = request.args.get('edbo')
    if not edbo:
        return jsonify({'status': 'failed'}), 400
    else:
        reviews = database.get_reviews(edbo)
        if not reviews:
            return jsonify({'status': 'success', 'reviews': []}), 200
        else:
            return jsonify({'status': 'success', 'reviews': [json.dumps(document, default=str) for document in reviews]}), 200

@app.route('/api/searchNear', methods = ['GET'])
def searchNear():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    if not longitude or not latitude:
        return jsonify({'status': 'failed', 'message': 'bad params'}), 400

    schools = databaseParser.get_json_response()
    nerby_schools = find_schools_nearby(latitude, longitude)
    
    return jsonify({'status': 'success', 'schools': [], 'all': nerby_schools})

if __name__ == "__main__":
    print('Starting application')
    tg_bot.start_polling()
    app.run(debug=False, port=5000)