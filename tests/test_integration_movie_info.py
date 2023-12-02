# Standard packages
from datetime import date

# Installed packages
import pandas as pd

# Internal modules
from src.movies_info import get_movies_info


def init_movies_info() -> str:
    """Initialise the movies' info.
    """
    # initialisation
    test_movie_title = "The Matrix"

    return get_movies_info(test_movie_title)


def test_null_get_movies_info():
    """Test if the function get_movies_info returns null.
    """
    # initialisation
    movies_info = init_movies_info()

    # check if the result is not null
    assert movies_info is not None, "The movies_info should not null."

    # check if the DataFrame is not empty
    assert not movies_info.empty, "The DataFrame should not be empty."


def test_content_get_movies_info():
    """Test the function get_movies_info.
    """
    # initialisation
    movies_info = init_movies_info()

    # check if columns exists in the DataFrame
    assert 'overview' in movies_info.columns, "The DataFrame should have an 'overview' column."
    assert 'name' in movies_info.columns, "The DataFrame should have an 'name' column."
    assert 'release_date' in movies_info.columns, "The DataFrame should have an 'release_date' column."
    assert 'genre' in movies_info.columns, "The DataFrame should have an 'genre' column."


def test_type_get_movies_info():
    """Test the type of the function get_movies_info.
    """
    # initialisation
    movies_info = init_movies_info()

    # check if the result is a string, since JSON is returned as a string in Python
    assert isinstance(
        movies_info, pd.DataFrame), "The function should return a pd.DataFrame."

    # ensure that every entry in the different columns have the right type
    assert all(isinstance(item, str)
               for item in movies_info['overview']), "Every item in the 'overview' column should be a string."

    assert all(isinstance(item, str)
               for item in movies_info['name']), "Every item in the 'name' column should be a string."

    assert all(isinstance(item, date)
               for item in movies_info['release_date']), "Every item in the 'release_date' column should be a string."

    assert all(isinstance(item, list)
               for item in movies_info['genre']), "Every item in the 'overview' column should be a string."
