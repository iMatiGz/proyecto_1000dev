from sqlite3 import *

file_path = 'App\models\database\cinemark.db'

def get_movies_name():

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute("SELECT movie_name FROM movies")
    movies_name = cursor.fetchall()
    database.close()
    return movies_name


def get_movie_info(movie):

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute(f"""SELECT movie_director, movie_gender, movie_length, movie_premiere_date 
    FROM movies WHERE movie_name = '{movie}'
    """)
    info = cursor.fetchall()
    database.close()
    return info[0]


def insert_reservation_on_table(movie, date, schedule, user_id, seats, lounge):

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute(f"SELECT movie_id FROM movies WHERE movie_name = '{movie}'")
    movie_id = cursor.fetchone()
    movie_id = movie_id[0]
    cursor.execute(f"""INSERT INTO reservations(reservation_seats, reservation_date, reservation_schedule, user_id, movie_id, lounge_id) VALUES(
        '{seats}', '{date}', '{schedule}', '{user_id}', '{movie_id}', {lounge}
    )""")
    database.commit()
    database.close()