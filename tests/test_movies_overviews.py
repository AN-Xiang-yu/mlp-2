# Installed packages
import pandas as pd

# Internal modules
from main import display_movies_overviews
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


def test_display_movies_overviews_with_mocks(mocker):
    """Test the function display_movies_overviews.
        Args:
            mocker: The mocker object of pytest.
    """
    # initialisation
    data_mocked = pd.DataFrame([
        {'overview': "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth. "},
        {'overview': "Plagued by strange memories, Neo's life takes an unexpected turn when he finds himself back inside the Matrix. "}
    ])

    # simulate the function
    mock_get_movies_overviews = mocker.patch("main.get_movies_overviews",
                                             return_value=data_mocked)

    # use the mocked function
    response = display_movies_overviews("The Matrix")

    # assert that the get_movies_overviews was called with the right argument
    mock_get_movies_overviews.assert_called_once_with("The Matrix")

    # verify that the mocked data is the same as the result
    assert response == data_mocked.to_json(
        orient='records'), "The mocked data should be the same as the result."
