from mysql.connector import connect, Error
from connection_details import *


try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            """Smažeme tabulky movies a directors z databáze."""
            sql_statement = """DROP TABLE movies;"""
            cursor.execute(sql_statement)
            conn.commit()
            print("Table 'movies' deleted.")

            sql_statement = """DROP TABLE directors;"""
            cursor.execute(sql_statement)
            conn.commit()
            print("Table 'directors' deleted.")


except Error as e:
    print(e)

print("== END ==")
