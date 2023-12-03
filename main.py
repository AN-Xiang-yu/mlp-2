# Installed packages
import uvicorn

from fastapi import FastAPI

# Internal modules
from src.get_movie_if_adult import get_movies_adult_limit

# initialisation of the API
app = FastAPI()


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


if __name__ == '__main__':
    # use the api read_root
    uvicorn.run(app, host="0.0.0.0", port=8000)
