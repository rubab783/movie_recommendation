# preprocess.py
import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Create model directory if not exists
os.makedirs("model", exist_ok=True)

# Load dataset files
# ---- Load data ----
movies = pd.read_csv("data/movie.csv")
links = pd.read_csv("data/link.csv")
ratings = pd.read_csv("data/rating.csv")
tags = pd.read_csv("data/tag.csv")

# ---- Reduce dataset for demo ----
movies = movies.head(2000)     # sirf 2000 movies
ratings = ratings[ratings['movieId'].isin(movies['movieId'])]  # un movies ke ratings

# Merge TMDB IDs from links
movies = movies.merge(links[['movieId', 'tmdbId']], on='movieId', how='left')

# Clean movie titles
movies['title'] = movies['title'].astype(str).apply(lambda x: re.sub(r'\s*\(\d{4}\)$', '', x).strip())
movies['genres'] = movies['genres'].fillna('').apply(lambda x: x.replace('|', ' '))

# Create a combined text feature for vectorization
movies['tags'] = (movies['title'] + ' ' + movies['genres']).fillna('')

# Vectorize the tags
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags'])

# Compute cosine similarity matrix
similarity = cosine_similarity(vectors)

# Save data for Streamlit app
pickle.dump(movies, open("model/movies.pkl", "wb"))
pickle.dump(similarity, open("model/similarity.pkl", "wb"))

print("✅ Preprocessing complete. Files saved to /model folder.")
