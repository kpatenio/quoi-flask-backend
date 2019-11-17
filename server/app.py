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

# @app.route('/<dict_code>/<word>')
def get_best_matching(dict_code,word):
    base_url = constants.URL + dict_code + '/'
    response = requests.get(base_url + "search/first/?q=" + word, headers=constants.HEADERS)

    # if word does not exist, show "did you mean" results
    # if 'errorCode' in response.json():
    #     # TODO - rename app_utils to utils or api_utils?
    #     new_response = app_utils.did_you_mean(dict_code, word, 10)
    #     return new_response
    # else:
    return response.json()

# TODO - maybe instead of calling get_best_matching directly, let's call "get an entry" instead of "best matching"

@app.route('/<dict_code>/<word>')
def get_entry(dict_code, word):
    base_url = constants.URL + dict_code + '/'

    # let's add "_1" to the word input to make it a valid id
    word_id = "{}_1".format(word)
    get_request = "{}entries/{}".format(base_url, word_id)
    print(get_request)
    response = requests.get(get_request, headers=constants.HEADERS)
    print(response)
    return response.json()

@app.route('/<dict_code>/<current_input>/auto')
def auto_complete(dict_code, current_input):
    base_url = constants.URL + dict_code + '/'
    # response = get_entry(dict_code, currentInput)
    # entry_id = response["entryId"]
    # entry_label = response["entryLabel"]

    current_input_id = "{}_1".format(current_input)
    # nearby = requests.get(base_url + "entries/" + entry_id + "/nearbyentries?entrynumber=5", headers=constants.HEADERS)
    nearby = requests.get(base_url + "entries/" + current_input_id + "/nearbyentries?entrynumber=5", headers=constants.HEADERS)
    # response = app_utils.did_you_mean(dict_code, word, 5)

    # nearbyFollowingLabels = [entry_label]
    nearbyFollowingLabels = [current_input]

    if "nearbyFollowingEntries" not in nearby.json():
        # TODO - figure out the proper type of thing to return as a part of REST specs
        return {
            "errorMessage": "Doesn't exist!"
        }

    for nearby_entry in nearby.json()["nearbyFollowingEntries"]:
       nearbyFollowingLabels.append(nearby_entry["entryLabel"])
    print(nearbyFollowingLabels)

    # result = nearbyFllowingLabels.insert(0, entry_id)

    new_response = {
        # "currentId": entry_id,
        "currentId": current_input_id,
        "results": nearbyFollowingLabels
        # "nearbyFollowingEntries": nearbyFollowingLabels,
        # "results": result
    }

    return new_response

if __name__ == '__main__':
    app.run(debug=True)

