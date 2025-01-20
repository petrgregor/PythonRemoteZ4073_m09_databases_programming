"""Updating values - Exercise 4
● Add 10 to cnt column for all 2015-01-09 entries"""
import datetime

from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password, database='bikesharing') as conn:
        with conn.cursor() as cursor:
            sql_statement = f"""
                SELECT tstamp, cnt FROM bikesharing
                WHERE tstamp >= '{datetime.datetime(2015, 1, 9, 0, 0, 0)}' 
                    AND tstamp < '{datetime.datetime(2015, 1, 10, 0, 0, 0)}';
            """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(result)
            # TODO: Add 10 to cnt column for all 2015-01-09 entries

except Error as e:
    print(e)

print("== END ==")
