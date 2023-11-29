# Installed packages
import uvicorn

from fastapi import FastAPI

# Internal modules
from src.commun import get_movies
from src.commun import get_genre


app = FastAPI()

app = FastAPI()
# use the api read_root
@app.get("/get_movies_genre")
def display_movies_genre():
    movies_genre = get_genre()
    movies_genre.to_json(orient='records')
    return movies_genre

if __name__ == '__main__':
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
