from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('word_count.html')

@app.route('/count_words', methods=['POST'])
def count_words():
    text = request.form.get('text')
    words = text.split()
    word_count = len(words)
    return render_template('word_count.html', word_count=word_count)

if __name__ == '__main__':
    app.run(debug=True)
