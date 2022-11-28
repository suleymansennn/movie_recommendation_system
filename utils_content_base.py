import requests
import pandas as pd

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=29838fb7de2d586b612c237ebb6b03d1"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def content_based_recommender(title, cosine_sim, dataframe):
    # index'leri olusturma
    indices = pd.Series(dataframe.index, index=dataframe['title'])
    indices = indices[~indices.index.duplicated(keep='last')]
    # title'ın index'ini yakalama
    movie_index = indices[title]
    # title'a gore benzerlik skorlarını hesapalama
    similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])
    # kendisi haric ilk 10 filmi getirme
    movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    recommended_movies = dataframe['title'].iloc[movie_indices]
    movie_names = []
    movie_posters = []
    for j, index in enumerate(recommended_movies.index):
        movie_id = dataframe.loc[dataframe.index == index, "imdb_id"]
        movie_posters.append(fetch_poster(movie_id.values[0]))
        movie_names.append(recommended_movies[index])
    return movie_names, movie_posters
