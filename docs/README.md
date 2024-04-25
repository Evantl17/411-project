# 411-project

Our project is a Spotify Web Application that uses [Flask](https://flask.palletsprojects.com/en/3.0.x/), [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/), [Bootstrap](https://getbootstrap.com/), Python, HTML, and CSS.

Our projcet will give the user an overview of their favorite artists and some information about them! To use our project you must do the following. In the project directory, you can run:

## `pip install flask, requests, spotipy, spotipy.oauth2, python-dotenv, virtualenv`

This installs all of the packages needed.
Then, you need to start the environment and the flask application:

```
virutalenv env
source env/bin/activate
export FLASK_APP=main
```
If we decide to commit our API keys to the GitHub repository then this step will not be necessary:

Create a file called .env and fill it with the following variables:

```
API_KEY = ""
client_id = ""
client_secret = ""
```
Fill these with your respective API keys. 
\
\
The API_KEY variable corresponds to your Google Custom Search JSON API Key. This can be found here: [link](https://developers.google.com/custom-search/v1/introduction). Click on the "Get a Key" button.
\
\
The other two variables are for the spotify API. Getting your access tokens are here: [link](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).

## Running the Application
To run the application simply type 
### `flask run`
into the console and it should bring you to our webpage!


