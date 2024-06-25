from flask import Flask, request, jsonify
from joke import get_joke, search_jokes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'Hello, Jokes!'
#here 2 endpoints display and search joke
@app.route('/display_joke/<category>')
def display_joke(category):
    flags = request.args.get('flags', default = "", type = str)
    joke = get_joke(category, flags)
    return jsonify({'joke': joke})

@app.route('/search_joke/<term>')
def search_joke(term):
    joke = search_jokes(term)
    return jsonify({'joke': joke})

if __name__ == '__main__':
    app.run(debug=True)
