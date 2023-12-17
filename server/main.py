from edbo_api import EdboApiFetcher
from search_engine import fetch_images_by_prompt, get_google_map_cords_by_prompt, FacebookApiProcessor
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from python_json_config import ConfigBuilder
from database import Database
import requests
import uuid
import json


builder = ConfigBuilder()
config = builder.parse_config('configuration.json')

app = Flask(__name__)
CORS(app=app)

database = Database(url=config.database, database_name=config.database_name)


# all routers
@app.route('/api/search')
def search():
    query = request.args.get('query', '').lower()
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
    return jsonify(fetch_images_by_prompt(prompt=query))

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
    if token:
        user = database.get_user(token)
        if user:
            return jsonify({'status': 'success', 'user': {
                'name': user['name'],
                'surname': user['surname'],
                'email': user['email'],
                'userType': user['userType']
            }}), 200
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
        'redirectUrl': 'http://localhost/donate/success'
    }
    response = requests.post('https://api.monobank.ua/api/merchant/invoice/create', headers=headers, data=json.dumps(body))
    json_response = response.json()
    return jsonify({'status': 'success', 'mono': json_response}), 200

@app.route('/api/reviews', methods = ['PUT'])
def reviews_add():
    pass

@app.route('/api/reviews', methods = ['GET'])
def reviews_get():  
    edbo = request.args.get('query')
    if not edbo:
        return jsonify({'status': 'failed'}), 400
    else:
        reviews = database.get_reviews(edbo)
        if not reviews:
            return jsonify({'status': 'success', 'reviews': []}), 200
        else:
            return jsonify({'status': 'success', 'reviews': reviews}), 200

if __name__ == "__main__":
    print('Starting application')
    databaseParser = EdboApiFetcher(url="https://registry.edbo.gov.ua/api/schools/?lc=&ut=3&exp=json")
    app.run(debug=True, port=5000)