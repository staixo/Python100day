import requests
import base64
import certifi
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
# Disable SSL verification
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# export SPOTIPY_CLIENT_ID='c198e162ca1840c28762ef0ca456d9e4'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

class Spotify():
    def __init__(self):
        self.user_id = "henri.peters"
        self.client_url = "http://api.spotify.com/v1/users/{user_id}"
        self.client_id = "c198e162ca1840c28762ef0ca456d9e4"
        self.client_secret = open("Python100day/Intermediate/AutomateSpotifyPlaylist/spotify.bd", "r").read()
        self.redirect_uri = "http://example.com"
        self.username = "Henri"
        self.scope = "user-library-read"       

    def get_access_token(self):
        url = 'https://accounts.spotify.com/api/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        response = requests.post(url, headers=headers, data=data, verify=False)
        # Extract the access token from the response
        self.header ={
            "access_token": response.json()['access_token'],
            "token_type": "Bearer",
            "expires_in": 3600
            }
    def createplaylist(self, name, description):
        self.body={
        "name": name,
        "description": description,
        "public": False
        }
        pass
    def addtoplaylist(self):
        "https://api.spotify.com/v1/users/{user_id}/playlists"
        pass
    def getplaylist(self):
        pass
    def searchsong(self):
        scope = "user-library-read"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri,scope=scope))

        results = sp.current_user_saved_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])
