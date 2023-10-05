from flask import Flask, render_template, request

app = Flask(__name__)

# Define hard-coded responses for specific keywords
keyword_responses = {
    "Flask": "A micro web framework written in Python.",
    "Python": "A high-level programming language known for its simplicity and readability.",
    "Web Development": "The process of building websites or web applications for the internet.",
    "AI": "Artificial Intelligence, the simulation of human intelligence in machines.",
}

@app.route('/', methods=['GET', 'POST'])
def search():
    response = None

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        response = keyword_responses.get(query, "No information available for that keyword.")

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
