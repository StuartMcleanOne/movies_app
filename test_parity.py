# Toggle between these two imports to test each module:
# import movie_storage  # JSON version
import movie_storage_sql as movie_storage  # SQL version

# Add a movie
movie_storage.add_movie("Inception", 2010, 8.8)

# List movies
movies = movie_storage.list_movies()
print("After add:", movies)

# Update a movie rating
movie_storage.update_movie("Inception", 9.0)
print("After update:", movie_storage.list_movies())

# Delete the movie
movie_storage.delete_movie("Inception")
print("After delete:", movie_storage.list_movies())
