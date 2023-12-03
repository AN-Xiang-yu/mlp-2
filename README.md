# Movie Information API

## Overview

This project is a FastAPI application that provides endpoints for fetching various information about movies. It includes functionalities like retrieving movie genres, overviews, adult content filtering, and detailed movie information.

## Installation

To set up this project, you need to have Python installed on your system. After cloning the repository, navigate to the project directory and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the FastAPI server:

```bash
uvicorn main:app --reload
```

The server will start on `http://127.0.0.1:8000`. You can access the following endpoints:

- `/get_movies_genres/{movie_title}`: Fetches the genre of a given movie.
- `/get_movies_overviews/{movie_title}`: Provides overviews of movies based on the title.
- `/get_movies_info/{movie_title}`: Retrieves detailed information about a movie.
- `/get_movies_adult_limit/{movie_title}`: Determines if a movie is restricted to adult audiences.

## Structure

- `main.py`: The entry point of the application, setting up the FastAPI server.
- `src/`: Directory containing the core functionalities:
  - `get_genres.py`: Script to get movie genres.
  - `movies_info.py`: Script to fetch detailed movie information.
  - `movies_overviews.py`: Script to get movie overviews.
  - `get_movie_if_adult.py`: Script to check for adult content.
- `test/`: Directory containing tests for the various functionalities.
- `requirements.txt`: File listing the necessary Python dependencies.

## Testing

To run the tests, navigate to the project directory and execute:

```bash
pytest
```

## Contributing
Katia ABAOUI:get_movies_genres, get_movies_info<br>
Wuqian MA: get_movies_adult_limit<br>
Xiangyu AN: get_movies_overviews, get_movies_info</b>
