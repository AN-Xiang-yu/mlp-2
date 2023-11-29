# Installed packages
import requests
import tmdbsimple as tmdb
import pandas as pd
################## Constants of the Movie handler ##################
TMDB_KEY = '6cd475d6493bd4fb6ead9f2919db145a'
URL_MOVIE = "https://api.themoviedb.org/3/search/movie"
################## Global Settings ##################
tmdb.API_KEY = TMDB_KEY
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

def get_genre():
    """Get the genre of the movie.
        Args:
            movie: The movie from the movie title.
        Returns:
            genre: The genre of the movie.
    """
    # initialisations
    movie_title = 'The Matrix'
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
    # Organize information in a DataFrame
    df = pd.DataFrame({
        'name': [movie['original_title'] for movie in movies],
        'release_date': [movie['release_date'] for movie in movies],
        'genre': genres_names
    })

    return df

