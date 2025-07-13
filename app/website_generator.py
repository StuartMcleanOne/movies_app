def generate_website():
    from database import movie_storage_sql as movie_storage

    with open("_static/index_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    movies = movie_storage.list_movies()

    movie_grid = ""
    for title, details in movies.items():
        movie_grid += f"""
        <li>
            <div class="movie">
                <img class="movie-poster" src="{details['poster']}" alt="{title} poster">
                <div class="movie-title">{title}</div>
                <div class="movie-year">{details['year']}</div>
                <div class="movie-rating">Rating: {details['rating']}</div>
            </div>
        </li>
        """

    final_html = template.replace("__TEMPLATE_TITLE__", "My Movie Collection")
    final_html = final_html.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

    with open("_static/index.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html)

    print("Website was generated successfully.")
