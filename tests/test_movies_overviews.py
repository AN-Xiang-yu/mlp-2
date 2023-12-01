# Installed packages
import pandas as pd

# Internal modules
from src.movies_overviews import get_movies_overviews


def init_movies_overviews() -> str:
    """Initialise the movies' overviews.
    """
    # initialisation
    test_movie_title = "The Matrix"

    return get_movies_overviews(test_movie_title)


def test_null_get_movies_overviews():
    """Test if the function get_movies_overviews returns null.
    """
    # initialisation
    movies_overviews = init_movies_overviews()

    # test
    assert movies_overviews is not None, "The movies_overviews should not null."

    # check if the DataFrame is not empty
    assert not movies_overviews.empty, "The DataFrame should not be empty."


def test_content_get_movies_overviews():
    """Test the function get_movies_overviews.
    """
    # initialisation
    movies_overviews = init_movies_overviews()

    # check if 'overview' column exists in the DataFrame
    assert 'overview' in movies_overviews.columns, "The DataFrame should have an 'overview' column."


def test_type_get_movies_overviews():
    """Test the type of the function get_movies_overviews.
    """
    # initialisation
    movies_overviews = init_movies_overviews()

    # check if the result is a string, since JSON is returned as a string in Python
    assert isinstance(
        movies_overviews, pd.DataFrame), "The function should return a pd.DataFrame."

    # ensure that every entry in the 'overview' column is a string
    assert all(isinstance(item, str)
               for item in movies_overviews['overview']), "Every item in the 'overview' column should be a string."
