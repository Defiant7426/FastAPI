from fastapi import FastAPI

app = FastAPI()

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
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "ovreview": "When the menace",
        "year": 1994,
        "rating": 9.0,
        "genre": "Action"
    },
]

@app.get("/", tags=["Home"])
def home():
    return {"message": "Hola Mundo!!! 🌎"}

@app.get("/movies/", tags=["Home"])
def movie(year: int):
    return [movie for movie in movies if movie["year"] == year]

