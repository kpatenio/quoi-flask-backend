from flask import Flask
from flask_cors import CORS
import constants
''' 
python library for making http requests
see: https://realpython.com/python-requests/#getting-started-with-requests
see: https://2.python-requests.org/en/master/user/quickstart

Note: this is different from Flask's request object - which is used for reading responses sent to the server!
'''
import requests

app = Flask(__name__) # TODO - Flask(__name__, static_folder=path, template_folder=path)
CORS(app) # enables CORS for the flask server. see: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

@app.route('/')
def index():
    return "Welcome! This is the index page!"

# TODO
# def get_dictionary_code()

dict_code = 'english-french'

# TODO - dynamic URLs - https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
# TODO - rename appropriately with entry id vs search
@app.route('/<word>')
def get_search_term(word):
    response = requests.get(constants.URL + 'dictionaries/' + dict_code + '/search/?q=' + word + '&pageSize=1', headers=constants.HEADERS)
    # return(str(constants.URL + 'dictionaries/' + dict_code + '/search/?q=' + word))
    # return response.json()
    return response.json()
# TODO
# def get_entry_id

# TODO
# Sends html of entry back to react app
# def get_entry_url -- note: # FIXME - when reading url, it is by default in http. If it fails, change to https!

if __name__ == '__main__':
    app.run(debug=True)

