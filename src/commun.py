# Installed packages
import requests
import pandas as pd
################## Constants of the Movie handler ##################
TMDB_KEY = '6cd475d6493bd4fb6ead9f2919db145a'
URL_MOVIE = "https://api.themoviedb.org/3/search/movie"
################## Functions ##################
def get_movies(movie_title: str, year_released: str = None) -> list[dict]:
    """Get the movie from the movie title.
        Args:
            movie_title: The title of the movie.
            year_released: The year the movie was released.

        Returns:
            movie: The movie from the movie title.
    """
    # initialisation
    params = {"api_key": TMDB_KEY, "query": movie_title}

    # make the request to the movie API
    response = requests.get(URL_MOVIE, params=params)

    # check if the request was successful
    if response.status_code != 200 or not response.json().get('results'):
        return None

    # get the movie
    if year_released:
        for movie in response.json()['results']:
            if movie['release_date'].split('-')[0] == year_released:
                return movie

    movie = response.json()['results']
    return movie
