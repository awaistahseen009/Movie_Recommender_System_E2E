import difflib
import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
api_key = os.getenv("API_KEY")
def recommend_movies(movies, all_movies, movie_name, n_movies, similarity):
    movie_name = difflib.get_close_matches(movie_name, all_movies)[0]
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []

    for i in distances[:n_movies]:
        recommended_movie = movies.iloc[i[0]]
        recommended_movie['image']=fetch_poster(recommended_movie['movie_id'])
        recommended_movies.append(recommended_movie)

    recommended_movies_df = pd.DataFrame(recommended_movies)
    return recommended_movies_df

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path