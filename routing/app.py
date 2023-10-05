from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    blog_title = "Welcome to My Blog"
    blog_content = "This is a blog about various topics."
    return render_template('home.html', title=blog_title, content=blog_content)

@app.route('/account/<username>')
def account(username):
    return render_template('account.html', username=username)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
