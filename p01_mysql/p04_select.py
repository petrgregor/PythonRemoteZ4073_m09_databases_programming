from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """SELECT * FROM movies;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            print("===================== MOVIES =====================")
            print(f"id\ttitle\tyear\tcategory\tdirector_id\trating")
            for movie in movies:
                print(f"{movie[0]}\t{movie[1]}\t{movie[2]}\t{movie[3]}\t{movie[4]}\t{movie[5]}")

            sql_statement = """SELECT * FROM directors;"""
            cursor.execute(sql_statement)
            directors = cursor.fetchall()
            print("===================== DIRECTORS =====================")
            for director in directors:
                print(*director)

            task = """Úkol 6
Napište dotaz SQL, který vrátí všechny filmy z roku 2002. Proveďte onen dotaz."""
            print("===================== MOVIES (year = 2002) =====================")
            sql_statement = """SELECT * FROM movies WHERE year = 2002;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(*movie)

            print("===================== MOVIES (year = 1994) =====================")
            sql_statement = """SELECT * FROM movies WHERE year = 1994;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(*movie)

            print("===================== MOVIES (year = 1994) with director name + surname =====================")
            sql_statement = """
                SELECT * FROM movies 
                    LEFT JOIN directors d on movies.director_id = d.director_id
                    WHERE year = 1994;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(f"Movie: '{movie[1]}' directed by '{movie[7]} {movie[8]}'.")

            print("===================== MOVIES CATEGORY COUNT =====================")
            sql_statement = """
                SELECT category, COUNT(category) FROM movies GROUP BY category;
            """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(*result)

            print("===================== 5 MOVIES WITH HIGHEST RATING =====================")
            sql_statement = """
                SELECT title, rating FROM movies
                ORDER BY rating DESC 
                LIMIT 5;
            """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(*result)

            print("===================== n MOVIES WITH HIGHEST RATING =====================")
            try:
                n = int(input("How many results do you want? "))
            except ValueError as e:
                print(e)
                n = 5
            sql_statement = f"""
                            SELECT title, rating FROM movies
                            ORDER BY rating DESC 
                            LIMIT {n};
                        """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(*result)

            """TASK:
            Chceme vypsat všechny režiséry a pod jménem odsazeně všechny jeho filmy:
            Frank Darabont (2 filmy):
                The Shawshank Redemption
                The Green Mile
            Francis Ford Coppola (2 filmy):
                The Godfather
                The Godfather III
            ...
            """
            print("===================== DIRECTORS AND THEIR MOVIES =====================")
            sql_statement = """SELECT director_id, name, surname FROM directors;"""
            cursor.execute(sql_statement)
            directors = cursor.fetchall()
            for director in directors:
                sql_statement = f"""
                    SELECT * FROM movies
                    WHERE director_id = {director[0]}
                """
                cursor.execute(sql_statement)
                movies = cursor.fetchall()
                print(f"{director[1]} {director[2]} ({len(movies)} filmy):")
                for movie in movies:
                    print(f"\t{movie[1]}")


except Error as e:
    print(e)

print("== END ==")
