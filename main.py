# Installed packages
import uvicorn

from fastapi import FastAPI

# Internal modules
from src.movies_reviews import transform_movies_review

# initialisation of the api
app = FastAPI()


@app.get("/get_movies_review")
def get_movies_review(movie_title: str):
    """Get the movies' reviews.
        Args:
            movie_title: The movie's title.
        Returns:
           movies_reviews: The movie reviews in a json.
    """
    # get the movies' reviews and put them in a json
    movies_reviews = transform_movies_review(
        movie_title).to_json(orient='records')

    return movies_reviews


if __name__ == '__main__':
    # use the api read_root
    uvicorn.run(app, host="0.0.0.0", port=8000)
