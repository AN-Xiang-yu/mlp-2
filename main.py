# Installed packages
import uvicorn

from fastapi import FastAPI

# Internal modules
from modules.commun import get_movies


app = FastAPI()


if __name__ == '__main__':
    app = FastAPI()
    # use the api read_root
    uvicorn.run(app, host="0.0.0.0", port=8000)
