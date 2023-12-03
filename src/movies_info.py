# Installed packages
import pandas as pd

# Internal modules
from src.movies_overviews import get_movies_overviews
from src.get_genres import get_genres


def get_movies_info(movie_title) -> pd.DataFrame:
    """Transform the movie in a dataFrame.
        Args:
            movie_title: The movies' title.
        Returns:
            movies_overviews: The movies' overviews
    """
    # initialisations
    movies_overviews = get_movies_overviews(movie_title)
    movies_genres = get_genres(movie_title)

    # put the movies' overviews and genres in a dataFrame
    movies_info = pd.concat([movies_overviews, movies_genres], axis=1)

    return movies_info
