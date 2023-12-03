# Installed packages
import uvicorn
from fastapi import FastAPI

# Internal modules
from src.get_genres import get_genres
from src.get_movie_if_adult import get_movies_adult_limit
from src.movies_info import get_movies_info
from src.movies_overviews import get_movies_overviews


# initialisation of the api
app = FastAPI()


@app.get("/get_movies_genres/{movie_title}")
def display_movies_genre(movie_title: str):
    """Get the genre of the movie.
        Args:
            movie_title: The movie from the movie title.
        Returns:
            Json Movies, realeses dates and genres.
    """
    # get the movies' genres and put them in a json
    movies_genre = get_genres(movie_title)

    return movies_genre.to_json(orient='records')


@app.get("/get_movies_overviews/{movie_title}")
def display_movies_overviews(movie_title: str):
    """Display the movies' overviews.
        Args:
            movie_title: The movie's title.
        Returns:
           movies_overviews: The movie overviews in a json.
    """
    # get the movies' overviews and put them in a json
    movies_overviews = get_movies_overviews(
        movie_title)

    return movies_overviews.to_json(orient='records')


@app.get("/get_movies_adult_limit/{movie_title}")
def display_movies_adult_limit(movie_title: str):
    """Display the movies' adult limit or not.
        Args:
            movie_title: The movie's title.
        Returns:
           movies_overviews: The movie is limited watch in adult or not in a json.
    """
    # get the movies' adult limit and put them in a json
    movies_adult_limit = get_movies_adult_limit(
        movie_title)

    return movies_adult_limit.to_json(orient='records')


@app.get("/get_movies_info/{movie_title}")
def display_movies_info(movie_title: str):
    """Display the movies' info.
        Args:
            movie_title: The movie's title.
        Returns:
           movies_info: The movie info in a json.
    """
    # get the movies' overviews and put them in a json
    movies_info = get_movies_info(
        movie_title)

    return movies_info.to_json(orient='records')


if __name__ == '__main__':
    # use the api read_root
    uvicorn.run(app, host="0.0.0.0", port=8000)
