from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        query = "SELECT name,password FROM users WHERE name = ? AND password = ?"
        cursor.execute(query, (name, password))
        results = cursor.fetchall()

        if len(results) == 0:
            print("Sorry, invalid details! Try Again")
        else:
            return render_template("login.html")

        connection.close()

    return render_template('index.html')