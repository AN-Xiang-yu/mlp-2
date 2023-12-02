# Installed packages
import pandas as pd

# Internal modules
from src.commun import get_movies


def get_movies_overviews(movie_title) -> pd.DataFrame:
    """Transform the movie overviews in a dataFrame.
        Args:
            movie_title: The movies' title.
        Returns:
            movies_overviews: The movies' overviews
    """
    # initialisations
    movies = get_movies(movie_title)
    movies_overviews = []

    # get the movies' overviews
    for movie in movies:
        movies_overviews.append(movie["overview"])

    return pd.DataFrame(movies_overviews, columns=["overview"])
