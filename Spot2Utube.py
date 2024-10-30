import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from spotipy.oauth2 import SpotifyClientCredentials


import os
from dotenv import load_dotenv
print("hi")

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

SPOTIFY_REDIRECT_URI = "http://localhost:1234/callback"
SPOTIFY_SCOPE = "user-library-read playlist-read-private"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, ["user-library-read","user-library-read-private","playlist-read-private"]))



try:
    results = sp.current_user_saved_tracks(limit=50,market="US")
    print(results)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
except spotipy.exceptions.SpotifyException as e:
    print("Error:", e)



# results= sp.current_user_saved_tracks(limit=50,offset=9, market="US")
# print("second hi")
# print(results)
# taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
# results = sp.artist_albums(taylor_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = sp.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

# scope = 'playlist-read-private'
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_playlists(limit=50)
# print(results)
# for i, item in enumerate(results['items']):
#     print("%d %s" % (i, item['name']))

# taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

# results = sp.artist_albums(taylor_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = sp.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])