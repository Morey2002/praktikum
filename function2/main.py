from config import host, user, password, db_name
import requests
import pprint
import psycopg2
from psycopg2 import Error

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port='5433'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(cursor.fetchone())

except Error as error:
    print("Ошибка подключения:", error)

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None and not connection.closed:
        connection.close()
        print("Соединение закрыто")











'''response = requests.get('https://api.github.com')
response_json = response.json()
print(response.status_code)
pprint.pprint(response_json)
print(type(response_json))
print(response.headers)
print(response.request.headers)

user_agent = {'User-Agent': 'I am here again'}
response = requests.get('https://api.github.com', headers=user_agent)

print(response.request.headers)'''

