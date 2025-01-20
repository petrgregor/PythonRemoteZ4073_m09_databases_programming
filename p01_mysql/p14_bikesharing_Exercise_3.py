"""Exercise 3
● fetch total sum of new shares by season
● fetch total sum of new shares during thunderstorms
● fetch the date and hour with the most new shares
"""

from mysql.connector import connect, Error
from connection_details import *

seasons = {0: 'spring', 1: 'summer', 2: 'fall', 3: 'winter'}

try:
    with connect(host=host, user=user, password=password, database='bikesharing') as conn:
        with conn.cursor() as cursor:
            task_3a = "fetch total sum of new shares by season"
            print(task_3a)
            sql_statement = """
                SELECT season, SUM(cnt) as sum FROM bikesharing
                GROUP BY season;
            """
            cursor.execute(sql_statement)
            results = sorted(cursor.fetchall())
            print("SEASON\tCOUNT")
            print('-'*15)
            for result in results:
                print(f"{seasons[result[0]]}\t{result[1]}")

            task_3b = "fetch total sum of new shares during thunderstorms"
            print(task_3b)
            sql_statement = """
                SELECT SUM(cnt) as sum FROM bikesharing
                WHERE weather_code = 10;
            """
            cursor.execute(sql_statement)
            print(f"{cursor.fetchone()[0]}")

            task_3c = "fetch the date and hour with the most new shares"
            print(task_3c)
            sql_statement = """
                SELECT tstamp, cnt FROM bikesharing
                WHERE cnt = (
                    SELECT MAX(cnt) FROM bikesharing
                );
            """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(f"{result[0]}")

            # nebo
            sql_statement = """
                SELECT tstamp, cnt FROM bikesharing
                ORDER BY cnt DESC 
                LIMIT 1;
            """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(f"{result[0]}")

except Error as e:
    print(e)


print("== END ==")
