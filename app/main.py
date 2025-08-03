from app.infrastructure.spotify.auth import get_spotify_client
from app.infrastructure.spotify.client import SpotifyClient
from app.infrastructure.playlist.manager import PlaylistManager
from app.application.use_cases.organize_liked_songs import organize_liked_songs

def main():
    print("🔐 Autenticando no Spotify...")
    sp = get_spotify_client()

    spotify_client = SpotifyClient(sp)
    playlist_manager = PlaylistManager(sp)

    organize_liked_songs(sp, spotify_client, playlist_manager)

if __name__ == "__main__":
    main()