"""
script takes name of playlist and user id and extends playlist by adding songs within playlist parameters
"""
import spotipy
import pandas as pd
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pickle as pkl

# authenticate to the API
# TODO: remove secrets and ids from source code. do not push to git until done
cid ="2bd837c837174d50ab873c61acf24f68" 
secret = "033bb4a851d54615bf83aaf94239ee06"
username = "omkwppodx5qi1pph0cwma65zc"  # this is the username
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private streaming user-modify-playback-state user-read-playback-state'
token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri="http://localhost/")
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)


