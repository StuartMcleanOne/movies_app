import json


def get_movies(filename="data.json"):
    """Reads movies from Json file and returns them as dictionaries"""
    try:
        with open(filename, "r") as file:
            data = json.load(file)  # loads stored data from json.
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # returns an empty dictionary


def save_movies(movies, filename="data.json"):
    """Writes movies to JSON file for persistent storage"""
    with open(filename, "w") as file:
        json.dump(movies, file, indent=4)  # Improves readability


def add_movie(title, year, rating, filename="data.json"):
    """Adds movie to the database and saves it to the json file"""
    movies = get_movies(filename)  # Loads existing data.
    movies[title] = {"rating": rating, "year": year}  # Add new movie
    save_movies(movies, filename)  # save changes


def delete_movie(title, filename="data.json"):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies(filename)
    if title in movies:
        del movies[title]
        save_movies(movies, filename)


def update_movie(title, rating, filename="data.json"):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies(filename)
    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies, filename)
