from database_parser import DatabaseParser
from search_engine import fetch_images_by_prompt, get_google_map_cords_by_prompt
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

databaseParser = None

@app.route('/api/schools')
def school():
    global databaseParser
    if databaseParser is None:
        return jsonify({'error': 'Database is not loaded'})
    return jsonify(databaseParser.get_json_response())

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

    return jsonify(school_responce)

@app.route('/api/images')
def images():
    query = request.args.get('query')
    return jsonify(fetch_images_by_prompt(prompt=query))

@app.route('/api/map')
def map():
    query = request.args.get('query')
    return jsonify(get_google_map_cords_by_prompt(prompt=query))

if __name__ == "__main__":
    print('Starting application')
    databaseParser = DatabaseParser(database_name="test.db", url="https://registry.edbo.gov.ua/api/schools/?lc=&ut=3&exp=json")
    app.run(debug=True, port=5000)
