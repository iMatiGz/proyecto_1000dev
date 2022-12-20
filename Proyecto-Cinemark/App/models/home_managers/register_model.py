from sqlite3 import *

file_path = 'App\models\database\cinemark.db'

def user_already_exists(email):

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users")
    users_list = cursor.fetchall()
    for user in users_list:
        
        if email in user:
            database.close()
            return True

    database.close()
    return False


def register_user(email, username, password, permissions):

    database = connect(file_path)
    cursor = database.cursor()
    cursor.execute(f"""INSERT INTO users(user_email, user_username, user_password, user_permissions) VALUES(
        '{email}', '{username}', '{password}', {permissions}
    )
    """)
    database.commit()
    database.close()