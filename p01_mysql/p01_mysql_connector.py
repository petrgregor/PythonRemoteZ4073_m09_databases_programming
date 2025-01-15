from mysql.connector import connect, Error

try:
    with connect(host='localhost', user='test', password='test') as conn:
        print(conn)
        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            print(f"Database version: {version[0]}")

except Error as e:
    print(e)

print("== END ==")
