import flask
import pymongo
import os

from flask import request, jsonify
from flask import Response
from pymongo import MongoClient


app = flask.Flask(__name__)
app.config["DEBUG"] = True

if "MONGO_HOST" in os.environ:
    mongo_host = os.environ["MONGO_HOST"]
else:
    mongo_host = "localhost"

if "MONGO_PORT" in os.environ:
    mongo_port = os.environ["MONGO_PORT"]
else:
    mongo_port = 27017

client = MongoClient(mongo_host, mongo_port)
db = client.test


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
@app.route('/api/v1/books', methods=['GET'])
def api_all():
    result = []
    for item in db.books.find():
        if "title" in item:
          result.append({"title": item["title"], "description": item["description"]})
    return jsonify(result)


@app.route('/api/v1/books/add', methods=['POST'])
def add_book():
    book = request.json
    result = db.books.insert_one(book).inserted_id
    
    return jsonify(str(result))

app.run(host='0.0.0.0')