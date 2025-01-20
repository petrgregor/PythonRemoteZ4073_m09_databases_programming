from mysql.connector import connect, Error
from connection_details import *


try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            """Změnit rating filmu Interstellar na 10"""
            sql_statement = """
                UPDATE movies SET rating = 10
                WHERE title = 'Interstellar';
            """
            cursor.execute(sql_statement)
            conn.commit()

            sql_statement = """
                SELECT * FROM movies
                WHERE title = 'Interstellar';
            """
            cursor.execute(sql_statement)
            result = cursor.fetchone()
            print(*result)

except Error as e:
    print(e)

print("== END ==")
