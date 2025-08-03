from typing import List

class Track:
    def __init__(self, track_id: str, artist_id: str, artist_genres: List[str]):
        self.track_id = track_id
        self.artist_id = artist_id
        self.artist_genres = artist_genres
