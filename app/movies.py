import random
import statistics
import requests

from database import movie_storage_sql as movie_storage# renamed the sql storage to match that of the json storage module to exercise parity
from app.utils import fetch_movie_data
from app.website_generator import generate_website


def list_movies():
    """Lists all the movies and their information."""
    movies = movie_storage.list_movies()

    if movies:
        print(f"\n{len(movies)} movies in total\n")
        for title, details in movies.items():
            print(f"{title} ({details['year']}): {details['rating']}")
    else:
        print("No movies found.")


def add_movie():
    title_input = input("Enter movie title: ").strip()
    if not title_input:
        print("movie title cannot be empty.")
        return

    movie_data = fetch_movie_data(title_input)
    if not movie_data:
        return # Error handled inside fetch function

    # Check if movie already exists
    existing = movie_storage.list_movies()
    if movie_data["title"] in existing:
        print(f"Movie '{movie_data['title']}' already exists.")
        return

    # Insert into database
    movie_storage.add_movie(
        movie_data["title"],
        movie_data["year"],
        movie_data["rating"],
        movie_data["poster"],
    )
    print(f"Movie '{movie_data['title']}' added successfully.")


def delete_movie():
    """Deletes movie from database"""
    movies = movie_storage.list_movies()

    while True: # While loop handles blank entries
        title = input("Enter movie name to delete: ").strip()
        if not title:
            print("Movie title cannot be empty.")
        elif title not in movies:
            print(f"Movie '{title}' not found.")
            return
        else:
            break

    movie_storage.delete_movie(title)
    print(f"Movie '{title}' successfully deleted.")


def update_movie():
    """Updates movie rating in database"""
    movies = movie_storage.list_movies()

    while True: # While loop here validates inputs
        title = input("Enter movie name to update: ").strip()
        if not title:
            print("Movie title cannot be empty.")
        elif title not in movies:
            print(f"Movie '{title}' not found.")
            return
        else:
            break

    while True:
        try:
            new_rating = float(input("Enter new rating (0–10): "))
            if 0 <= new_rating <= 10:
                break
            else:
                print("Rating must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Rating must be a number.")

    movie_storage.update_movie(title, new_rating)
    print(f"Movie '{title}' successfully updated to rating {new_rating}.")


def stats():
    """Displays movies stats using persistent storage"""
    movies = movie_storage.list_movies()

    if movies:
        ratings = [details["rating"] for details in movies.values()]
        avg_rating = round(sum(ratings) / len(ratings), 2)
        median_rating = round(statistics.median(ratings), 2)

        max_rating = max(ratings)
        min_rating = min(ratings)

        best_movies = [title for title, details in movies.items() if details["rating"] == max_rating]
        worst_movies = [title for title, details in movies.items() if details["rating"] == min_rating]

        print(f"Average rating: {avg_rating}")
        print(f"Median rating: {median_rating}")
        print(f"Best movies: {', '.join(best_movies)} ({max_rating})")
        print(f"Worst movies: {', '.join(worst_movies)} ({min_rating})")
    else:
        print("No movies in database.")


def random_movie():
    """Selects a random movie using persistent storage"""
    movies = movie_storage.list_movies()

    if movies:
        title = random.choice(list(movies.keys()))
        details = movies[title]
        print(f"Random Movie: {title} ({details['year']}): {details['rating']}")
    else:
        print("No movies available.")


def search_movie():
    """Search for movies using keyword"""
    movies = movie_storage.list_movies()

    while True: # While loop handles blank inputs
        query = input("Enter part of a movie name: ").strip().lower()
        if not query:
            print("Search query cannot be empty.")
        else:
            break

    # Local database search
    results = [title for title in movies if query in title.lower()]
    if results:
        print("Found in your collection:")
        for title in results:
            print(f"{title} ({movies[title]['year']}): {movies[title]['rating']}")
        return

    # OMBd fallback . Added this for smoother UX logic.
    search_term = query.title()
    print("No match in your collection. Searching OMDb...")
    movie_data = fetch_movie_data(search_term)

    if movie_data:
        print("\nFound via OMDb:")
        print(f"{movie_data['title']} ({movie_data['year']})")
        print(f"IMDb Rating: {movie_data['rating']}")
        print(f"Poster URL: {movie_data['poster']}")

        confirm = input("\nWould you like to add this movie to your collection? (Y/N): ").strip().lower()
        if confirm == 'y':
            movie_storage.add_movie(
                movie_data["title"],
                movie_data["year"],
                movie_data["rating"],
                movie_data["poster"]
            )
            print(f"\nMovie '{movie_data['title']}' added successfully.")
        else:
            print("\nNo changes made.")
    else:
        print(f"\nMovie '{search_term}' not found via OMDb")

def sort_movies():
    """Displays all movies sorted from high to low"""
    movies = movie_storage.list_movies()

    if movies:
        sorted_list = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
        for title, details in sorted_list:
            print(f"{title} ({details['year']}): {details['rating']}")
    else:
        print("No movies found.")

def seed_database():
    """Seed the database with original ten movies if its empty"""
    if not movie_storage.list_movies():
        print("Seeding database with original movies...\n")
        starter_titles = [
            "The Shawshank Redemption", "Pulp Fiction", "The Room",
            "The Godfather", "The Godfather: Part II", "The Dark Knight",
            "12 Angry Men", "Everything Everywhere All At Once",
            "Forrest Gump", "Star Wars: Episode V"
        ]
        for title in starter_titles:
            data = fetch_movie_data(title)
            if data:
                movie_storage.add_movie(
                    data["title"], data["year"], data["rating"], data["poster"]
                )
            else:
                print(f" Could not fetch '{title}' from OMDb.")

def menu():
    """Menu display and user input"""

    while True:
        print("\n********** My Movie Database **********")
        print("0. Exit")  # Moved exit to "0"
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")
        print("9. Generate website")

        choice = input("Enter choice (0–8): ").strip()  # User input for menu choice

        print()  # Adds a blank space before displaying output
        # Corresponding functions based on user choice
        if choice == "0":
            print("bye!")
            break  # stops loop
        elif choice == "1":
            list_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            stats()
        elif choice == "6":
            random_movie()
        elif choice == "7":
            search_movie()
        elif choice == "8":
            sort_movies()
        elif choice =="9":
            generate_website()
        else:
            # Error handling for incorrect inputs.
            print("Invalid choice. Please enter number between 0 and 8.") #Validates inputs


def main():
    """Runs the program"""
    seed_database()
    menu()

if __name__ == "__main__":

    main()
