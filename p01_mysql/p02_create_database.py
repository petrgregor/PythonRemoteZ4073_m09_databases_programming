from mysql.connector import connect, Error
from connection_details import *

try:
    """Úkol 1
    Z Pythonu se připojte k serveru mysql. Poté vytvořte databázi cinematic."""
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS cinematic;")
            print("Database 'cinematic' created.")

except Error as e:
    print(e)

print("== END ==")
