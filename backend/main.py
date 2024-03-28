import time
from flask import Flask, request, url_for, session, redirect
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
#creating a temp cookie to load faster
app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
#creating a dummy key to access
app.secret_key = 'abcd123'
#authentication token 
TOKEN_INFO = 'token_info'

@app.route('/')
def login():
    #calling the authorization function 
    auth_url = create_spotify_oauth().get_authorize_url()
    #this will retunr the url for it 
    return redirect(auth_url)

@app.route('/redirect')
def redirect_():
    #create a new session
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('authenticate', _external=True))

@app.route('/authenticate')
def authenticate():
    try:
        token_info = get_token()
        return "OAUTH Successful"
    except:
        print("User not logged in")
        return redirect('/')

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        return redirect(url_for('login', _external=False))
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id='a8dd8b7decf845e1b7becdc8dbb909e3',
        client_secret="c6cfafd242384321b9c4aa81b58fb5fd",
        redirect_uri=url_for('redirect_', _external=True),
        scope='user-top-read'
    )

if __name__ == '__main__':

    app.run(debug=True, port=5000, host='128.197.29.253')