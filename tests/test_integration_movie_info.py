# Standard packages
from datetime import date, datetime
import json
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
               for item in movies_info['genres']), "Every item in the 'overview' column should be a string."

def test_get_movies_info(mocker):
    # Sample JSON data
    json_data = '[{"overview": "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.", "name": "The Matrix", "release_date": "1999-03-30", "genres": ["Action", "Science Fiction"]}, ... ]'  # Add the rest of your JSON data here

    # Parse the JSON string into a list of dictionaries
    movies_list = json.loads(json_data)

    # Create a DataFrame from the list of dictionaries
    sample_df = pd.DataFrame(movies_list)

    # Mock the get_movies_info function to return the sample DataFrame
    mocker.patch('src.movies_info.get_movies_info', return_value=sample_df)

    # Call the function with a sample movie title
    result_df = get_movies_info("The Matrix")

    # Compare the result with the expected DataFrame
    pd.testing.assert_frame_equal(result_df, sample_df)