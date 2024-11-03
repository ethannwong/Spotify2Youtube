import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from spotipy.oauth2 import SpotifyClientCredentials
import google.oauth2.credentials
import google_auth_oauthlib.flow
import argparse
import os
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv
print("hi")
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://localhost:3333/callback"
# SPOTIFY_SCOPE = "user-library-read playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, ["user-library-read","user-library-read-private","playlist-read-private"],open_browser=False))

print("connecting to Spotify")
spotify_playlist=[]
length_of_playlist=(sp.current_user_saved_tracks()['total'])

def playlist_formatter(start=0,end=length_of_playlist):
    if (end%50)>0:
        remainder=True
    else:
        remainder=False
    playlist_end_index=end%50
    p_remainder=end//50
    print("start and end is :", start,end)
    print("remainder offset and remainder is", p_remainder*50, remainder)

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

# playlist=playlist_formatter(5,57) 

#!/usr/bin/python

# This code sample creates a private playlist in the authorizing user's
# YouTube channel.
# Usage:
#   python playlist_updates.py --title=<TITLE> --description=<DESCRIPTION>

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    
CLIENT_SECRETS_FILE = 'client_secret.json'

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
    
# Authorize the request and store authorization credentials.
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_local_server(port=0)
#   credentials = flow.run_console()

  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
    
def add_playlist(youtube, args):
  
  body = dict(
    snippet=dict(
      title=args.title,
      description=args.description
    ),
    status=dict(
      privacyStatus='private'
    ) 
  ) 
    
  playlists_insert_response = youtube.playlists().insert(
    part='snippet,status',
    body=body
  ).execute()

  print ('New playlist ID: %s' % playlists_insert_response['id'])
  return (playlists_insert_response['id'])
def add_playlist_item(youtube, videoId, playlistId):
  body = dict(
     kind="youtube#playlistItem",
     snippet=dict(
        playlistId=str(playlistId),
        resourceId=dict(
           kind="youtube#video",
           videoId=str(videoId)
           )
      ) 
    ) 
    
  playlists_items_insert_response = youtube.playlistItems().insert(
    part='snippet',
    body=body
  ).execute()


  print("added a song!")
   
DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(songNameandArtistName):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=songNameandArtistName,
    part='id,snippet',
    maxResults=5 
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
       return (search_result['id']['videoId'])
    
def Converter(youtube, args):
   ytPlaylistID=add_playlist(youtube,args)
   sp2=playlist_formatter(args.start_index,args.end_index)

   for songSubArray in range(len(sp2)):
      #searches for song and saves first result
      youtubeSongFirstResultID=(youtube_search(sp2[songSubArray][1]+sp2[songSubArray][2]+"lyrics"))
      #adds song
      add_playlist_item(youtube,youtubeSongFirstResultID,str(ytPlaylistID) )
  
if __name__ == '__main__':
           
  parser = argparse.ArgumentParser()
  parser.add_argument('--start_index','-s', 
                      type=int, 
                      default=0,
                      help='The starting index of your spotify playlist that you want converted')
  parser.add_argument('--end_index', '-e',
                      type=int,
                      default=1, 
                      help="The ending index of your spotify playlist that you want converted, default=1")
  parser.add_argument('--title','-t',
      default='Test Playlist',
      help='The title of the new playlist.')
  parser.add_argument('--description', '-d',
      default='A private playlist created with the YouTube Data API.',
      help='The description of the new playlist.')
  
  args = parser.parse_args()
    
  youtube = get_authenticated_service()
  try:
     Converter(youtube,args)
  except HttpError as e:
    print ('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
