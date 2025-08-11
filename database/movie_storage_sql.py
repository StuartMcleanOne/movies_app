import os
from sqlalchemy import create_engine, text

# Set the path to the database file dynamically
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "database", "movies.db")
DB_URL = f"sqlite:///{db_path}"

engine = create_engine(DB_URL, echo=False)

# Create the movies table if it does not exist
with engine.connect() as connection:
    connection.execute(text("""
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE NOT NULL,
        year INTEGER NOT NULL,
        rating REAL NOT NULL,
        poster TEXT
    )
    """))
    connection.commit()

def list_movies():
    """Retrieve all movies from the database."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT title, year, rating, poster FROM movies"))
        movies = result.fetchall()

    return {
        row[0]: {
            "year": row[1],
            "rating": row[2],
            "poster": row[3]
        } for row in movies
    }

def add_movie(title, year, rating, poster):
    """Add a new movie to the database, including poster URL."""
    with engine.connect() as connection:
        try:
            connection.execute(
                text("""
                INSERT INTO movies (title, year, rating, poster)
                VALUES (:title, :year, :rating, :poster)
                """),
                {"title": title, "year": year, "rating": rating, "poster": poster}
            )
            connection.commit()
            print(f"Movie '{title}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")

def delete_movie(title):
    """Delete a movie from the database."""
    with engine.connect() as connection:
        try:
            connection.execute(
                text("DELETE FROM movies WHERE title = :title"),
                {"title": title}
            )
            connection.commit()
            print(f"Movie '{title}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting movie: {e}")

def update_movie(title, rating):
    """Update a movie's rating in the database."""
    with engine.connect() as connection:
        try:
            connection.execute(
                text("UPDATE movies SET rating = :rating WHERE title = :title"),
                {"title": title, "rating": rating}
            )
            connection.commit()
            print(f"Movie '{title}' updated successfully.")
        except Exception as e:
            print(f"Error updating movie: {e}")