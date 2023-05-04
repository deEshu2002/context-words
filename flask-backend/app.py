from miningLogic import get_words_using_sentence  
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> Hello, World! </h1>'

@app.route('/getWordsFromScenario', methods=['POST'])
def getWordsFromScenario():
    if request.method == 'POST':
        json = request.get_json()
        request_string = json['string']
        out = get_words_using_sentence(request_string)
        print(out)
        return 'Success Printing',200