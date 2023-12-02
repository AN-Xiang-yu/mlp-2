# Installed packages
import uvicorn

from fastapi import FastAPI, Query

# Internal modules
from src.get_genres import get_genres


app = FastAPI()
# use the api read_root


@app.get("/get_movies_genre/{movie_title}")
def display_movies_genre(movie_title: str):
    """Get the genre of the movie.
    Args:
        movie: The movie from the movie title.
    Returns:
        Json Movies, realeses dates and genres .
    """
    # get the movie
    movies_genre = get_genres(movie_title)

    return movies_genre.to_json(orient='records')


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
