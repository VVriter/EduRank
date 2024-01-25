import requests

# Замените 'YOUR_API_KEY' на ваш собственный ключ API Google Places
api_key = 'AIzaSyDDy5IUrvL4bVAdeQ_MBvcqsy1rgs5X3V4'

def find_schools_nearby(latitude, longitude, radius=10000, type='school', api_key=api_key, language='uk'):
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
        schools_info = []

        for result in results:
            # Get additional details for each place (including address)
            place_id = result.get('place_id')
            place_details = get_place_details(place_id, api_key, language)

            # Add the school info to the list
            schools_info.append({
                'details': place_details,
                'more': result
            })

        return schools_info
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def get_place_details(place_id, api_key, language):
    details_endpoint_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    details_params = {
        'key': api_key,
        'place_id': place_id,
        'language': language
    }

    details_response = requests.get(details_endpoint_url, params=details_params)
    if details_response.status_code == 200:
        return details_response.json().get('result', {})
    else:
        print(f"Details request failed with status code {details_response.status_code}")
        return {}
