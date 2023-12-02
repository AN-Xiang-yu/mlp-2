# Standard packages
from datetime import date, datetime
import pandas as pd

# Installed packages
import pandas as pd

# Internal modules
from src.get_genres import get_genres



def init_movies_genre() -> pd.DataFrame:
    """Initialise the movies' genres.
    """
    test_movie_title = "The Matrix"
    return get_genres(test_movie_title)


def test_genre_not_empty():
    """Test if the function get_genres returns null.
    """
    genres = init_movies_genre()
    assert genres is not None, "We don't have this movie in the database"
    assert not genres.empty, "The genres DataFrame is empty"


def test_genre_release_date_is_date():
    """Test if the release date is a date.
    """
    genres = init_movies_genre()
    for _, row in genres.iterrows():
        release_date_str = row['release_date']
        release_date = datetime.strptime(release_date_str, "%Y-%m-%d").date()
        assert isinstance(release_date, date), "The release date is not valid"


def test_genre_name_is_string():
    """Test if the name is a string.
    """
    genres = init_movies_genre()
    for _, row in genres.iterrows():
        genres_list = row['genres']
        assert isinstance(genres_list, list), "The genres is not a list"
        for g in genres_list:
            assert isinstance(g, str), "The genre is not a string"


def test_genre_types():
    """Test if the types of each column are correct.
    """
    genres = init_movies_genre()
    for _, row in genres.iterrows():
        assert 'name' in row, "The name is not in the DataFrame"
        assert 'release_date' in row, "The release date is not in the DataFrame"
        assert 'genres' in row, "The genres is not in the DataFrame"


def test_get_genres(mocker):
        
    # Sample data for mocking
    sample_movies = [
        {'genre_ids': [28, 12], 'original_title': 'Iron Man', 'release_date': '2021-01-01'},
        {'genre_ids': [14], 'original_title': 'Iron Man', 'release_date': '2021-01-02'}
    ]

    sample_genres = {'genres': [
        {'id': 28, 'name': 'Action'},
        {'id': 12, 'name': 'Adventure'},
        {'id': 14, 'name': 'Fantasy'}
    ]}

    # Mock get_movies function
    mocker.patch('src.commun.get_movies', return_value=sample_movies)

    # Mock tmdb.Genres().movie_list method
    mocker.patch('tmdbsimple.Genres.movie_list', return_value=sample_genres)

    # Call the function with a sample movie title
    result = get_genres("Iron Man")

    # Assertions
    assert isinstance(result, pd.DataFrame), "Result should be a pandas DataFrame"
    assert set(result.columns) == {'name', 'release_date', 'genres'}, "DataFrame should have name, release_date, and genres columns"
