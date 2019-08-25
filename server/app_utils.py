import constants
import json
import requests # python library for making http requests

# TODO - maybe this is not a function to be found in utils
def did_you_mean(dict_code, word):
    base_url = constants.URL + dict_code +'/'
    response = requests.get(base_url + 'search/didyoumean?q=' + word + '&entrynumber=10', headers=constants.HEADERS)
    return response.json()
