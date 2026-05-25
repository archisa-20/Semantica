# Semantica — Semantic Search Engine

A full-stack semantic search engine that retrieves results based on **meaning**, not keywords. Built with sentence embeddings and cosine similarity, visualized through an interactive vector-space map.

> Search *"a lonely astronaut drifting in silence"* and find **Interstellar** — even though those words never appear in its description.

![Semantica Preview](https://via.placeholder.com/900x450/0D0221/00FFFF?text=Semantica+Preview)

---

## How It Works

Traditional search looks for **exact keyword matches**. Semantica converts both your query and every movie description into high-dimensional **embedding vectors** using a pre-trained language model. It then measures the **cosine similarity** between your query vector and all stored vectors — returning results ranked by semantic closeness.

```
Your Query → Sentence Embedding → Query Vector
                                        ↓
                              Cosine Similarity with all stored vectors
                                        ↓
                              Top-K most semantically similar results
```

The right panel visualizes this as a **vector space map** — results closer to the center anchor are more semantically similar to your query.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Embedding Model | `all-MiniLM-L6-v2` via Sentence Transformers |
| Similarity Metric | Cosine Similarity (NumPy) |
| Backend API | Python · Flask · Flask-CORS |
| Frontend | HTML · CSS · Vanilla JS · HTML5 Canvas |
| Data | 200+ movies with rich descriptions, themes, and mood tags |

---

## Project Structure

```
semantic-search/
│
├── backend/
│   ├── app.py           # Flask API — POST /search endpoint
│   ├── data.py          # 200+ movies with descriptions, themes, mood
│   ├── search.py        # Standalone terminal search (for testing)
│   └── requirements.txt
│
└── frontend/
    └── semantica.html   # Full UI — connects to Flask backend
```

---

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/semantic-search.git
cd semantic-search
```

### 2. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 3. Start the backend
```bash
cd backend
python app.py
```
The model downloads once (~80MB) and pre-embeds all 200+ movies on startup. You'll see:
```
Loading model...
Embedding 200+ movies with rich profiles...
✅ Ready!
 * Running on http://localhost:5000
```

### 4. Open the frontend
Open `frontend/semantica.html` directly in your browser. No build step needed.

---

## API

### `POST /search`
```json
// Request
{ "query": "lonely astronaut in space", "top_k": 10 }

// Response
{
  "results": [
    {
      "title": "Interstellar",
      "description": "...",
      "genre": "Sci-Fi",
      "year": 2014,
      "score": 0.8423,
      "themes": ["love", "space", "sacrifice", "time"],
      "mood": ["epic", "emotional", "awe-inspiring"]
    }
  ]
}
```

### `GET /health`
```json
{ "status": "ok", "movies_indexed": 214 }
```

---

## Why Semantic > Keyword Search

| Query | Keyword Search | Semantica |
|---|---|---|
| "lonely person in space" | No results (exact words not in descriptions) | Interstellar, Gravity, Moon |
| "family hiding something dark" | Maybe Hereditary | Hereditary, Parasite, Get Out |
| "genius who destroys himself" | No results | Whiplash, Black Swan, Requiem for a Dream |

---

## Dataset

`data.py` contains **200+ films** across all genres, each enriched with:
- **Description** — 2-3 sentence plot summary
- **Themes** — semantic concepts (e.g. `grief, identity, survival`)
- **Mood** — emotional tone (e.g. `slow-burn, devastating, whimsical`)
- **Genre + Year** — for metadata display

The embedding pipeline combines all fields into a single rich text representation per movie, significantly improving retrieval accuracy over description-only embeddings.

---

## Planned Features
- [ ] Genre filter
- [ ] Minimum similarity threshold slider  
- [ ] Grid / list view toggle
- [ ] "More like this" — click a result to search by that movie
- [ ] TMDB API integration for posters and ratings

---

## Requirements

```
flask
flask-cors
sentence-transformers
numpy
```

Install:
```bash
pip install -r backend/requirements.txt
```

---

*Built as a demonstration of semantic search, NLP embeddings, and vector similarity — part of a data science engineering portfolio.*