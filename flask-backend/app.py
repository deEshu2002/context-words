from miningLogic import get_words
from flask import Flask, jsonify
from flask import request, Response
import json5

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> Hello, World! </h1>'

def handle_input(text):
    py_obj = json5.loads(text)
    return py_obj

@app.route('/getWordsFromScenario', methods=['POST'])
def getWordsFromScenario():
    if request.method == 'POST':
        req_data = request.get_data()
        py_obj = handle_input(req_data)
        scenario = py_obj["scenario"]

        out = get_words(scenario)
        response = jsonify(out)
        response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With,Content-Type, Origin, X-Auth-Token')
        # response.headers.add('Access-Control-Allow-Credentials', 'true')
        print(response)
        return response,200