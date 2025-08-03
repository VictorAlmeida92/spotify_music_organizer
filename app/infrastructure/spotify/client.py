from typing import List, Dict, Any
from spotipy import Spotify
from app.domain.entities.track import Track as DomainTrack

class SpotifyClient:
    def __init__(self, sp: Spotify):
        self.sp = sp

    def get_liked_tracks(self, limit: int = 50) -> List[DomainTrack]:
        tracks_list: List[DomainTrack] = []
        offset = 0

        while True:
            response = self.sp.current_user_saved_tracks(limit=limit, offset=offset) or {}
            items = response.get("items", [])
            if not items:
                break

            for item in items:
                track = item.get("track")
                if not track:
                    continue

                track_id = track.get("id")
                artists = track.get("artists")
                if not artists:
                    continue

                artist_id = artists[0].get("id")
                if track_id and artist_id:
                    artist = self.sp.artist(artist_id) or {}
                    artist_genres = artist.get("genres", [])
                    tracks_list.append(DomainTrack(track_id, artist_id, artist_genres))

            offset += limit

        return tracks_list