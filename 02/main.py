from fastapi import FastAPI, Body

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

@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get("/movies/", tags=["Movies"])
def get_movie_from_year(year: int):
    return [movie for movie in movies if movie["year"] == year]


@app.post("/movies", tags=["Movies"])
def create_movie(
    title: str = Body(...), # cuando se pone ... se indica que es requerido
    overview: str = Body(...),
    year: int = Body(...),
    rating: float = Body(...),
    genre: str = Body(...)
):
    movie = {
        "id": len(movies) + 1,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "genre": genre
    }
    movies.append(movie)
    return movie
