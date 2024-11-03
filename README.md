# Spotify2Youtube

A Python script to help convert your Spotify Liked Songs to a Youtube Music playlist 

Python version used: 3.13.0

Note: I believe you can only convert ~65 songs daily due to Youtube API's quota 

## DEMO
<img src="it works.gif"/>
Screen is hidden right before running the script to avoid showing my emails, as running the script opens a pop-up immediately.

## Before Starting:
You need to create your web api app from spotify which will give you a client id and client secret. 

https://developer.spotify.com/

You also need to include the email associated with your spotify account as a test user.


## Setup for Windows Users:

```
cd /path/{for_your_project}

Set-ExecutionPolicy Unrestricted -Scope Process  # if venv\Scripts\activate doesn't work

py -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

py Spot2Utube.py # or python Spot2Utube.py
```
