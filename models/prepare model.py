import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import ast

movies_m = pd.read_csv("datasets/movies_metadata.csv", low_memory=False)
df_credits = pd.read_csv("datasets/credits.csv")
df_keywords = pd.read_csv("datasets/keywords.csv")


def preprocess(df_meta, df_credits, df_keywords):
    df_meta = df_meta[df_meta["vote_count"] > 30]
    df_meta["id"] = pd.to_numeric(df_meta["id"], errors="coerce")
    df_meta = df_meta[~df_meta["id"].isnull()]

    df_tmp = df_meta.merge(df_credits, on="id", how="left")
    df = df_tmp.merge(df_keywords, on="id", how="left")
    df = df[["id", "imdb_id", "title", "overview", "genres", "keywords", "cast", "crew"]]

    df["genres"].fillna("[]", inplace=True)
    df["genres"] = df["genres"].apply(
        lambda x: [ast.literal_eval(x)[i]["name"] for i in range(0, len(ast.literal_eval(x)))])
    df["genres"] = df["genres"].apply(lambda x: ' '.join([i.replace(" ", "") for i in x]))

    df["keywords"].fillna("[]", inplace=True)
    df["keywords"] = df["keywords"].apply(
        lambda x: [ast.literal_eval(x)[i]["name"] for i in range(0, len(ast.literal_eval(x)))])
    df['keywords'] = df['keywords'].apply(lambda x: ' '.join([i.replace(" ", '') for i in x]))

    df["cast"].fillna("[]", inplace=True)
    df["cast"] = df["cast"].apply(
        lambda x: [ast.literal_eval(x)[i]["name"] for i in range(0, len(ast.literal_eval(x)))])
    df['cast'] = df['cast'].apply(lambda x: ' '.join([i.replace(" ", '') for i in x]))

    df["crew"].fillna("[]", inplace=True)
    df["crew"] = df["crew"].apply(
        lambda x: [ast.literal_eval(x)[i]["name"] for i in range(0, len(ast.literal_eval(x))) if
                   ast.literal_eval(x)[i]["job"] == "Director"])
    df["crew"] = df["crew"].apply(lambda x: ' '.join([i.replace(" ", '') for i in x]))

    df['overview'] = df['overview'].fillna('')

    df['tags'] = df['overview'] + " " + df['genres'] \
                 + " " + df['keywords'] + " " + df['cast'] + " " + df["crew"]

    df.drop(["genres", "overview", "keywords", "cast", "crew"], axis=1, inplace=True)

    return df


df = preprocess(movies_m, df_credits, df_keywords)
pickle.dump(df, open("models/movies_m.pkl", "wb"))


def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
    tfidf_matrix = tfidf.fit_transform(dataframe["tags"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim


cosine = calculate_cosine_sim(df)

pickle.dump(cosine, open("models/cosine_sim.pkl", "wb"))
