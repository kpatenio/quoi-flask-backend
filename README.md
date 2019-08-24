# QUOI
The app to use when ask yourself « Quoi  » !

## About
This Flask app utilizes the [Collins Dictionary API](https://www.collinsdictionary.com/api/) to retrieve information from the Collins server via HTTP calls. Once the API call is made, the app returns this information to the [frontend React app](https://github.com/kpatenio/quoi-react-app).

For more information about this project's history and/or progress, see the wiki [here](https://github.com/kpatenio/QUOI/wiki).

## Requirements
Virtual environments are set up on my local computer, each with different modules installed via `pip`. To run the server on your own local environment, you must have the following:
- `Python 3.7`
- `Flask (>= 1.1.1)`
- `Flask-Cors (>= 3.0.8)`

Note that `Python 3.7` is needed in order to utilize this version's [Data Class feature](https://docs.python.org/3/library/dataclasses.html).

## Running the Server
At the moment, the server can only be run by executing the `app.py` file with your Python interpreter. Note that using `flask run` does not currently work!

### Setup with only Python 3.7 installed
If you are using Windows:
```
py app.py
```

If you are using unix:
```
python app.py
```

### Setup with multiple versions of Python installed
If you are using Windows:
```
py -3.7 app.py
```

If you are using unix:
```
python3.7 app.py
```

### Localhost
Considering that the app is not yet deployed, the server will temporarily be hosted manually at `http://127.0.0.1:5000/`. This means that `quoi-react-app` is heavily dependent on this app being run at localhost.
