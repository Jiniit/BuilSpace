from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random

app = Flask(__name__)

# Create the SQLite database and table
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS questions (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       question_text TEXT NOT NULL,
       choice1 TEXT NOT NULL,
       choice2 TEXT NOT NULL,
       choice3 TEXT NOT NULL,
       choice4 TEXT NOT NULL,
       correct_choice INTEGER NOT NULL
   )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
   question_text = request.form['question']
   choice1 = request.form['choice1']
   choice2 = request.form['choice2']
   choice3 = request.form['choice3']
   choice4 = request.form['choice4']
   correct_choice = int(request.form['correct_choice'])

   # Insert the question, choices, and correct choice into the database
   conn = sqlite3.connect('questions.db')
   cursor = conn.cursor()
   cursor.execute('INSERT INTO questions (question_text, choice1, choice2, choice3, choice4, correct_choice) VALUES (?, ?, ?, ?, ?, ?)',
                  (question_text, choice1, choice2, choice3, choice4, correct_choice))
   conn.commit()
   conn.close()

   return redirect(url_for('index'))

@app.route('/get_question')
def get_question():
   # Fetch a random question from the database
   conn = sqlite3.connect('questions.db')
   cursor = conn.cursor()
   cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1')
   question = cursor.fetchone()
   conn.close()

   return render_template('question.html', question=question)

@app.route('/answer', methods=['POST'])
def answer():
   selected_choice = int(request.form['choice'])
   question_id = int(request.form['question_id'])

   # Retrieve the correct answer from the database
   conn = sqlite3.connect('questions.db')
   cursor = conn.cursor()
   cursor.execute('SELECT correct_choice FROM questions WHERE id = ?', (question_id,))
   correct_choice = cursor.fetchone()[0]
   conn.close()

   # Determine if the selected answer is correct
   is_correct = (selected_choice == correct_choice)

   return render_template('answer.html', is_correct=is_correct)

if __name__ == '__main__':
   app.run(debug=True)
