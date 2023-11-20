import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Connect to the database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\nConnected to the database!")

    # Query 1: Select all fields from the studio table
    query1 = "SELECT * FROM studio;"
    cursor.execute(query1)
    print("\n-- DISPLAYING Studio RECORDS --")
    for studio_id, studio_name in cursor:
        print(f"Studio ID: {studio_id}\nStudio Name: {studio_name}\n")

    # Query 2: Select all fields from the genre table
    query2 = "SELECT * FROM genre;"
    cursor.execute(query2)
    print("-- DISPLAYING Genre RECORDS --")
    for genre_id, genre_name in cursor:
        print(f"Genre ID: {genre_id}\nGenre Name: {genre_name}\n")

    # Query 3: Select movie names with a runtime less than two hours
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;"
    cursor.execute(query3)
    print("-- DISPLAYING Short Film RECORDS --")
    for film_name, runtime in cursor:
        print(f"Film Name: {film_name}\nRuntime: {runtime}\n")

    # Query 4: List of film names and directors, ordered by director
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_director;"
    cursor.execute(query4)
    print("-- DISPLAYING Director RECORDS in Order --")
    for film_name, director in cursor:
        print(f"Film Name: {film_name}\nDirector: {director}\n")

except mysql.connector.Error as err:
    # Error handling
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    # Close the database connection
    db.close()
    print("Database connection closed...")
