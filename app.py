import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Streamlit config
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Custom CSS
st.markdown("""
<style>
:root {
  --bg: #0b1220;
  --card: #111a2f;
  --muted: #9fb0d6;
  --accent: #06b6d4;
  --text: #e6eef8;
  --shadow: 0 4px 15px rgba(0,0,0,0.4);
}
[data-testid="stAppViewContainer"] {
  background-color: var(--bg);
  color: var(--text);
  font-family: 'Poppins', sans-serif;
}
h1 {
  color: var(--accent);
  text-align: center;
  font-weight: 700;
}
.stButton button {
  background-color: var(--accent);
  color: #fff;
  border: none;
  padding: 0.6rem 1.4rem;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}
.stButton button:hover {
  background-color: #0891b2;
  transform: scale(1.05);
}
.poster {
  border-radius: 10px;
  width: 100%;
  height: 260px;
  object-fit: cover;
  margin-bottom: 8px;
  box-shadow: var(--shadow);
}
.movie-title {
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 4px;
  text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Load data
movies = pickle.load(open("model/movies.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

# Cached poster fetch
@st.cache_data(show_spinner=False)
def fetch_poster(tmdb_id):
    if not tmdb_id or pd.isna(tmdb_id):
        return "https://via.placeholder.com/342x513?text=No+Poster"
    try:
        url = f"https://api.themoviedb.org/3/movie/{int(tmdb_id)}?api_key={TMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return "https://image.tmdb.org/t/p/w342" + poster_path
    except Exception:
        pass
    return "https://via.placeholder.com/342x513?text=No+Poster"

# Recommend function
def recommend(movie):
    try:
        idx = movies[movies['title'] == movie].index[0]
        distances = similarity[idx]
        movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:9]
        recommended_movies, recommended_posters = [], []
        for i in movie_list:
            movie_row = movies.iloc[i[0]]
            recommended_movies.append(movie_row['title'])
            recommended_posters.append(fetch_poster(movie_row['tmdbId']))
        return recommended_movies, recommended_posters
    except IndexError:
        return [], []

# UI
st.markdown("<h1>🎞️ Smart Movie Recommendation System</h1>", unsafe_allow_html=True)
st.write("Select a movie to get similar recommendations based on content features.")

selected_movie = st.selectbox("🎬 Select a movie you like:", movies['title'].values)

if st.button("Recommend"):
    with st.spinner("Finding similar movies... 🎥"):
        names, posters = recommend(selected_movie)

    if names:
        st.markdown("### Recommended Movies:")
        cols = st.columns(len(names))
        for i, col in enumerate(cols):
            with col:
                st.image(posters[i], use_container_width=True)
                st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
    else:
        st.error("No recommendations found. Try another movie.")
