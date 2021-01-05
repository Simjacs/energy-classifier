import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


def connect_to_api():
    cid = "2bd837c837174d50ab873c61acf24f68"
    secret = "033bb4a851d54615bf83aaf94239ee06"
    username = "omkwppodx5qi1pph0cwma65zc"
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    scope = 'user-library-read playlist-read-private streaming user-modify-playback-state user-read-playback-state'
    token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret,
                                       redirect_uri="http://localhost/")
    if token:
        sp = spotipy.Spotify(auth=token)
        return sp
    else:
        print("Can't get token for", username)


def get_tracks_from_playlist_name(user_id, playlist_name):

    return


def get_artist_id_from_name():
    return


def get_related_artists_from_id():
    return


def get_tracks_from_artist_id():
    return


def get_attributes_from_track_id_list():
    return





