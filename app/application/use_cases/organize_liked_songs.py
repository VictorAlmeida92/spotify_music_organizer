from collections import defaultdict
from spotipy import Spotify

from app.shared.genre_mapping import normalize_genre
from app.infrastructure.spotify.client import SpotifyClient
from app.infrastructure.playlist.manager import PlaylistManager

def organize_liked_songs(
    sp: Spotify,
    spotify_client: SpotifyClient,
    playlist_manager: PlaylistManager
) -> None:
    print("🎵 Buscando músicas curtidas...")
    tracks = spotify_client.get_liked_tracks()

    genre_to_tracks = defaultdict(list)

    print("🧠 Agrupando músicas por gênero...")
    for track_entity in tracks:
        genre = normalize_genre(track_entity.artist_genres)
        genre_to_tracks[genre].append(track_entity.track_id)

    user_id = playlist_manager.get_user_id()

    if not user_id:
        print("❌ Não foi possível obter o ID do usuário.")
        return

    print("📂 Criando playlists e adicionando músicas...")
    for genre, track_ids in genre_to_tracks.items():
        playlist_name = f"{genre} - Auto Playlist"

        playlist_manager.delete_playlist_if_exists(playlist_name)
        playlist_id = playlist_manager.get_or_create_playlist(user_id, playlist_name)

        if not playlist_id:
            print(f"⚠️ Não foi possível criar playlist '{playlist_name}'.")
            continue

        playlist_manager.add_tracks_to_playlist(playlist_id, track_ids)

        print(f"✅ Playlist '{playlist_name}' criada com {len(track_ids)} músicas.")

    print("🎉 Organização concluída com sucesso!")