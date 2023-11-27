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


def show_films(cursor, title):
    # Inner join query
    query = ("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as Studio "
             "FROM film "
             "INNER JOIN genre ON film.genre_id = genre.genre_id "
             "INNER JOIN studio ON film.studio_id = studio.studio_id")
    cursor.execute(query)

    films = cursor.fetchall()
    print(f"\n -- {title} --")

    # Display the results
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name: {film[2]}\nStudio Name: {film[3]}\n")


try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Display initial film records
    show_films(cursor, "-- DISPLAYING FILMS --")

    # Insert a new film record (Inception)
    insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
    VALUES ('Inception', '2010', '148', 'Christopher Nolan', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'), (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'))
    """
    cursor.execute(insert_query)
    db.commit()

    # Display films after insert
    show_films(cursor, "-- DISPLAYING FILMS AFTER INSERT --")

    # Update the film 'Alien' to Horror
    update_query = """
    UPDATE film 
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') 
    WHERE film_name = 'Alien'
    """
    cursor.execute(update_query)
    db.commit()

    # Display films after update
    show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror --")

    # Delete the movie 'Gladiator'
    delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
    cursor.execute(delete_query)
    db.commit()

    # Display films after delete
    show_films(cursor, "-- DISPLAYING FILMS AFTER DELETE --")

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
    print("\nDatabase connection closed.")
