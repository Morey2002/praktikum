import requests
import pprint

response = requests.get('https://api.github.com')
response_json = response.json()
#print(response.status_code)
pprint.pprint(response_json)
print(type(response_json))