import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def get_spotify_client() -> Spotify:
    scope = "user-library-read playlist-modify-private playlist-read-private"

    sp_oauth = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        show_dialog=True
    )
    return Spotify(auth_manager=sp_oauth)
