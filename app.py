import streamlit as st
import pickle
import difflib
import pandas as pd
from PIL import Image
import requests
from io import BytesIO
from utils import recommend_movies

try:
    similarities = pickle.load(open('similarities.pkl', 'rb'))
except Exception as e:
    print('Ensure that you have run the generate_similarities.py file')
    print(e)

try:
    movies = pd.read_csv('processed_data_frame.csv')
except Exception as e:
    print('Ensure you have run the prepare_data.py file')
    print(e)

all_movies = movies['title'].values

# Main Streamlit app
def main():
    st.title("Movie Recommendation App")

    # Search bar
    movie_name = st.text_input("Search for a movie:")

    # Dropdown for number of movies to recommend
    n_movies_to_recommend = st.selectbox("Select number of movies to recommend", [1, 2, 3, 4, 5,6,7,8,9,10], index=2)

    if st.button("Recommend"):
        # Call recommend_movies function to get recommendations
        recommended_movies = recommend_movies(movies, all_movies, movie_name, n_movies_to_recommend, similarities)

        # Display recommendations in a grid layout with inline CSS
        st.markdown('<div style="display: grid; grid-template-columns:repeat(5,1fr);">', unsafe_allow_html=True)

        for index, row in recommended_movies.iterrows():
            st.markdown(
                f"""
                <div style="display: inline-block; margin: 10px; text-align: center; border: 1px solid #ccc; padding: 10px; border-radius: 10px;">
                    <img src="{row['image']}" alt="Movie Poster" style="width: 300px; height: 450px; border-radius: 5px;">
                    <p style="margin-top: 10px; font-weight: bold; font-size: 16px;">{row['title']}</p>
                    <p><strong>Cast:</strong> {row['cast_new']}</p>
                    <p><strong>Crew:</strong> {row['crew_new']}</p>
                    <p><strong>Runtime:</strong> {row['runtime']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
