# 🎬 Smart Movie Recommendation System

A **Streamlit-based web app** that recommends movies similar to the one you like using **content-based filtering** and **TMDB API** for fetching movie posters. Built as a university project to demonstrate practical application of Python, data processing, and web deployment.

---

## 🛠 Features

- Select a movie and get **6 similar movie recommendations**  
- Dynamic fetching of **movie posters** using TMDB API  
- User-friendly **interactive interface** with responsive layout  
- Smooth, **custom-styled UI** using Streamlit and CSS  
- Handles missing posters gracefully with placeholders  

---

## 📂 Files in the Project

- `app.py` – Main Streamlit app  
- `movies.pkl` – Pickled DataFrame containing movie metadata  
- `similarity.pkl` – Pickled similarity matrix for recommendations  
- `requirements.txt` – Python dependencies for the project  
- `data/` (optional) – CSV or supporting data if needed  

---

## ⚡ Technologies Used

- **Python 3.13**  
- **Streamlit** – Web app framework  
- **Pandas** – Data manipulation  
- **Scikit-learn** – Machine learning (similarity calculations)  
- **Requests** – API calls to TMDB  
- **Pickle** – Load pre-processed datasets  
- **dotenv** – Load API keys from environment variables  

---

## 🚀 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/movie_recommendation.git
cd movie_recommendation

Install dependencies

pip install -r requirements.txt


Set up API key

Create a .env file in the root directory:

TMDB_API_KEY="your_tmdb_api_key_here"


Run the app


streamlit run app.py
Open the URL shown in the terminal to view the app in your browser

🧩 How It Works

User selects a movie from a dropdown list

The app retrieves the similarity scores for the selected movie

Top 8 similar movies are selected

TMDB API is used to fetch the poster images for each recommended movie

Recommendations are displayed in a responsive grid

⚠️ Notes

Ensure the .pkl files are in the root directory or accessible via URLs

API requests require an active TMDB API key

If a movie poster is missing, a placeholder image will appear