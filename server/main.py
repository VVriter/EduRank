from database_parser import DatabaseParser
from search_engine import fetch_images_by_prompt, get_google_map_cords_by_prompt
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from sms import send_verification_code, is_phone_valid

app = Flask(__name__)
CORS(app=app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app=app)

databaseParser = None

@app.route('/api/search')
def search():
    query = request.args.get('query')
    responce_schools = []

    for school in databaseParser.get_json_response():
        if query.lower() in school['institution_name'].lower() or query.lower() in school['short_name'].lower():
            responce_schools.append(school)

    if len(query) <= 3:
        return jsonify([responce_schools[0], responce_schools[1], responce_schools[3], responce_schools[4]])

    return jsonify(responce_schools)

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

@app.route('/api/chart')
def chart():
    query = request.args.get('query')
    return jsonify([1, 2, 3, 5, 4, 2, 5])





if __name__ == "__main__":
    print('Starting application')
    databaseParser = DatabaseParser(database_name="test.db", url="https://registry.edbo.gov.ua/api/schools/?lc=&ut=3&exp=json")
    app.run(debug=True, port=5000)
