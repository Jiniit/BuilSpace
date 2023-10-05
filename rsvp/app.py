from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('rsvp.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rsvp (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        response TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    response = request.form['response']

    conn = sqlite3.connect('rsvp.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rsvp (name, response) VALUES (?, ?)', (name, response))
    conn.commit()
    conn.close()

    return redirect(url_for('list_rsvps'))

@app.route('/list_rsvps')
def list_rsvps():
    conn = sqlite3.connect('rsvp.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rsvp')
    rsvps = cursor.fetchall()
    conn.close()

    return render_template('rsvp_list.html', rsvps=rsvps)

if __name__ == '__main__':
    app.run(debug=True)
