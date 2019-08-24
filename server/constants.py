import os

URL = 'https://api.collinsdictionary.com/api/v1/'

HEADERS = {
    'Host': 'api.collinsdictionary.com',
    'Accept': 'application/json',
    'accessKey': os.environ['ACCESS_KEY']
}