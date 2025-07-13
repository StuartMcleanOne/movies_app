# movies_app
# 🎬 My Movie Collection App

A Python CLI application for managing a personal movie database — complete with poster links, ratings, and a dynamic website generator.

---

## 📦 Features

- Add, delete, update, and list movies
- Store movie details in a SQLite database
- Automatically generate a website with your movie collection
- View movies sorted by rating or selected at random
- Search for a movie by title
- Clean file structure with storage separated into packages

---

## 🚀 Installation

Clone the repo to your local machine:

```bash
git clone https://github.com/StuartMcleanOne/movies_app.git
cd movies_app

````
Install dependencies:
```bash
pip intall -r requirements.txt
```
---
## ▶️ Usage
Follow on-screen menu to interact with movie collection. To generate website choose option 9.
```bash
python -m app.movies
```
---
## 💾 Data & Structure

 - Database is stored in /database/movies.db

 - Static assets like HTML/CSS are in /_static

 - Website generated at /_static/index.html

---

## 👨‍💻Tech Stack

 - Python 3

 - SQLAlchemy

 - SQLite

 - Requests

---
## 📁 File Tree Overview

movies_app/
│
├── app/
│   ├── movies.py
│   ├── website_generator.py
│   └── utils.py
│
├── database/
│   ├── movies.db
│   ├── movie_storage_sql.py
│   └── transfer_json_to_sql.py
│
├── _static/
│   ├── index_template.html
│   ├── index.html
│   └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md

---
 ## Author

A Masterschool case study by Stuart McLean
 GitHub Profile → https://github.com/StuartMcleanOne