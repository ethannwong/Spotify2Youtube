# Spotify2Youtube

A Python script to help convert Spotify Liked Songs to a Youtube Music playlist

Python version used: 3.13.0

I believe you can use convert ~65 songs daily due to Google's api quota.
## DEMO
<img src="it works.gif"/>
Screen is hidden right before running the script to avoid showing my emails, as running the script opens a pop-up immediately.




Before Starting:

You need to create your web api app from spotify which will give you a client id and client secret. You should also add the email associated with your Spotify account as a test user for it to work.

https://developer.spotify.com/

You will also need a Google account which you will use to register to create a project in the Google's developer console. 
You have to add the youtube data api v3 to your API library. After doing so you should
be able to see it under Enabled APIs and services.
You need to make an API key, and a OAuth 2.0 Client ID in the Credentials section. 
Once you finish that download the json file from your OAuth 2.0 client ID and rename it as client_secret.json. 
You have to move this into your cloned project directory later.
ALSO add the email you want the playlist to be created in as a test user.

https://developers.google.com/youtube/v3/getting-started

Follow the steps below right and stop right before running the script. Make an .env file in your project directory which should look like: 
```
SPOTIFY_CLIENT_ID='SPOTIFY_CLIENT_ID'
SPOTIFY_CLIENT_SECRET='SPOTIFY_CLIENT_SECRET'
DEVELOPER_KEY='DEVELOPER_KEY'

```
and replace the strings with your own credentials.

## Setup for Windows Users:

```
cd /path/{for_your_project}

Set-ExecutionPolicy Unrestricted -Scope Process  # if venv\Scripts\activate doesn't work

py -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

# Finish the steps above before running it 

py Spot2Utube.py -s {starting index} -e {ending index} -t {Playlist title} 
# or python Spot2Utube.py with the above arguments
```

