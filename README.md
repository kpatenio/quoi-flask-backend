# QUOI
The app to use when ask yourself « Quoi  » !

## About
This Flask app utilizes the [Collins Dictionary API](https://www.collinsdictionary.com/api/) to retrieve information from the Collins server via HTTP calls. Once the API call is made, the app returns this information to the [frontend React app](https://github.com/kpatenio/quoi-react-app).

For more information about this project's history and/or progress, see the wiki [here](https://github.com/kpatenio/QUOI/wiki).

## Running the Server
At the moment, the server can only be run using `python`. Note that using `flask run` does not currently work.

If you are using Windows (Python 3):
```
py -3 app.py
```

If you are using unix (Python 3):
```
python3 app.py
```

Considering that the app is not yet deployed, the server will temporarily be hosted manually at `http://127.0.0.1:5000/`. This means that `quoi-react-app` is heavily dependent on this app being run at localhost.
