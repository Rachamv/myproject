from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.route('/index')
def home():
    return "Welcome to my web app!"

@app.route('/about', methods=['GET'])
def about():
    return "<h1>Hello</h1>"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}!"

@app.route('/api/data', methods=['GET'])
def api_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

@app.route('/users/<username>')
def user_profile(username):
    return f"Welcome to the profile page of {username}."

@app.route('/search')
def search():
    query = request.args.get('query')
    sort_order = request.args.get('sort')
    return f"Searching for: {query}, sorted in {sort_order} order."

if __name__ == '__main__':
    app.run()