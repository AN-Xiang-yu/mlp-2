# Installed packages
import pandas as pd

# Internal modules
from src.commun import get_movies


def get_movies_adult_limit(movie_title) -> pd.DataFrame:
    """Transform the movie's adult limitation info in a dataFrame.
        Args:
            movie_title: The movies' title.
        Returns:
            movies_if_adult: The movies are limited for adult or not
    """
    # initialisations
    movies = get_movies(movie_title)
    movies_if_adult = []

    # get the movies' overviews
    for movie in movies:
        movies_if_adult.append(movie["adult"])

    return pd.DataFrame(movies_if_adult, columns=["adult"])


