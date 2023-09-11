import pickle
import streamlit as st
import pandas as pd
import requests
from streamlit import runtime
runtime.exists()


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2685f6cc01761272896057e0082abc02".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movies = pd.DataFrame(movies_dict)
    index = movies[movies['title'] == movie].index[0]
    movie_index = similarity[index]
    distances = sorted(list(enumerate(movie_index)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:5]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')



movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies_dict['title'].values()
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
    with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

    with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
    with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
    with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])






