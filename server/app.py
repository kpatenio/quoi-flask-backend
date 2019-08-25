from flask import Flask
from flask import request
from flask_cors import CORS
import constants
import json
import requests # python library for making http requests
import app_utils

app = Flask(__name__) # TODO - Flask(__name__, static_folder=path, template_folder=path) 
CORS(app)

@app.route('/')
def get_homepage():
    return "This is the index page!"

@app.route('/<dict_code>/<word>')
def get_entry(dict_code,word):
    base_url = constants.URL + dict_code + '/'
    response = requests.get(base_url + 'search/first/?q=' + word, headers=constants.HEADERS)

    # if word does not exist, show "did you mean" results
    if 'errorCode' in response.json():
        # TODO - rename app_utils to utils or api_utils?
        new_response = app_utils.did_you_mean(dict_code, word)
        return new_response
    else:
        return response.json()

if __name__ == '__main__':
    app.run(debug=True)

