import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

# command = "CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"
cursor.execute("INSERT INTO users VALUES('jim','jim-password')")
connection.commit()