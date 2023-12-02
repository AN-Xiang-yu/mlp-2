
# Installed packages
import tmdbsimple as tmdb
import pandas as pd

# Internal modules
from src.commun import get_movies

################## Constants of the Movie handler ##################
TMDB_KEY = '6cd475d6493bd4fb6ead9f2919db145a'
################## Global Settings ##################
tmdb.API_KEY = TMDB_KEY

def get_genres(movie_title : str) -> pd.DataFrame:
    """Get the genre of the movie.
        Args:
            movie: The movie from the movie title.
        Returns:
            genre: The genre of the movie.
    """
    # initialisations
    movies = get_movies(movie_title)
    genres_movies = [movie['genre_ids'] for movie in movies]
    genres_names = []

    # get the genre of the movie
    for genres_movie in genres_movies:
        my_current_movie_genres = []
        genres_movies = tmdb.Genres()
        response = genres_movies.movie_list()

        for g in response['genres']:
            for genre in genres_movie:
                if g['id'] == genre:
                    my_current_movie_genres.append(g['name'])
        genres_names.append(my_current_movie_genres)

    # organize information in a DataFrame
    df = pd.DataFrame({
        'name': [movie['original_title'] for movie in movies],
        'release_date': [movie['release_date'] for movie in movies],
        'genres': genres_names
    })

    return df

