import flask
import pymongo

from flask import request, jsonify
from flask import Response
from pymongo import MongoClient


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/health/live', methods=['GET'])
def live_check():
    return "Healthy"

@app.route('/health/ready', methods=['GET'])
def ready_check():
    return "Healthy"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    client = MongoClient()
    db = client.test
    books = db.books
    cur = books.find()
    result = []
    for item in cur:
        if "title" in item:
          result.append({"title": item["title"], "description": item["description"]})


    return jsonify(result)


@app.route('/api/v1/resources/add', methods=['POST'])
def add_book():
    
    client = MongoClient()
    db = client.test
    books = db.books

    book = request.json
    result = books.insert_one(book)
    
    return result


app.run()