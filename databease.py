import sqlite3

def createfoodstable():
    database = sqlite3.connect('dp.sqlite')
    cursor = database.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS foods(
    chat_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name VARCHAR,
    price INTEGER,
    about VARCHAR,
    )
    ''')
    database.commit()
    database.close()
createfoodstable()

def registeruser(full_name, user_name, chat_id):
    database = sqlite3.connect('dp.sqlite')
    cursor = database.cursor()
    cursor.execute('''INSERT INTO users(fullname, username, chatid)
    VALUES(?,?,?)''', (full_name, user_name, chat_id))
    database.commit()
    database.close()