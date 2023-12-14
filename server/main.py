from edbo_api import EdboApiFetcher
from search_engine import fetch_images_by_prompt, get_google_map_cords_by_prompt, FacebookApiProcessor
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from python_json_config import ConfigBuilder
from database import Database


builder = ConfigBuilder()
config = builder.parse_config('configuration.json')

app = Flask(__name__)
CORS(app=app)

databae = Database(url=config.database, database_name=config.database_name)


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

@app.route('/api/register', methods = ['POST'])
def register():
    try: 
        data = request.json
        print(data)
        if data and data['name'] and data['surname'] and data['userType'] and (data['userType'] == "parrent" or data['userType'] == "pupil" or data['userType'] == "teacher") and data['email']:
            databae.register_user(data)
            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'failed'}), 400
    except Exception as error:
        print(error)
        return jsonify({'status': 'failed', 'exception': error}), 500


if __name__ == "__main__":
    print('Starting application')
    databaseParser = EdboApiFetcher(url="https://registry.edbo.gov.ua/api/schools/?lc=&ut=3&exp=json")
    app.run(debug=True, port=5000)