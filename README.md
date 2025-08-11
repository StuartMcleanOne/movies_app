**My Movie Database**



Welcome to My Movie Database, a Python command-line application that allows you to manage a personal movie collection. The application uses a local SQLite database to store movie data and can also generate a static website to display your collection.



**Features**

This application lets you:

View a list of all movies in your collection.

Add a new movie by title, which fetches data from the OMDb API.

Delete a movie from your collection.

Update a movie's rating.

See statistics about your movie collection (e.g., average rating, best/worst movies).

Get a random movie recommendation.

Search for a movie in your collection or online.

Generate a static HTML website to showcase your movies.



**Getting Started**
Follow these steps to set up and run the project.



**1. Prerequisites**
You will need Python 3.6 or later installed on your system.

**2. Setup**
First, clone this repository to your local machine:

git clone https://github.com/your-username/Movies_3.git
cd Movies_3



**3. Install Dependencies**
It's recommended to use a virtual environment. Create and activate one:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Next, install the required Python libraries:

pip install -r requirements.txt


**4. OMDb API Key**
The application uses the OMDb API to fetch movie data. You need to get a free API key from OMDb API and set it up in your project.

Create a file named .env in the movies_app directory and add your API key like this:

OMDB_API_KEY=YOUR_API_KEY_HERE

How to Run the Application
To start the application, navigate to the Movies_3 directory (the project's root) and run the following command:

python -m movies_app.app.movies

This will launch the command-line menu, where you can select from a variety of options to manage your movie collection.

Generating the Website
The website generation feature (choice 9 in the menu) will create a static HTML file.

The generated website is located at:
Movies_3/movies_app/_static/index.html

You can open this file directly in your web browser to view your movie collection.



Project Structure
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
