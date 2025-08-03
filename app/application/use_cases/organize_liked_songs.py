from collections import defaultdict
from spotipy import Spotify

from app.domain.services.genre_classifier import normalize_genre
from app.infrastructure.spotify.client import get_liked_tracks
from app.infrastructure.playlist.manager import (
    get_or_create_playlist,
    delete_playlist_if_exists,
    add_tracks_to_playlist
)


def organize_liked_songs(sp: Spotify) -> None:
    print("🎵 Buscando músicas curtidas...")
    tracks = get_liked_tracks(sp)

    genre_to_tracks = defaultdict(list)

    print("🧠 Agrupando músicas por gênero...")
    for item in tracks:
        track = item.get("track")
        if not track:
            continue

        artists = track.get("artists")
        if not artists:
            continue

        artist_id = artists[0].get("id")
        if not artist_id:
            continue

        artist = sp.artist(artist_id) or {}
        artist_genres = artist.get("genres", [])
        genre = normalize_genre(artist_genres)
        track_id = track.get("id")

        if track_id:
            genre_to_tracks[genre].append(track_id)

    user = sp.current_user() or {}
    user_id = user.get("id")

    if not user_id:
        print("❌ Não foi possível obter o ID do usuário.")
        return

    print("📂 Criando playlists e adicionando músicas...")
    for genre, track_ids in genre_to_tracks.items():
        playlist_name = f"{genre} - Auto Playlist"

        # Apaga playlist antiga com mesmo nome
        delete_playlist_if_exists(sp, playlist_name)

        # Cria nova playlist
        playlist_id = get_or_create_playlist(sp, user_id, playlist_name)
        if not playlist_id:
            print(f"⚠️ Não foi possível criar playlist '{playlist_name}'.")
            continue

        # Adiciona faixas (sem duplicar)
        add_tracks_to_playlist(sp, playlist_id, track_ids)

        print(f"✅ Playlist '{playlist_name}' criada com {len(track_ids)} músicas.")

    print("🎉 Organização concluída com sucesso!")
