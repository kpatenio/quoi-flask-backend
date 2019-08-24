from flask import Flask
from flask_cors import CORS
import constants
import json
import requests # python library for making http requests

app = Flask(__name__) # TODO - Flask(__name__, static_folder=path, template_folder=path)
CORS(app)

# TODO - toggle english-french and french-english
dict_code = 'english-french'
base_url = constants.URL + 'dictionaries/' + dict_code + '/'

@app.route('/')
def get_homepage():
    return "Welcome to the index page!"

@app.route('/<word>')
def get_entry(word):
    response = requests.get(base_url + 'search/first/?q=' + word, headers=constants.HEADERS)
    return response.json()

# TODO
# Sends html of entry back to react app
# def get_entry_url(word_id) # FIXME - when reading url, it is by default in http. If it fails, change to https!
    # response = requests.get(base_url + 'entries/') #entries/{entry_id}?format=html

if __name__ == '__main__':
    app.run(debug=True)

