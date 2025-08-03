from app.infrastructure.spotify.auth import get_spotify_client
from app.application.use_cases.organize_liked_songs import organize_liked_songs

def main():
    print("🔐 Autenticando no Spotify...")
    sp = get_spotify_client()
    organize_liked_songs(sp)

if __name__ == "__main__":
    main()
