# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list to store tasks as objects
tasks = []

class Task:
    def __init__(self, text):
        self.text = text
        self.done = False

@app.route('/')
def todo_list():
    return render_template('todo.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task_text = request.form.get('task')
    if new_task_text:
        new_task = Task(new_task_text)
        tasks.append(new_task)
    return redirect(url_for('todo_list'))

if __name__ == '__main__':
    app.run(debug=True)
