import random
import statistics
import movie_storage  # imports custom storage module
from movie_storage_sql import (
    add_movie as sql_add_movie,
    list_movies as sql_list_movies,
    update_movie as sql_update_movie,
    delete_movie as sql_delete_movie
)

def list_movies():
    """Lists all the movies and their information."""
    movies = movie_storage.get_movies()

    if movies:
        print(f"\n{len(movies)} movies in total\n")
        for title, details in movies.items():
            print(f"{title} ({details['year']}): {details['rating']}")
    else:
        print("No movies found.")


def add_movie():
    """Adds a movie to the movie database"""
    movies = movie_storage.get_movies()

    while True: # While loop here handles blank inputs
        title = input("Enter new movie name: ").strip()
        if not title:
            print("Movie title cannot be empty.")
        elif title in movies:
            print(f"Movie '{title}' already exists!")
            return
        else:
            break

    while True:
        try:
            year = int(input("Enter year of release: "))
            break
        except ValueError:
            print("Invalid input. Year must be an integer.")

    while True:
        try:
            rating = float(input("Enter movie rating (0–10): "))
            if 0 <= rating <= 10:
                break
            else:
                print("Rating must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Rating must be a number.")

    movie_storage.add_movie(title, year, rating)
    print(f"Movie '{title}' successfully added.")


def delete_movie():
    """Deletes movie from database"""
    movies = movie_storage.get_movies()

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
    movies = movie_storage.get_movies()

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
    movies = movie_storage.get_movies()

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
    movies = movie_storage.get_movies()

    if movies:
        title = random.choice(list(movies.keys()))
        details = movies[title]
        print(f"Random Movie: {title} ({details['year']}): {details['rating']}")
    else:
        print("No movies available.")


def search_movie():
    """Search for movies using keyword"""
    movies = movie_storage.get_movies()

    while True: # While loop handles blank inputs
        query = input("Enter part of a movie name: ").strip().lower()
        if not query:
            print("Search query cannot be empty.")
        else:
            break

    results = [title for title in movies if query in title.lower()]
    if results:
        for title in results:
            print(f"{title} ({movies[title]['year']}): {movies[title]['rating']}")
    else:
        print("No matching movies found.")


def sort_movies():
    """Displays all movies sorted from high to low"""
    movies = movie_storage.get_movies()

    if movies:
        sorted_list = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
        for title, details in sorted_list:
            print(f"{title} ({details['year']}): {details['rating']}")
    else:
        print("No movies found.")


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
        else:
            # Error handling for incorrect inputs.
            print("Invalid choice. Please enter number between 0 and 8.") #Validates inputs


def main():
    """Runs the program"""
    menu()


if __name__ == "__main__":

    sql_add_movie("Inception", 2010, 8.8)

    movies = sql_list_movies()
    print(movies)

    sql_update_movie("Inception", 9.0)
    print(sql_list_movies())

    sql_delete_movie("Inception")
    print(sql_list_movies())

    main()
