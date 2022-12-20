from sqlite3 import *

file_path = 'App\models\database\cinemark.db'

def find_user(email, password):

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users")
    users_list = cursor.fetchall()
    for user in users_list:

        if email in user and password in user:
            database.close()
            return user[0]

    database.close()
    return 0
