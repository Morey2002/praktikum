import requests
import pprint

response = requests.get('https://api.github.com')
response_json = response.json()
print(response.status_code)
pprint.pprint(response_json)
print(type(response_json))
print(response.headers)
print(response.request.headers)

user_agent = {'User-Agent': 'I am here again'}
response = requests.get('https://api.github.com', headers=user_agent)

print(response.request.headers)

