# from flask import Flask
#
# # requests is a python library used for making http requests
# # main documentation: https://2.python-requests.org/en/master/
# # another great guide: https://realpython.com/python-requests/
# import requests
#
# app = Flask(__name__)
#
# @app.route('/')
# def helloworld():
#     return 'hello world'
#
# @app.route('/hello')
# def hello():
#     return 'hello'
#
# @app.route('/world')
# def world():
#     return 'world'
#
# @app.route('/test')
# def test():
#     host = 'api.collinsdictionary.com'
#     access_key = 'bEbubPMmAVlNHJZMaUnrMRwUGHsOis2MUxBzPLUgWiHrrhzYaO1itOnvwZceAMUs'
#     accept = 'application/json'
#     headers = {
#         'Host': host,
#         'Accept': accept,
#         'accessKey': access_key
#     }
#     response = requests.get('https://api.collinsdictionary.com/api/v1/dictionaries', headers=headers)
#     return str(response.text)
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#     # TODO -
#
#     # TODO - https://www.youtube.com/watch?v=Z1RJmh_OqeA