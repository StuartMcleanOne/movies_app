import json
from movie_storage_sql import add_movie

# Load the JSON file
with open("data.json", "r") as file:
    movies = json.load(file)

# Insert each movie into the SQL database
for title, info in movies.items():
    add_movie(title, info["year"], info["rating"])

print("Transfer complete. Data Migrated")