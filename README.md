# QUOI
The Python Flask backend of QUOI.

## About
This is a work-in-progress, React+TypeScript, personal side project that allows users to instantly see definitions of English-French words via the Collins Dictionary API.

For more information about this project's history and/or progress, see the wiki [here](https://github.com/kpatenio/QUOI/wiki).

## What It Does
This Flask app utilizes the [Collins Dictionary API](https://www.collinsdictionary.com/api/) to retrieve information from the Collins server via HTTP calls. Once the API call is made, the app returns this information to the [frontend React app](https://github.com/kpatenio/quoi-react-app).

## Starting Flask
Currently, no venv has been set up. The temporary workaround is use PyCharm to run the app.

## Server
Considering the app is not yet deployed, the server will be hosted at `http://127.0.0.1:5000/` for the time being.
