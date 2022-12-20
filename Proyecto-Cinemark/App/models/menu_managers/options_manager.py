from sqlite3 import *

file_path = 'App\models\database\cinemark.db'

def get_username(user_id):

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute(f"SELECT user_username FROM users WHERE user_id = {user_id}")
    username = cursor.fetchone()
    database.close()
    return username[0]