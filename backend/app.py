# app.py — Semantica Flask Backend
# Builds rich embeddings from title + description + themes + mood for better accuracy

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
import numpy as np
import os
from data import movies

app = Flask(__name__)
@app.route("/")
def home():
    return send_from_directory("../frontend", "semantic.html")
CORS(app)  # required so semantica.html can call this API

# ── Build a rich text representation for each movie ──────────────────
# This is the key upgrade: instead of embedding just the description,
# we embed a full semantic profile of each movie.
def build_rich_text(m):
    themes = ", ".join(m.get("themes", []))
    mood   = ", ".join(m.get("mood", []))
    return (
        f"{m['title']}. "
        f"{m['description']} "
        f"Genre: {m.get('genre', '')}. "
        f"Themes: {themes}. "
        f"Mood: {mood}."
    )

# ── Load model and pre-embed everything on startup ───────────────────
print("Loading model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
# Tip: swap to 'all-mpnet-base-v2' for better accuracy (slower, ~420MB)

rich_texts = [build_rich_text(m) for m in movies]
print(f"Embedding {len(movies)} movies with rich profiles...")
embeddings = model.encode(rich_texts, show_progress_bar=True)
print("✅ Ready!")

# ── Cosine similarity ─────────────────────────────────────────────────
def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

# ── Frontend route ───────────────────────────────────────────────────
# Serves the local semantic.html frontend at the app root.
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(os.path.dirname(__file__), 'semantic.html')

# ── Search endpoint ───────────────────────────────────────────────────
# Called by semantica.html via POST /search
# Body:    { "query": "your search text", "top_k": 10 }
# Returns: { "results": [{ title, description, genre, year, score }, ...] }
@app.route('/search', methods=['POST'])
def search():
    data  = request.get_json()
    query = (data.get('query') or '').strip()
    top_k = int(data.get('top_k', 10))

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    query_embedding = model.encode(query)
    scores = [cosine_similarity(query_embedding, emb) for emb in embeddings]

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        m = movies[idx]
        results.append({
            "title":       m["title"],
            "description": m["description"],
            "genre":       m.get("genre", "—"),
            "year":        m.get("year", "—"),
            "themes":      m.get("themes", []),
            "mood":        m.get("mood", []),
            "score":       round(scores[idx], 4),
        })

    return jsonify({'results': results})

# ── Health check ──────────────────────────────────────────────────────
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'movies_indexed': len(movies)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)