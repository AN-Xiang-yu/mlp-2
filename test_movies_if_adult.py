# Installed packages
import pandas as pd
import pytest
import json


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
    assert all(isinstance(item, bool)
               for item in movies_adult_limit['adult']), "Every item in the 'adult' column should be a boolean(True/False)."


def test_get_movies_adult_limit_with_mocks(mocker):
    """Test the function get_movies_adult_limit.
        Args:
            mocker: The mocker object of pytest.
    """
    # initialisation
    json_str="[{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false},{\"adult\":false}]"

    #Parse the JSON string into a Python list of dictionaries
    data_list=json.loads(json_str)
    #Create a dataframe from list
    data_mocked=pd.DataFrame(data_list)

    # simulate the function
    mock_get_movies_adult_limit = mocker.patch("main.get_movies_adult_limit",
                                             return_value=data_mocked)

    # use the mocked function
    response = display_movies_adult_limit("The Matrix")

    # assert that the get_movies_adult_limit was called with the right argument
    mock_get_movies_adult_limit.assert_called_once_with("The Matrix")

    # verify that the mocked data is the same as the result
    response_df=pd.read_json(response,orient='records')
    pd.testing.assert_frame_equal(response_df, data_mocked)
