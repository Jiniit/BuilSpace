from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def blog():
    blog_data = {
        'title': 'Blog Post',
        'author': 'Agatha Christie',
        'content': 'The famous detective writer of all time, she has wrote the worlds longest running play, The Mousetrap.'
    }
    return render_template('blog.html', **blog_data)

if __name__ == '__main__':
    app.run(debug=True)
