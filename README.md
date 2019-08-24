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

### Using `venv`(s)
Optionally, you may create your own virtual environments. This is recommended if you want to isolate this app's Python packages from your own. You will need to install the required packages (via `pip 3` or `pip3.7`) within a `venv` in order to run the app locally! [The official documentation (Python 3.7)](https://docs.python.org/3/library/venv.html) is your best resource.

**Commands found in this section will only work if you are using Linux (Ubuntu) and `apt`)**.

#### Downloading `venv`s
`Python 3.x` usually comes with `venv` support. However, if you are unable to use and create `venv`s for some reason, you may need to install `venv` packages separately.

If you only have Python 3.7 installed:
```
sudo apt install python3-venv
```

If you have multiple versions of Python already installed, you will need to specify a version explicitly:
```
sudo apt install python3.7-venv
```

#### Creating `venv`s
Note that newly created `venv`s will be created at the current path you are in.

If you only have Python 3.7 installed:
```
python3 -m venv <pick a name for your venv>
```

If you have multiple versions of Python already installed, you will need to specify a version explicitly:
```
python3.7 -m venv <pick a name for your venv>
```

#### Enabling a `venv`:

```
. <name of your venv>/bin/activate
```

Alternatively, you may run:
```
source <name of your venv>/bin/activate
```

#### Disabling a `venv`:
```
deactivate
```

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

Note: if you wish to use a `venv`, make sure you activate it first before running the commands above!

### Setup with multiple versions of Python installed
If you are using Windows:
```
py -3.7 app.py
```

If you are using unix:
```
python3.7 app.py
```
Note: if you wish to use a `venv`, make sure you activate it first before running the commands above!

### Localhost
Considering that the app is not yet deployed, the server will temporarily be hosted manually at `http://127.0.0.1:5000/`. This means that `quoi-react-app` is heavily dependent on this app being run at localhost.
