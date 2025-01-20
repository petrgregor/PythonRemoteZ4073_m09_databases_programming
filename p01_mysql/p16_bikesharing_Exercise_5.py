"""Deleting values - Exercise 5
● Delete all entries from 2017-01-03 in bikesharing table"""

from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password, database='bikesharing') as conn:
        with conn.cursor() as cursor:
            # TODO: Delete all entries from 2017-01-03 in bikesharing table
            pass


except Error as e:
    print(e)

print("== END ==")
