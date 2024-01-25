import requests
from pymongo import MongoClient

def get_google_map_cords_by_prompt(prompt):
    api_key = "Akg-oZJD8XMkferl2H4-SqAC5ukNw1tx7eEuUqRHiv72a1QN4LSwyHVNUVbpoXSA"
    url = f"http://dev.virtualearth.net/REST/v1/Locations?query={prompt}&key={api_key}"
    response = requests.get(url)
    return response.json()

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1")
print("Mongo db connected")
db = client['edurank']

schools = list(db['schools'].find({}, {'_id': 0}))
i=1
for school in schools:
	i = i + 1
	if i < 5561:
		continue
	name = school['institution_name']
	kotauu = school['koatuu_name']
	address = school['address']
	id = school['institution_id']
	google_api_response = get_google_map_cords_by_prompt(f"{kotauu} {address}")
	db['coords_by_address'].insert_one({
		"name": name,
		"id": id,
		"coords": google_api_response
	})
	print(f"Success {i}")

        