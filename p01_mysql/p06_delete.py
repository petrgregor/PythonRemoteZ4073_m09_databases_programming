from mysql.connector import connect, Error
from connection_details import *


try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            """Smažeme film s názvem Zodiac"""
            sql_statement = """
                DELETE FROM movies
                WHERE title = 'Zodiac';
            """
            cursor.execute(sql_statement)
            conn.commit()

            sql_statement = """
                SELECT * FROM movies;
            """
            cursor.execute(sql_statement)
            result = cursor.fetchall()
            for movie in result:
                print(*movie)

except Error as e:
    print(e)

print("== END ==")
