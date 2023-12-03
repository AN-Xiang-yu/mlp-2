# Standard packages
from datetime import date, datetime

# Installed packages
import pandas as pd

# Internal modules
from main import display_movies_info
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
    assert 'genres' in movies_info.columns, "The DataFrame should have an 'genres' column."


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

    assert all(isinstance(datetime.strptime(item, "%Y-%m-%d").date(), date)
               for item in movies_info['release_date']), "Every item in the 'release_date' column should be convertible to a date."

    assert all(isinstance(item, list)
               for item in movies_info['genres']), "Every item in the 'genres' column should be a string."


def test_display_movies_info_with_mock(mocker):
    """Test the function display_movies_info.
        Args:
            mocker: The mocker object of pytest.
    """
    # sample JSON data
    data_mocked = pd.DataFrame([
        {"name": "The Matrix", "release_date": "2021-01-01",
            "genres": ["Action", "Adventure"], 'overview': "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth. "},
        {"name": "The Matrix", "release_date": "2021-01-02",
            "genres": ["Fantasy"], 'overview': "Plagued by strange memories, Neo's life takes an unexpected turn when he finds himself back inside the Matrix. "}
    ])

    # mock the get_movies_info function to return the sample DataFrame
    mock_get_movies_info = mocker.patch(
        'main.get_movies_info', return_value=data_mocked)

    # call the function with a sample movie title
    result = display_movies_info("The Matrix")

    # assert that the get_movies_overviews was called with the right argument
    mock_get_movies_info.assert_called_once_with("The Matrix")

    # verify that the mocked data is the same as the result
    assert result == data_mocked.to_json(
        orient='records'), "The mocked data should be the same as the result."
