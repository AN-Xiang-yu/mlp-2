# from main import display_movies_genre
from src.get_genres import get_genres
from datetime import datetime, date
import pandas as pd
from src.get_genres import get_genres
from datetime import datetime

def init_movies_genre() -> pd.DataFrame:
    """Initialise the movies' genres."""
    test_movie_title = "The Matrix"
    return get_genres(test_movie_title)

def test_genre_not_empty():
    genres = init_movies_genre()
    assert genres is not None, "We don't have this movie in the database"
    assert not genres.empty, "The genres DataFrame is empty"

def test_genre_release_date_is_date():
    genres = init_movies_genre()
    for _, row in genres.iterrows():
        release_date_str = row['release_date']
        release_date = datetime.strptime(release_date_str, "%Y-%m-%d").date()
        assert isinstance(release_date, date), "The release date is not valid"

def test_genre_name_is_string():
    genres = init_movies_genre()
    for _, row in genres.iterrows():
        genres_list = row['genres']
        assert isinstance(genres_list, list), "The genres is not a list"
        for g in genres_list:
            assert isinstance(g, str), "The genre is not a string"

def test_genre_types():
    genres = init_movies_genre()
    for _, row in genres.iterrows():
        assert 'name' in row, "The name is not in the DataFrame"
        assert 'release_date' in row, "The release date is not in the DataFrame"
        assert 'genres' in row, "The genres is not in the DataFrame"