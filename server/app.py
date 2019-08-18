from flask import Flask
from flask_cors import CORS
import constants
import json
''' 
python library for making http requests
see: https://realpython.com/python-requests/#getting-started-with-requests
see: https://2.python-requests.org/en/master/user/quickstart

Note: this is different from Flask's request object - which is used for reading responses sent to the server!
'''
import requests

app = Flask(__name__) # TODO - Flask(__name__, static_folder=path, template_folder=path)
CORS(app) # enables CORS for the flask server. see: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

# TODO - toggle english-french and french-english
dict_code = 'english-french'

base_url = constants.URL + 'dictionaries/' + dict_code + '/'

@app.route('/')
def get_homepage():
    return "Welcome to the index page!"

# TODO - dynamic URLs - https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
# TODO - rename appropriately with entry id vs search
# TODO - do we want ALL search results to be available?
# @app.route('/<word>')
def get_search_results(word):
    response = requests.get(base_url + 'search/?q=' + word + '&pageSize=1', headers=constants.HEADERS)
    return response.json() # FIXME - see if we can make a non-json version for other helper functions

# TODO - a helper function
@app.route('/<word>')
def get_entry(word):
    try:
        entry_data = get_entry_label_id(word)
    except:
        return False # FIXME - do better error handling
    entry_label = entry_data[0]
    entry_id = entry_data[1]
    response = requests.get(base_url + 'entries/' + entry_id + '?format=html', headers=constants.HEADERS)
    return response.json()

# helper function
def get_entry_label_id(word):
    response_dict = get_search_results(word)
    # response_dict = json.loads(response)
    # FIXME - find a better searching algorithm!
    # Follow this format! --> response_dict['results'][index]['entryLabel']
    results = response_dict['results'] # results returns a long list of dicts
    for i in range(0, len(results)):
        if (word == results[i]['entryLabel']):
            # (label, id)
            return (word, results[i]['entryId'])


# TODO
# Sends html of entry back to react app
# def get_entry_url(word_id) # FIXME - when reading url, it is by default in http. If it fails, change to https!
    # response = requests.get(base_url + 'entries/') #entries/{entry_id}?format=html

if __name__ == '__main__':
    app.run(debug=True)

