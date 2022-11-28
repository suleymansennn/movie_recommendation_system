import streamlit as st
import pandas as pd
import requests
import pickle
from utils_content_base import *

movies_m = pickle.load(open("models/movies_m.pkl", "rb"))

st.title("Content Base Recommender System")
st.text("")
st.header("I Think You Might Like This Movie :popcorn::eyes:")
st.image("images/1_GKeESn8RruAbAUEm4k3_EQ.png")

st.write("""
How to design a recommendation system is a popular question appearing in the most recent system design
interviews for big tech companies. Thre reason is simple. Recommendation systems have become very 
important over the past few years. Amazon, Netflix, Spotify, YouTube and several other companies have
their own recommendation systems to make different kinds of suggestions to their users. Different
types of algorihms are used to track patterns in the kind of data utilized by the users on the app,
to suggest the most relevant material to each user from a large store of content
""")
st.subheader("About Content Base Filtering")
st.write("""
Based on the movies the user has watched, we can look into the metadata of the movies (overview,
genres, keywords, cast, crew...) and look for similar movies using these attributes. Idea is that
if a user watch some movie, he/she will watch a movie that is similar to it.\n
Pros:\n
-The model doesn't need any data about other users, since the recommendations are 
specific to this user. This makes it easier to scale to a large number of users.
    
-The model can capture the specific interests of a user, and canrecommend niche 
items that very few other users are interested in
     
Cons:\n
-Since the feature representation of the items are hand-engineered to some extent,
     this technique requires a lot of domain knowledge. Therefore, the model can only 
     be as good as the hand-engineered features.
     
-The model can only make recommendations based on existing interests of the user. 
    In other words, the model has limited ability to expand on the users' existing interests.
""")
st.markdown(":dart: Before Data PreProcessing :dart:")
st.image("images/before_pp.png")
st.text("")

st.markdown(":dart: After Data PreProcessing :dart:")
st.image("images/after.png")
st.text("")

st.markdown("Example Tag ->Toy Story:point_down:")
st.image("images/tag_toy_story.png")
st.text("")

st.markdown("Example Tag -> The 40 Year Old Virgin:point_down:")
st.image("images/tag_40_year_old.png")
st.text("")
