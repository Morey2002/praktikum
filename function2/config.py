host = "127.0.0.1"
user = "postgres"
password = "19741980"
db_name = "Saby"

from config import host, user, password, db_name
import psycopg2
from psycopg2 import Error

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password="19741980",
        database="postgres",
        port='5555'
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Serever Version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL)"""
        )

        print()
        print("[INFO] Table created successfully")


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

