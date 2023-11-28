# Installed packages
import pandas as pd

# Internal modules
from src.commun import get_movies


def transform_movies_review(movie_title) -> pd.DataFrame:
    """Transform the movie in a dataFrame.
        Args:
            movie_title: The movies' title.
        Returns:
            movies_reviews: The movies' reviews
    """
    # initialisations
    movies = get_movies(movie_title)
    movies_reviews = []

    # get the movies' reviews
    for movie in movies:
        movies_reviews.append(movie["overview"])

    return pd.DataFrame(movies_reviews)
