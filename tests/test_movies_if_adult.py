# Installed packages
import pandas as pd
import pytest



# Internal modules
import main
from main import display_movies_adult_limit
from src.get_movie_if_adult import get_movies_adult_limit



def init_movies_adult_limit() -> str:
    """Initialise the movies' adult limit.
    """
    # initialisation
    test_movie_title = "The Matrix"

    return get_movies_adult_limit(test_movie_title)


def test_null_get_movies_adult_limit():
    """Test if the function get_movies_adult_limit returns null.
    """
    # initialisation
    movies_adult_limit = init_movies_adult_limit()

    # test
    assert movies_adult_limit is not None, "The movies_adult_limit should not null."

    # check if the DataFrame is not empty
    assert not movies_adult_limit.empty, "The DataFrame should not be empty."


def test_content_get_movies_adult_limit():
    """Test the function get_movies_adult_limit.
    """
    # initialisation
    movies_adult_limit = init_movies_adult_limit()

    # check if 'adult' column exists in the DataFrame
    assert 'adult' in movies_adult_limit.columns, "The DataFrame should have an 'adult' column."


def test_type_get_movies_adult_limit():
    """Test the type of the function get_movies_adult_limit.
    """
    # initialisation
    movies_adult_limit = init_movies_adult_limit()

    # check if the result is a pandas dataframe
    assert isinstance(
        movies_adult_limit, pd.DataFrame), "The function should return a pd.DataFrame."

    # ensure that every entry in the 'adult' column is a boolean
    assert all(isinstance(item, str)
               for item in movies_adult_limit['adult']), "Every item in the 'adult' column should be a boolean(True/False)."


def test_get_movies_adult_limit_with_mocks(mocker):
    """Test the function get_movies_adult_limit.
        Args:
            mocker: The mocker object of pytest.
    """
    # initialisation
    data_mocked = pd.DataFrame([
        {'adult': False},
        {'adult': False}
    ])

    # simulate the function
    mock_get_movies_adult_limit = mocker.patch("display_movies_adult_limit",
                                             return_value=data_mocked)

    # use the mocked function
    response = display_movies_adult_limit("The Matrix")

    # assert that the get_movies_adult_limit was called with the right argument
    mock_get_movies_adult_limit.assert_called_once_with("The Matrix")

    # verify that the mocked data is the same as the result
    assert response == data_mocked.to_json(
        orient='records'), "The mocked data should be the same as the result."
