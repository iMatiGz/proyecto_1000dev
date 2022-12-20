from sqlite3 import *

file_path = 'App\models\database\cinemark.db'

def create_database():

    database = connect(file_path)
    database.close()


def create_users_table():

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_email text,
        user_username text,
        user_password text,
        user_permissions INTEGER
    )
    """)
    database.commit()
    database.close()


def insert_default_admin():

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute(f"""INSERT INTO users(user_email, user_username, user_password, user_permissions) VALUES(
        'admin', 'Admin', 'admin123', 1
    )
    """)
    database.commit()
    database.close()


def create_movies_table():

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
        movie_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        movie_name text,
        movie_director text,
        movie_gender text,
        movie_length text,
        movie_premiere_date text
    )
    """)
    database.commit()
    database.close()


def insert_movie_on_table(name, director, gender, length, premiere_date):

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute(f"""INSERT INTO movies(movie_name, movie_director, movie_gender, movie_length, movie_premiere_date) VALUES(
        '{name}', '{director}', '{gender}', '{length}', '{premiere_date}'
    )
    """)
    database.commit()
    database.close()


def create_lounges_table():

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS lounges(
        lounge_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        lounge_capability INTEGER,
        movie_id INTEGER NOT NULL,
        FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
    )
    """)
    database.commit()
    database.close()


def create_reservations_table():

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS reservations(
        reservation_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        reservation_seats text,
        reservation_date text,
        reservation_schedule text,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        lounge_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (movie_id) REFERENCES movies (movie_id),
        FOREIGN KEY (lounge_id) REFERENCES lounges (lounge_id)
    )
    """)
    database.commit()
    database.close()
    

if __name__ == "__main__":

    #create_database()
    #create_users_table()
    #insert_default_admin()
    #create_movies_table()
    #create_lounges_table()
    #create_reservations_table()

    insert_movie_on_table(name="Canguro Jack", director="David McNally", gender="Aventura", length="1h 29min", premiere_date="17/01/2003")
    pass