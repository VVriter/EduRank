import requests

def find_schools_nearby(api_key, latitude, longitude, radius=10000, type='school', language='uk'):
    endpoint_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'key': api_key,
        'location': f'{latitude},{longitude}',
        'radius': radius,
        'type': type,
        'language': language
    }

    response = requests.get(endpoint_url, params=params)
    if response.status_code == 200:
        results = response.json().get('results', [])
        return results
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

# Замените 'YOUR_API_KEY' на ваш собственный ключ API Google Places
api_key = 'AIzaSyDDy5IUrvL4bVAdeQ_MBvcqsy1rgs5X3V4'
latitude = 50.141100  # Широта (например, Москва)
longitude = 30.745100  # Долгота (например, Москва)

schools = find_schools_nearby(api_key, latitude, longitude)
if schools:
    print("Список школ в радиусе 10 км:")
    for index, school in enumerate(schools, 1):
        print(f"{index}. {school['name']} - {school['vicinity']}")
else:
    print("Не удалось получить список школ.")
