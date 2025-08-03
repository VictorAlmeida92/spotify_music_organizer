from typing import List, Dict, Any
from spotipy import Spotify


def get_liked_tracks(sp: Spotify, limit: int = 50) -> List[Dict[str, Any]]:
    tracks: List[Dict[str, Any]] = []
    offset = 0

    while True:
        response = sp.current_user_saved_tracks(limit=limit, offset=offset) or {}
        items = response.get("items", [])
        if not items:
            break
        tracks.extend(items)
        offset += limit

    return tracks


def get_artist_genres(sp: Spotify, artist_id: str) -> List[str]:
    artist = sp.artist(artist_id)
    if not artist:
        return []
    genres = artist.get("genres")
    return genres if isinstance(genres, list) else []
