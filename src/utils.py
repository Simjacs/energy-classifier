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


def get_playlist_id_from_name(user_id, search_playlist_name):
    sp = connect_to_api()
    try:
        playlists = sp.user_playlists(user_id)
    except spotipy.exceptions.SpotifyException:
        print(f"bad request, no user for {user_id}")
        return False
    i = 0
    while playlists["next"]:
        i += 50
        playlists = sp.user_playlists(user_id, offset=i)
        names = [playlists["items"][j]["name"].lower() for j in range(len(playlists["items"]))]
        if search_playlist_name.lower() in names:
            idx = names.index(search_playlist_name)
            playlist_id = playlists["items"][idx]["id"]
            return playlist_id
    print(f"no such playlist for {search_playlist_name}")
    return False


def get_tracks_from_playlist_id(playlist_id, id_type="uri"):
    sp = connect_to_api()
    tracks = sp.playlist_tracks(playlist_id)["items"]
    return [tracks[i]["track"][id_type] for i in range(len(tracks))]


def get_artist_id_from_name(artist_name: str, id_type="uri"):
    sp = connect_to_api()
    search = sp.search(artist_name, limit=1, type="artist")
    try:
        artist_id = search["artists"]["items"][0][id_type]
    except IndexError:
        print(f"no results for query string: {artist_name}")
        return False
    return artist_id


def get_related_artists_from_id(artist_id: str, id_type="uri"):
    sp = connect_to_api()
    try:
        rel_artists = sp.artist_related_artists(artist_id)["artists"]
    except spotipy.exceptions.SpotifyException:
        print(f"either no such artist for {artist_id}")
        return False
    return [rel_artists[i][id_type] for i in range(len(rel_artists))]


def get_tracks_from_artist_id(artist_id: str, id_type="uri"):
    sp = connect_to_api()
    tracks = sp.artist_top_tracks(artist_id)["tracks"]
    return [tracks[i][id_type] for i in range(len(tracks))]


def get_attributes_from_track_id_list():
    return


if __name__ == "__main__":
    sp = connect_to_api()
    uname = "omkwppodx5qi1pph0cwma65zc"
    playlist_id = get_playlist_id_from_name(uname, "bar jazz")
    playlist_tracks = get_tracks_from_playlist_id(playlist_id)
    




