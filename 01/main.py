from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi primera aplicación con FastAPI"
app.version = "0.0.1"
app.description = "Esta es una descripción de mi API con FastAPI"

movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "ovreview": "Two imprisoned",
        "year": 1994,
        "rating": 9.3,
        "genre": "Drama"
    },
    {
        "id": 2,
        "title": "The Godfather",
        "ovreview": "An organized crime dynasty's",
        "year": 1972,
        "rating": 9.2,
        "genre": "Crime"
    }
]

@app.get("/", tags=["Home"])
def home():
    return {"message": "Hola Muewrewndo!!! 🌎"}

@app.get("/movies", tags=["Home"])
def home():
    return movies

@app.get("/movies/{movie_id}", tags=["Home"])
def home(movie_id: int):
    return movies[movie_id - 1]