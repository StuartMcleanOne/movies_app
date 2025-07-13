import requests

API_KEY = "5156d3f1"

def fetch_movie_data(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            rating = data.get("imdbRating")
            return {
                "title": data.get("Title"),
                "year": int(data.get("Year")),
                "rating": float(rating) if rating and rating != "N/A" else None,
                "poster": data.get("Poster")
            }
        else:
            print(F"Movie '{title}' not found in OMDb.")
            return None
    except requests.exceptions.RequestException:
        print("Network error. Could not connect to OMDb.")
        return None

