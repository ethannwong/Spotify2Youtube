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

spotify_playlist=[]
length_of_playlist=(sp.current_user_saved_tracks()['total'])

def playlist_formatter(start=0,end=length_of_playlist):
    if (end%50)>0:
        remainder=True
    else:
        remainder=False
    playlist_end_index=end%50
    p_remainder=end//50
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, ["user-library-read","user-library-read-private","playlist-read-private"]))
    print("start and end is :", start,end)
    print("remainder offset and remainder is", p_remainder*50, remainder)
    ### TO DO
    # find solution for non english characters 
    # test cases for playlists less than 50 songs and playlists from starting index >0 to random ending index
    # just make a seperate testcase but modify it to check if len<50 and if so make the playlist and return it 
    ###

    global_idx=0
    if start !=0:
        first_song=sp.current_user_saved_tracks(limit=1,offset=start-1, market="US")
        # print(first_song)
        spotify_playlist.append([0,first_song['items'][0]['track']['artists'][0]['name'],first_song['items'][0]['track']['name']])
        global_idx+=1
        print(spotify_playlist)

    for i in range(start,end,50):
        results = sp.current_user_saved_tracks(limit=50,offset=i,market="US")
        
        for idx, item in enumerate(results['items']):
            track= item['track']
            
            spotify_playlist.append([global_idx,track['artists'][0]['name'], track['name']])
            global_idx+=1
            if global_idx==(end-start+1):
                break
        print("first iter length: ", len(spotify_playlist)+1 )
        print("index number: ", i)
    
    print("length of spotify_playlist is: " , len(spotify_playlist))
    print(spotify_playlist)
    return(spotify_playlist)

# playlist_formatter(205,367)
playlist_formatter(5,57) 
# playlist_formatter(23,99)
# playlist_formatter(1,56)


# try:
#     results = sp.current_user_saved_tracks(limit=50,market="US")
#     print(results)
#     for idx, item in enumerate(results['items']):
#         track = item['track']
#         print(idx, track['artists'][0]['name'], " – ", track['name'])
# except spotipy.exceptions.SpotifyException as e:
#     print("Error:", e)
