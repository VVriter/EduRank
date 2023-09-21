from edbo_api import EdboApiFetcher
from search_engine import fetch_images_by_prompt, get_google_map_cords_by_prompt, FacebookApiProcessor
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from python_json_config import ConfigBuilder


builder = ConfigBuilder()
config = builder.parse_config('configuration.json')

app = Flask(__name__)
CORS(app=app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app=app)


# all routers
@app.route('/api/search')
def search():
    query = request.args.get('query', '').lower()
    schools = databaseParser.get_json_response()

    matching_schools = [school for school in schools if query in school['institution_name'].lower() or query in school['short_name'].lower()]

    if len(query) <= 3:
        response_schools = matching_schools[:5]
    else:
        response_schools = matching_schools

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

@app.route('/api/me')
def me():
    return jsonify({
        'success': True,
        'logined': False,
    })

@app.route('/api/credentials/tg')
def tg_creds():
    return jsonify({
        'username': config.tg_username,
        'url': config.url,
        'bot_id': config.tg_bot_id
    })

@app.route('/api/credentials/google')
def google_creds():
    return jsonify({
        'id': config.google_0auth_client_id,
        'secret': config.google_0auth_client_secret,
        'url': config.url
    })


@app.route('/api/login/google')
def login_via_google():
    return jsonify({
        'success': True
    })

if __name__ == "__main__":
    print('Starting application')
    facebook = FacebookApiProcessor()
    res = facebook.search('Трипільський ліцей')
    print(res)
    databaseParser = EdboApiFetcher(url="https://registry.edbo.gov.ua/api/schools/?lc=&ut=3&exp=json")
    app.run(debug=True, port=5000)