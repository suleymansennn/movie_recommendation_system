import streamlit as st
import pandas as pd
import pickle
from utils_content_base import *

st.set_page_config(
    page_title="Movie Recommender",
    page_icon=":movie_camera:"
)

st.title("Movie Recommender System :movie_camera::popcorn:")
st.text("")

movies_m = pickle.load(open("models/movies_m.pkl", "rb"))

movie = st.selectbox("Type or select a movie from the dropdown",
                     (movies_m["title"].unique().tolist()))

if st.button("Show Recommendations"):
    with st.spinner("Please wait..."):
        cosine_sim = pickle.load(open("models/cosine_sim.pkl", "rb"))
        movie_names, movie_posters = content_based_recommender(movie, cosine_sim, movies_m)

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(movie_names[0])
            st.image(movie_posters[0])
        with col2:
            st.text(movie_names[1])
            st.image(movie_posters[1])
        with col3:
            st.text(movie_names[2])
            st.image(movie_posters[2])
        with col4:
            st.text(movie_names[3])
            st.image(movie_posters[3])
        with col5:
            st.text(movie_names[4])
            st.image(movie_posters[4])

