from typing import List

GENRE_MAP = {
    'pop': 'Pop',
    'k-pop': 'Pop',
    'dance pop': 'Pop',
    'pop rap': 'Pop',
    'rock': 'Rock',
    'classic rock': 'Rock',
    'alternative rock': 'Rock',
    'hard rock': 'Rock',
    'rap': 'Hip Hop',
    'hip hop': 'Hip Hop',
    'trap': 'Hip Hop',
    'r&b': 'R&B',
    'indie': 'Indie',
    'indie pop': 'Indie',
    'indie rock': 'Indie',
    'metal': 'Metal',
    'heavy metal': 'Metal',
    'latin': 'Latino',
    'reggaeton': 'Latino',
    'sertanejo': 'Sertanejo',
    'mpb': 'MPB',
    'funk carioca': 'Funk',
    'funk': 'Funk',
    'jazz': 'Jazz',
    'blues': 'Blues',
    'electronic': 'Eletrônica',
    'edm': 'Eletrônica',
}

def normalize_genre(genres: List[str]) -> str:
    if not genres:
        return "Outros"
    genre_lower = genres[0].lower()
    for key, value in GENRE_MAP.items():
        if key in genre_lower:
            return value
    return "Outros"
