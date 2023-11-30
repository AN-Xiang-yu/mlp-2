# Standard imports
import json

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


def test_null_get_movies_review():
    """Test if the function get_movies_review returns null.
    """
    # initialisation
    movies_overviews = init_movies_overviews()

    # test
    assert movies_overviews is not None, "The movies_overviews should not null."


def test_type_get_movies_review():
    """Test the type of the function get_movies_review.
    """
    # initialisation
    movies_overviews = init_movies_overviews()

    # check if the result is a string, since JSON is returned as a string in Python
    assert isinstance(
        movies_overviews, pd.DataFrame), "The function should return a pd.DataFrame."

    assert isinstance(
        movies_overviews.overview, str), "The function should return a pd.DataFrame."


def test_content_get_movies_review():
    """Test the function get_movies_review.
    """
    # initialisation
    movies_overviews = init_movies_overviews()

    # test
    assert movies_overviews == ""
