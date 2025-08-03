from typing import List, Dict
from spotipy import Spotify

def add_tracks_to_playlist(sp: Spotify, playlist_id: str, track_ids: List[str], batch_size: int = 100) -> None:
    existing_track_ids = set()
    offset = 0

    while True:
        response = sp.playlist_items(
            playlist_id,
            offset=offset,
            fields="items.track.id,total",
            additional_types=["track"]
        ) or {}

        items = response.get("items", [])
        if not items:
            break

        for item in items:
            track = item.get("track") or {}
            track_id = track.get("id")
            if track_id:
                existing_track_ids.add(track_id)

        offset += len(items)

    # Filtra faixas novas
    new_tracks = [track_id for track_id in track_ids if track_id not in existing_track_ids]

    # Adiciona em lotes
    for i in range(0, len(new_tracks), batch_size):
        batch = new_tracks[i:i + batch_size]
        sp.playlist_add_items(playlist_id, batch)

def get_user_id(sp: Spotify) -> str:
    user = sp.current_user()
    if user is None or "id" not in user:
        raise RuntimeError("Não foi possível obter o ID do usuário.")
    return user["id"]


def get_or_create_playlist(sp: Spotify, user_id: str, playlist_name: str) -> str:
    response = sp.current_user_playlists(limit=50)
    if response is None or "items" not in response:
        raise RuntimeError("Não foi possível obter as playlists do usuário.")

    for playlist in response["items"]:
        if playlist.get("name", "").lower() == playlist_name.lower():
            return playlist["id"]

    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    if new_playlist is None or "id" not in new_playlist:
        raise RuntimeError(f"Não foi possível criar a playlist: {playlist_name}")

    return new_playlist["id"]


def delete_playlist_if_exists(sp: Spotify, playlist_name: str):
    response = sp.current_user_playlists(limit=50)
    if response is None or "items" not in response:
        return

    for playlist in response["items"]:
        if playlist.get("name", "").lower() == playlist_name.lower():
            sp.current_user_unfollow_playlist(playlist["id"])
            break


def create_genre_playlists(sp: Spotify, user_id: str, genre_to_tracks: Dict[str, List[str]]):
    for genre, track_ids in genre_to_tracks.items():
        if not track_ids:
            continue

        playlist_name = f"{genre.title()} Vibes"
        delete_playlist_if_exists(sp, playlist_name)
        playlist_id = get_or_create_playlist(sp, user_id, playlist_name)

        # Spotify só aceita no máximo 100 faixas por requisição
        for i in range(0, len(track_ids), 100):
            sp.playlist_add_items(playlist_id, track_ids[i:i + 100])
