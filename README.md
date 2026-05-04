# 🔍 Semantic Search Engine

A semantic search engine built with Python and Sentence Transformers.
Understands the **meaning** of your query, not just keywords.

## How it works
- Text is converted into vectors using `all-MiniLM-L6-v2`
- Query vector is compared to all stored vectors using cosine similarity
- Top matches are returned ranked by relevance

## Setup
```bash
pip install -r requirements.txt
python search.py
```

## Tech Used
- `sentence-transformers`
- `numpy`
- HuggingFace `all-MiniLM-L6-v2` model