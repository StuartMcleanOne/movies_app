# 🎬 My Movie Database

Welcome to **My Movie Database**, a Python command-line application that helps you manage your personal movie collection. It uses a local SQLite database to store movie data and can generate a static website to showcase your collection.

---

## ✨ Features

This application lets you:

- 📃 View a list of all movies in your collection
- ➕ Add a new movie by title (fetches data from the OMDb API)
- ❌ Delete a movie from your collection
- ⭐ Update a movie's rating
- 📊 View statistics (average rating, best/worst movies)
- 🎲 Get a random movie recommendation
- 🔍 Search for a movie in your collection or online
- 🌐 Generate a static HTML website to display your movies

---

## 🚀 Getting Started

Follow these steps to set up and run the project.

### 1. Prerequisites

- Python **3.6 or later** installed on your system

### 2. Setup

Clone the repository and navigate into the project folder:

````bash
git clone https://github.com/your-username/Movies_3.git
cd Movies_3 
````
### 3. Install Dependencies
It’s recommended to use a virtual environment:

````bash
python -m venv venv
Activate the environment:

Windows:

bash
.\venv\Scripts\activate
macOS/Linux:

bash
source venv/bin/activate

````
#### 4. OMDb API Key
The app uses the OMDb API to fetch movie data. Get a free API key from OMDb API, then create a .env file in the movies_app directory:

OMDB_API_KEY=YOUR_API_KEY_HERE
▶️ How to Run the Application
From the project root (Movies_3), run:
````
bash
python -m movies_app.app.movies
This launches the command-line menu where you can manage your movie collection.
````
#### 🌐 Generating the Website
Choose option 9 in the menu to generate a static HTML website.

The site will be created at: Movies_3/movies_app/_static/index.html

Open this file in your browser to view your movie collection.

````
Movies_3/
├── movies_app/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── movies.py
│   │   ├── utils.py
│   │   └── website_generator.py
│   ├── database/
│   │   ├── movie_storage_sql.py
│   │   └── movies.db
│   ├── _static/
│   │   ├── index.html
│   │   ├── index_template.html
│   │   └── style.css
│   └── .env
└── requirements.txt
````
