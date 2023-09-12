import requests
from python_json_config import ConfigBuilder

builder = ConfigBuilder()
config = builder.parse_config('configuration.json')

url = "https://telesign-telesign-send-sms-verification-code-v1.p.rapidapi.com/sms-verification-code"

def send_verification_code(phone_number, verification_code):

  querystring = {
    "phoneNumber": phone_number,
    "verifyCode": verification_code,
    "appName": "EduRank"
  }

  headers = {
    "X-RapidAPI-Key": config.sms_verify_api_key,
    "X-RapidAPI-Host": config.sms_verify_host
  }

  response = requests.post(url, headers=headers, params=querystring)

  return response.json()